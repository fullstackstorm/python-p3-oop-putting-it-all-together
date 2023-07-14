#!/usr/bin/env python3

class Shoe:
    condition = None

    def __init__(self, brand="Prada", size=6):
        self.set_brand(brand)
        self.set_size(size)
    
    def set_brand(self, brand):
        self.__brand = brand

    def get_brand(self):
        return self.__brand
    
    def set_size(self, size):
        if isinstance(size, int):
            self.__size = size
        else:
            print("size must be an integer")

    def get_size(self):
        return self.__size
    
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"        
    
    brand = property(get_brand, set_brand)
    size = property(get_size, set_size)