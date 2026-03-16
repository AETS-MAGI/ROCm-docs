#!/usr/bin/env python3
"""Chapter 02: Numbers as tables (NumPy basics)."""

import numpy as np


def main() -> None:
	x = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float32)

	print("x:")
	print(x)
	print("shape:", x.shape)
	print("dtype:", x.dtype)
	print("rows:", x.shape[0])
	print("cols:", x.shape[1])


if __name__ == "__main__":
	main()
