How to Use project_library.py ?

•Menu 1: Add

    To add a book, enter "add."
    Enter ISBN number, book name, and author.
    Information (ISBN, Book Name, Author, T) is added to books.txt.
    Type "cont" to continue adding books.
    Type "q" to exit and go back to the main menu.


•Menu 2: Register

    To register a student, enter "register."
    Enter student name, student surname, and student ID.
    Information (Name, Surname, ID) is added to students.txt.
    Type "cont" to continue adding books.
    Type "q" to exit and go back to the main menu.


•Menu 3: Delete

    To delete , enter "delete."
    Submenus:
        "book": Enter ISBN number or book name to remove from books.txt.
        "student": Enter Studen ID or Surname to remove from students.txt.

•Menu 4: Find

    To search, enter "find."
    Submenus:
        "books": Search in books.txt by ISBN, book name, or author.
        "students": Search in students.txt by student number or name.
        "taken": Search in taken_books.txt by student name or number to see 
        borrowed books.


•Menu 5: Give

    To give a book, enter "give."
    Enter the book to give ("takenn_book").
    Checks if the book is in the library (T/F).
    If F, continue the process.
    If T, give an error and exit.
    Enter student number, name, surname, and delivery date.
    Information added to taken_books.txt.


•Menu 6: Take

    To take a book, enter "take."
    Enter the book to take ("takenn_book").
    Enter student number.
    Updates books.txt (T to F).
    Information added to taken_books.txt.

Menu 7: List

    To list information, enter "list."
    Submenus:
        "books": Print all data in books.txt.
        "students": Print all data in students.txt.
        "takens": Print data in taken_books.txt.

•Menu 8: Quit

    To exit the code sequence, enter "quit."
    Stops all loops and exits the program.
    This text reflects the structure and functionalities of your described 
    Python project. You can use this as a reference when implementing your 
    code.
