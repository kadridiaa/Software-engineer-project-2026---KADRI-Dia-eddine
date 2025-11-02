import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
from src.factory import get_compressor
from src.overflow import BitPackingOverflow
import time

class BitPackingGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("BitPacking Compression Demo")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Enter integers (comma-separated):").grid(row=0, column=0, sticky="w")
        self.entry_array = tk.Entry(self.root, width=50)
        self.entry_array.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Choose compression mode:").grid(row=1, column=0, sticky="w")
        self.mode_var = tk.StringVar(value="classic")
        tk.Radiobutton(self.root, text="Classic", variable=self.mode_var, value="classic").grid(row=1, column=1, sticky="w")
        tk.Radiobutton(self.root, text="Strict", variable=self.mode_var, value="strict").grid(row=1, column=1)
        tk.Radiobutton(self.root, text="Overflow", variable=self.mode_var, value="overflow").grid(row=1, column=1, sticky="e")

        self.run_button = tk.Button(self.root, text="Run Compression", command=self.run_compression)
        self.run_button.grid(row=3, column=0, columnspan=2, pady=10)

        tk.Label(self.root, text="Results:").grid(row=4, column=0, sticky="nw")
        self.output_text = scrolledtext.ScrolledText(self.root, width=80, height=25)
        self.output_text.grid(row=4, column=1, padx=5, pady=5)

    def run_compression(self):
        self.output_text.delete(1.0, tk.END)
        raw_input = self.entry_array.get()
        try:
            arr = [int(x.strip()) for x in raw_input.split(",")]
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid integers separated by commas.")
            return

        mode = self.mode_var.get()
        try:
            if mode in ["classic", "strict"]:
                compressor = get_compressor(mode)
                self.run_standard(arr, compressor, mode)
            elif mode == "overflow":
                self.run_overflow(arr)
            else:
                messagebox.showerror("Mode Error", "Unknown compression mode.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def run_standard(self, arr, compressor, label):
        self.output_text.insert(tk.END, f"==== {label.capitalize()} ====\n")
        self.output_text.insert(tk.END, f"Original array: {arr}\n")
        bits = compressor._compute_bits_per_int(arr)
        self.output_text.insert(tk.END, f"Detected bits_per_int = {bits}\n")

        start = time.time()
        compressed = compressor.compressarray(arr)
        end = time.time()
        self.output_text.insert(tk.END, f"Compressed: {compressed}\n")
        compress_time = end - start
        self.output_text.insert(tk.END, f"Time to compress: {compress_time:.6f} seconds\n")

        start = time.time()
        decompressed = compressor.decompressarray(compressed, len(arr))
        end = time.time()
        decompress_time = end - start
        self.output_text.insert(tk.END, f"Decompressed: {decompressed}\n")
        self.output_text.insert(tk.END, f"Time to decompress: {decompress_time:.6f} seconds\n")

        # Taux de compression
        compressed_size_ints = len(compressed)
        compression_ratio = compressed_size_ints / len(arr)
        self.output_text.insert(tk.END, f"Compression ratio: {compression_ratio:.2f} ({compressed_size_ints} ints vs {len(arr)} original)\n")

        start = time.time()
        for i in range(len(arr)):
            val = compressor.getint(compressed, i)
            assert val == arr[i], f"Mismatch at index {i}: {val} != {arr[i]}"
        end = time.time()
        self.output_text.insert(tk.END, f"Time for direct access: {end - start:.6f} seconds\n")
        self.output_text.insert(tk.END, "Decompression successful!\n\n")

        # Accès interactif à un élément
        self.access_element_gui(compressor, compressed, arr)

    def run_overflow(self, arr):
        self.output_text.insert(tk.END, f"==== Overflow (automatic threshold) ====\n")
        self.output_text.insert(tk.END, f"Original array: {arr}\n")

        bp = BitPackingOverflow(arr)

        start = time.time()
        packed, overflow = bp.compressarray(arr)
        end = time.time()
        compress_time = end - start
        self.output_text.insert(tk.END, f"Packed array: {packed}\n")
        self.output_text.insert(tk.END, f"Overflow area: {overflow}\n")
        self.output_text.insert(tk.END, f"Display format x-y: {bp.get_display()}\n")
        self.output_text.insert(tk.END, f"Time to compress: {compress_time:.6f} seconds\n")

        start = time.time()
        decompressed = bp.decompressarray(packed, overflow)
        end = time.time()
        decompress_time = end - start
        self.output_text.insert(tk.END, f"Decompressed: {decompressed}\n")
        self.output_text.insert(tk.END, f"Time to decompress: {decompress_time:.6f} seconds\n")

        # Taux de compression
        compressed_size_ints = len(packed) + len(overflow)
        compression_ratio = compressed_size_ints / len(arr)
        self.output_text.insert(tk.END, f"Compression ratio: {compression_ratio:.2f} ({compressed_size_ints} ints vs {len(arr)} original)\n")

        start = time.time()
        for i in range(len(arr)):
            val = bp.getint(packed, overflow, i)
            assert val == arr[i], f"Mismatch at index {i}: {val} != {arr[i]}"
        end = time.time()
        self.output_text.insert(tk.END, f"Time for direct access: {end - start:.6f} seconds\n")
        self.output_text.insert(tk.END, "Overflow decompression successful!\n\n")

        # Accès interactif à un élément
        self.access_element_gui(bp, (packed, overflow), arr, overflow_mode=True)

    def access_element_gui(self, compressor, compressed_data, arr, overflow_mode=False):
        while True:
            idx_input = simpledialog.askstring("Access Element", f"Enter index to access (0 to {len(arr)-1}) or leave empty to quit:")
            if not idx_input:
                break
            try:
                idx = int(idx_input)
                if idx < 0 or idx >= len(arr):
                    messagebox.showwarning("Index Error", f"Index out of range (0-{len(arr)-1})")
                    continue
                if overflow_mode:
                    val = compressor.getint(*compressed_data, idx)
                else:
                    val = compressor.getint(compressed_data, idx)
                self.output_text.insert(tk.END, f"Element at index {idx}: {val}\n")
            except ValueError:
                messagebox.showwarning("Input Error", "Please enter a valid integer.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BitPackingGUI(root)
    root.mainloop()
