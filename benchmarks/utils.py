# benchmarks/utils.py
import time

def timed_run(bp, arr, mode="Classic"):
    """Mesure compress/decompress/getint pour n'importe quel tableau."""
    # 
    start_c = time.perf_counter()
    compressed = bp.compressarray(arr)
    end_c = time.perf_counter()

    # 
    if isinstance(compressed, tuple):
        decompressed = bp.decompressarray(*compressed, len(arr))
    else:
        decompressed = bp.decompressarray(compressed, len(arr))
    end_d = time.perf_counter()

    # Accès direct
    start_g = time.perf_counter()
    for i in range(len(arr)):
        if isinstance(compressed, tuple):
            val = bp.getint(*compressed, i)
        else:
            val = bp.getint(compressed, i)
        assert val == arr[i], f"Mismatch at index {i}: {val} != {arr[i]}"
    end_g = time.perf_counter()

    # Tailles
    if isinstance(compressed, tuple):
        packed, overflow = compressed
        compressed_size_ints = len(packed) + len(overflow)
    else:
        compressed_size_ints = len(compressed)

    return {
        "compressed": compressed,
        "decompressed": decompressed,
        "compress_time": end_c - start_c,
        "decompress_time": end_d - end_c,
        "get_time": end_g - start_g,
        "compressed_size_ints": compressed_size_ints,
        "mode": mode
    }
