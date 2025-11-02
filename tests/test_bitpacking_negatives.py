import unittest
from src.bitpacking import BitPackingClassic
from src.bitpacking_strict import BitPackingStrict


class TestBitPackingNegatives(unittest.TestCase):
    def test_classic_with_negatives(self):
        arr = [-10, -5, 0, 3, 7, 10]
        bp = BitPackingClassic()
        bp._compute_bits_per_int(arr)
        compressed = bp.compressarray(arr)
        decompressed = bp.decompressarray(compressed, len(arr))
        self.assertEqual(decompressed, arr)
        for i in range(len(arr)):
            self.assertEqual(bp.getint(compressed, i), arr[i])

    def test_strict_with_negatives(self):
        arr = [-20, -1, 0, 12, 64]
        bp = BitPackingStrict()
        bp._compute_bits_per_int(arr)
        compressed = bp.compressarray(arr)
        decompressed = bp.decompressarray(compressed, len(arr))
        self.assertEqual(decompressed, arr)
        for i in range(len(arr)):
            self.assertEqual(bp.getint(compressed, i), arr[i])

