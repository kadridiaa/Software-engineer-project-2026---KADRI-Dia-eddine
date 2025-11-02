import unittest
from src.overflow import BitPackingOverflow

class TestBitPackingOverflow(unittest.TestCase):
    def test_compress_decompress(self):
        arr = [1, 500, 4, 600]
        bp = BitPackingOverflow(arr)
        packed, overflow = bp.compressarray(arr)
        decompressed = bp.decompressarray(packed, overflow)
        self.assertEqual(decompressed, arr)

    def test_getint(self):
        arr = [1, 150, 4, 7, 200]
        bp = BitPackingOverflow(arr)
        packed, overflow = bp.compressarray(arr)
        for i, val in enumerate(arr):
            self.assertEqual(bp.decompressarray(packed, overflow)[i], val)

if __name__ == '__main__':
    unittest.main() 