# -*- coding: utf-8 -*-
"""komputer.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KTIlbqRm-0yhqolkDeQCo2K8DexVBqgX
"""

class Komputer:
    def __init__(self, merk, processor):
        self.merk = merk
        self.processor = processor

    def spesifikasi(self):
        print(f"Komputer {self.merk} dengan prosesor {self.processor}.")

# Objek
pc = Komputer("Asus", "Intel i7")
pc.spesifikasi()