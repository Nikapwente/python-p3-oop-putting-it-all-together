#!/usr/bin/env python3

class Shoe:
    pass
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    def get_shoe_size(self):
            return self._size

    def set_shoe_size(self, size=0):
            if (type(size) == (int)):
                self._size = size
            else:
                print("size must be an integer")

    size = property(get_shoe_size, set_shoe_size,)

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")