import unittest
from src.bitpacking import BitPackingClassic

class TestBitPackingClassic(unittest.TestCase):
    def test_compress_decompress(self):
        arr = [1, 2, 3, 4, 5]
        bp = BitPackingClassic()
        bp._compute_bits_per_int(arr)
        compressed = bp.compressarray(arr)
        decompressed = bp.decompressarray(compressed, len(arr))
        self.assertEqual(decompressed, arr)

    def test_getint(self):
        arr = [17, 2, 10]
        bp = BitPackingClassic()
        bp._compute_bits_per_int(arr)
        compressed = bp.compressarray(arr)
        self.assertEqual(bp.getint(compressed, 2), arr[2])
