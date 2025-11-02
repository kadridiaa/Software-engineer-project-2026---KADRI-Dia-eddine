class BitPackingOverflow:
    """BitPackingOverflow support négatifs et affichage x-y."""

    def __init__(self, arr):
        self.arr = arr
        self.threshold = max(abs(x) for x in arr) // 4  # threshold automatique simplifié
        self.flag_bit = 1

    def compressarray(self, arr):
        packed = []
        overflow = []
        display = []
        for x in arr:
            if abs(x) <= self.threshold:
                packed.append(x)
                display.append(f"0-{x}")
            else:
                overflow.append(x)
                idx = len(overflow) - 1
                packed.append(self.threshold if x > 0 else -self.threshold)
                display.append(f"1-{idx}")
        self.display = display
        return packed, overflow

    def decompressarray(self, packed, overflow):
        result = []
        overflow_idx = 0
        for i, x in enumerate(packed):
            if abs(x) == self.threshold:
                result.append(overflow[overflow_idx])
                overflow_idx += 1
            else:
                result.append(x)
        return result

    def get_display(self):
        return self.display