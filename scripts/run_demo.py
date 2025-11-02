# scripts/run_demo.py
from src.factory import get_compressor
from src.overflow import BitPackingOverflow
from benchmarks.utils import timed_run
import time

def compute_compression_ratio(original_len, compressed_len, bits_per_int):
    original_bits = original_len * 32
    compressed_bits = compressed_len * bits_per_int
    ratio = original_bits / compressed_bits if compressed_bits != 0 else 0
    return ratio, original_bits, compressed_bits

def run_overflow(arr):
    print("\n==== Overflow (automatic threshold) ====")
    print(f"Original array: {arr}")

    bp = BitPackingOverflow(arr)

    start = time.perf_counter()
    packed, overflow = bp.compressarray(arr)
    end = time.perf_counter()
    print(f"Packed array: {packed}")
    print(f"Overflow area: {overflow}")
    print(f"Display format x-y: {bp.get_display()}")
    print(f"Time to compress: {end - start:.6f} seconds")

    # Ratio
    total_len = len(packed) + len(overflow)
    ratio, orig_bits, comp_bits = compute_compression_ratio(len(arr), total_len, bp.bits_per_int)
    print(f"Compression ratio: {ratio:.2f}x ({orig_bits} bits → {comp_bits} bits)")

    start = time.perf_counter()
    decompressed = bp.decompressarray(packed, overflow)
    end = time.perf_counter()
    print(f"Decompressed: {decompressed}")
    print(f"Time to decompress: {end - start:.6f} seconds")

    print("Overflow decompression successful!\n")

def main():
    raw_input_array = input("Enter integers separated by commas: ")
    try:
        arr = [int(x.strip()) for x in raw_input_array.split(",")]
    except ValueError:
        print("Please enter valid integers separated by commas.")
        return

    print("\nChoose compression mode:")
    print("1 - Classic")
    print("2 - Strict")
    print("3 - Overflow")
    choice = input("Enter choice (1/2/3): ").strip()

    if choice in ["1", "2"]:
        mode = "Classic" if choice == "1" else "Strict"
        compressor = get_compressor(mode.lower())
        bits = compressor._compute_bits_per_int(arr)
        print(f"\n==== {mode} Mode ====")
        print(f"Detected bits_per_int = {bits}")

        result = timed_run(compressor, arr, mode=mode)
        compressed = result["compressed"]
        decompressed = result["decompressed"]

        print(f"Compressed: {compressed}")
        print(f"Decompressed: {decompressed}")
        print(f"Time to compress: {result['compress_time']:.6f} s")
        print(f"Time to decompress: {result['decompress_time']:.6f} s")
        print(f"Time for direct access: {result['get_time']:.6f} s")

        # Ajout du taux de compression
        ratio, orig_bits, comp_bits = compute_compression_ratio(len(arr), len(compressed), bits)
        print(f"Compression ratio: {ratio:.2f}x ({orig_bits} bits → {comp_bits} bits)\n")

    elif choice == "3":
        run_overflow(arr)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
