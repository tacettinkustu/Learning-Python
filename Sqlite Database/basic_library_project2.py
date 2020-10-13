from basic_library_project import *

print("""***********************************

Welcome Library.

Processes;

1. Show Books

2. Query Books

3. Add Books

4. Delete Books

5. Upgrade Edition

To exit press 'q'.
***********************************""")

library = Library()

while True:
    process = input("Your Process:")

    if (process == "q"):
        print("Ending.....")
        print("See you soon....")
        break
    elif (process == "1"):
        library.show_books()

    elif (process == "2"):
        name = input("Which book do you want ? ")
        print("Query...")
        time.sleep(2)

        library.query_book(name)

    elif (process == "3"):
        name = input("Name:")
        author = input("Author:")
        publisher = input("Publisher:")
        genre = input("Genre:")
        edition = int(input("Edition:"))

        new_book = Book(name,author,publisher,genre,edition)

        print("Adding book....")
        time.sleep(2)

        library.add_book(new_book)
        print("Book added....")


    elif (process == "4"):
        name = input("Which book do you want to delete ?")

        answer = input("Sure? (Y/N)")
        if (answer == "Y"):
            print("Deleting...")
            time.sleep(2)
            library.delete_book(name)
            print("Book Deleted....")


    elif (process == "5"):
        name = input("Which book do you want to upgrade ?")
        print("Edition upgrading....")
        time.sleep(2)
        library.upgrade_edition(name)
        print("Edition Upgraded....")

    else:
        print("Unfollowed process...")
