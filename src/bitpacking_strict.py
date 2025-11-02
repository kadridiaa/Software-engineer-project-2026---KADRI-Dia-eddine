class BitPackingStrict:
    """BitPackingStrict avec overlap et support des négatifs."""

    def __init__(self, bits_per_int=None):
        self.bits_per_int = bits_per_int
        self.offset = 0

    def _compute_bits_per_int(self, arr):
        if not arr:
            self.bits_per_int = 1
            return 1
        max_val = max(arr)
        min_val = min(arr)
        if min_val < 0:
            bits = max(abs(max_val), abs(min_val)).bit_length() + 1
        else:
            bits = max_val.bit_length()
        self.bits_per_int = max(bits, 1)
        return self.bits_per_int

    def compressarray(self, arr):
        if self.bits_per_int is None:
            self._compute_bits_per_int(arr)
        if not arr:
            return []
        self.offset = -min(arr) if min(arr) < 0 else 0
        mask = (1 << self.bits_per_int) - 1
        result = []
        accu = 0
        bits_in_accu = 0
        for x in arr:
            val = (x + self.offset) & mask
            accu |= val << bits_in_accu
            bits_in_accu += self.bits_per_int
            while bits_in_accu >= 32:
                result.append(accu & 0xFFFFFFFF)
                accu >>= 32
                bits_in_accu -= 32
        if bits_in_accu > 0:
            result.append(accu)
        return result

    def decompressarray(self, arr_compressed, n):
        bits = self.bits_per_int
        mask = (1 << bits) - 1
        result = []
        if not arr_compressed:
            return result
        accu = arr_compressed[0]
        bits_in_accu = 32
        i_in_compressed = 1
        for _ in range(n):
            if bits_in_accu < bits and i_in_compressed < len(arr_compressed):
                accu |= arr_compressed[i_in_compressed] << bits_in_accu
                bits_in_accu += 32
                i_in_compressed += 1
            val = accu & mask
            result.append(val - self.offset)
            accu >>= bits
            bits_in_accu -= bits
        return result

    def getint(self, arr_compressed, i):
        bits = self.bits_per_int
        bit_pos = i * bits
        block_idx = bit_pos // 32
        offset = bit_pos % 32
        mask = (1 << bits) - 1
        val = (arr_compressed[block_idx] >> offset) & mask
        if offset + bits > 32 and block_idx + 1 < len(arr_compressed):
            part1 = arr_compressed[block_idx] >> offset
            part2 = arr_compressed[block_idx + 1] & ((1 << (offset + bits - 32)) - 1)
            val = (part2 << (32 - offset)) | part1
            val &= mask
        return val - self.offset