# General matrix multiply test

    # Wall Fame
    # Results N = 8192
    # Cooler: 72 GFLOPS float64, 148 GFLOPS float32
    # RAN-DPP9043: 382 GFLOPS float64, 850 GFLOPS float32


import time
import numpy as np

N = 8192

# Multiply matrices C = A @ B

if __name__ == "__main__":
    # A = np.random.randn(N,N)
    # B = np.random.randn(N,N)
    A = np.random.randn(N,N).astype(np.float32)
    B = np.random.randn(N,N).astype(np.float32)
    

    # Time flops

    flop = N*N*2*N

    print(f"{flop / 1e9:.2f}, GFLOP")

    st = time.monotonic()
    C = A @ B
    en = time.monotonic()
    s = en-st

    print(f"{flop / s * 1e-9:.2f}, GFLOPS")
