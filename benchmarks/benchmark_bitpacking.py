from src.bitpacking import BitPackingClassic
from src.bitpacking_strict import BitPackingStrict
from src.overflow import BitPackingOverflow
from benchmarks.utils import timed_run

def benchmark():
    arr = [i % 128 for i in range(10000)] + [10**6, 10**7]

    bp_classic = BitPackingClassic(8)
    bp_strict = BitPackingStrict(8)
    bp_overflow = BitPackingOverflow([0])  # tableau factice pour init

    for label, bp in [("Classic", bp_classic), ("Strict", bp_strict), ("Overflow", bp_overflow)]:
        results = timed_run(bp, arr, label)
        print(f"\n==== {label} ====")
        print(f"Compressed size (ints): {results['compressed_size_ints']}")
        print(f"Time to compress: {results['compress_time']:.6f} s")
        print(f"Time to decompress: {results['decompress_time']:.6f} s")
        print(f"Time for direct access get(i): {results['get_time']:.6f} s")
