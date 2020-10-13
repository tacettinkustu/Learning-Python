import sqlite3

import time

class Book():

    def __init__(self,name,author,publisher,genre,edition):

        self.name = name
        self.author = author
        self.publisher = publisher
        self.genre = genre
        self.edition = edition

    def __str__(self):
        return "Book's Name : {}\n Author : {}\n Publisher : {}\n Genre : {}\n Edition : {}\n".format(self.name,self.author,self.publisher,self.genre,self.edition)


class Library():

    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.connection = sqlite3.connect("library1.db")
        self.cursor = self.connection.cursor()
        query = "Create Table If not exists books (name TEXT,author TEXT,publisher TEXT,genre TEXT,edition INT)"
        self.cursor.execute(query)
        self.connection.commit()

    def close_conneection(self):
        self.connection.close()

    def show_books(self):

        query = "Select * From books"

        self.cursor.execute(query)

        books = self.cursor.fetchall()

        if (len(books) == 0):
            print("There is no book in the library...")
        else:
            for i in books:
                book = Book(i[0], i[1], i[2], i[3], i[4])
                print(book)

    def query_book(self, name):

        query = "Select * From books where name = ?"

        self.cursor.execute(query,(name,))

        books = self.cursor.fetchall()

        if (len(books) == 0):
            print("There is no book in the library with this name.....")
        else:
            book = Book(books[0][0], books[0][1], books[0][2], books[0][3], books[0][4])

            print(book)

    def add_book(self, book):

        query = "Insert into books Values(?,?,?,?,?)"

        self.cursor.execute(query, (book.name, book.author, book.publisher, book.genre, book.edition,))

        self.connection.commit()

    def delete_book(self, name):

        query = "Delete From books where name = ?"

        self.cursor.execute(query, (name,))

        self.connection.commit()

    def upgrade_edition(self, name):

        query = "Select * From books where name = ?"

        self.cursor.execute(query, (name,))

        books = self.cursor.fetchall()

        if (len(books) == 0):
            print("There is no book in the library with this name...")
        else:
            edition = books[0][4]

            edition += 1

            query2 = "Update books set edition = ? where name = ?"

            self.cursor.execute(query2, (edition, name))

            self.connection.commit()