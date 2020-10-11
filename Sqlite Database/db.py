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
def get_data():
    cursor.execute("SELECT * FROM library")
    list1 = cursor.fetchall()
    for i in list1:
        print(i)
def get_data2():
    cursor.execute("SELECT name,author FROM library")
    list1 = cursor.fetchall()
    for i in list1:
        print(i)
def get_data3(name):
    cursor.execute("SELECT * FROM library WHERE name = ?",(name,))
    list1 = cursor.fetchall()
    for i in list1:
        print(i)

#name = input("Name:")
#author = input("Author:")
#book_name = input("Book name:")
#page =  int(input("Page:"))

#get_data()
# add_input(name,author,book_name,page)
#get_data2()
get_data3("İstanbul Hatırası")
con.close()