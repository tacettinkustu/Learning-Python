import sqlite3
con = sqlite3.connect("library.db")
cursor = con.cursor()
def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS library (name TEXT, author TEXT,book_name TEXT,page INT)")
    con.commit()
def add_data():
    cursor.execute("INSERT INTO library VALUES('İstanbul Hatırası','Ahmet Ümit','Everest',561)")
    con.commit()
def add_input(name,author,book_name,page):
    cursor.execute("INSERT INTO library VALUES(?,?,?,?)",(name,author,book_name,page))
    con.commit()


name = input("Name:")
author = input("Author:")
book_name = input("Book name:")
page =  int(input("Page:"))

add_input(name,author,book_name,page)
con.close()