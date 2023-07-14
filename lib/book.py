#!/usr/bin/env python3

class Book:
    
    def __init__(self, title = "The Shining", page_count = "450"):
        self.set_title(title)
        self.set_page_count(page_count)

    def get_title(self):
        return self.__title
    
    def set_title(self, title):
        self.__title = title

    def get_page_count(self):
        return self.__page_count
    
    def set_page_count(self, page_count):
        if isinstance(page_count, int):
            self.__page_count = page_count
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    title = property(get_title, set_title)
    page_count = property(get_page_count, set_page_count)

    
        