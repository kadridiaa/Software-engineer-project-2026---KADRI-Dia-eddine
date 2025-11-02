from src.bitpacking import BitPackingClassic
from src.bitpacking_strict import BitPackingStrict

def get_compressor(mode="classic", bits_per_int=None):
    if mode == "classic":
        return BitPackingClassic(bits_per_int)
    elif mode == "strict":
        return BitPackingStrict(bits_per_int)
    else:
        raise ValueError(f"Unknown compression mode: {mode}")
