class BitPackingClassic:
    """BitPackingClassic sans overlap, support négatifs."""

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
        arr_offset = [x + self.offset for x in arr]
        bits = self.bits_per_int
        block_size = 32
        result = []
        accu = 0
        bits_in_accu = 0
        for x in arr_offset:
            if bits_in_accu + bits > block_size:
                result.append(accu)
                accu = 0
                bits_in_accu = 0
            accu |= (x << bits_in_accu)
            bits_in_accu += bits
        if bits_in_accu > 0:
            result.append(accu)
        return result

    def decompressarray(self, arr_compressed, n):
        bits = self.bits_per_int
        block_size = 32
        result = []
        idx = 0
        for block in arr_compressed:
            bits_in_block = 0
            while bits_in_block + bits <= block_size and idx < n:
                val = (block >> bits_in_block) & ((1 << bits) - 1)
                result.append(val - self.offset)
                bits_in_block += bits
                idx += 1
        return result

    def getint(self, arr_compressed, i):
        bits = self.bits_per_int
        block_size = 32
        ints_per_block = block_size // bits
        block_idx = i // ints_per_block
        offset_in_block = (i % ints_per_block) * bits
        val = (arr_compressed[block_idx] >> offset_in_block) & ((1 << bits) - 1)
        return val - self.offset

