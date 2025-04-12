#Encapsulation

class Author:
    def __init__(self, name):
        self.__name = name

    def get_data(self):
        return f"{self.__name}"
    
    def get_name(self):
        return self.__name
    
    def set_name(self, new_name):
        self.__name = new_name

class Book:
    def __init__(self, title, author: Author):
        self.__title = title
        self.__author = author

    def display(self):
        print(f"'{self.__title}' written by {self.__author.get_data()}")

    def get_title(self):
        return self.__title
    
    def set_title(self, new_title):
        self.__title = new_title

author1 = Author("Regigigas")
book1 = Book ("Rock On", author1)

book1.display()

book1.set_title("Under The Torrent")
author1.set_name("Kyogre")

book1.display()