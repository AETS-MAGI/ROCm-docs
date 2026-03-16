#!/usr/bin/env python3
"""Chapter 03: Table-by-table math (matrix multiply with NumPy)."""

import numpy as np


def main() -> None:
    a = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float32)
    b = np.array([[7, 8], [9, 10], [11, 12]], dtype=np.float32)
    c = a @ b

    print("a.shape:", a.shape)
    print("b.shape:", b.shape)
    print("c.shape:", c.shape)
    print(c)


if __name__ == "__main__":
    main()
