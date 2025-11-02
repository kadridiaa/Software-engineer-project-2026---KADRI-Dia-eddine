import unittest
from src.bitpacking_strict import BitPackingStrict


class TestBitPackingStrict(unittest.TestCase):
    def test_compress_decompress(self):
        arr = [42, 56, 77]
        bp = BitPackingStrict()
        bp._compute_bits_per_int(arr)
        compressed = bp.compressarray(arr)
        decompressed = bp.decompressarray(compressed, len(arr))
        self.assertEqual(decompressed, arr)

    def test_getint(self):
        arr = [100, 255, 3]
        bp = BitPackingStrict()
        bp._compute_bits_per_int(arr)
        compressed = bp.compressarray(arr)
        self.assertEqual(bp.getint(compressed, 1), arr[1])