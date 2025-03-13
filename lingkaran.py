# -*- coding: utf-8 -*-
"""lingkaran.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WynnyclAw1mbOx5D-AJfD3X4MUrFIVAh
"""

import math

class Lingkaran:
    def __init__(self, radius):
        self.radius = radius

    def buat_lingkaran(self):
        luas = math.pi * self.radius ** 2
        print(f"Lingkaran dengan radius {self.radius} memiliki luas {luas:.2f}.")

# Objek
blt = Lingkaran(10)
blt.buat_lingkaran()