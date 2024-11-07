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


•Menu 3: Delete

    To delete a book, enter "delete."
    Enter ISBN number or book name to remove from books.txt.


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






Scroll down for more details. I tried to express it as clearly as possible. :)







•There are 8 main menus in my project_library.py code. 
Some of these menus have submenus.


1•My first menu element is add: If your first input is add, 
the first question you will be asked will be the isbn_number of the book, 
then the book_name will be asked, and then the author will be asked. 
If you enter these inputs correctly, ISBN_number, Book_name, Author, T 
will be added to the content of the books.txt file. When a book is added
with Add, T will automatically be written in the control content.
If you want to continue adding books, you need to type cont.
If you say no, you want to exit this menu, just type q. 
Typing q will direct you to the upper menu.


2•My second menu element is register: If you enter register as input,
the first question asked will be student_name, then student_surname 
will be asked and finally student_id will be asked. 
When you enter this information, all this information will be added to 
the students.txt file and it will be added in this file in the following 
order: student_name, student_surname, student_id. 


3•The third menu element is delete: If you enter the delete input, 
the menu will receive a delete_book input from you, and if you write the 
ISBN number or the name of the book here, it will remove that book 
from the books.txt file.


4•The fourth menu element is find: If you type find as input,you will 
enter the find menu. 
There are 3 submenus here:

         •If you enter the books input, you can search in the books.txt file, 
    by ISBN number, by the name of the book, or by the name of the author,
    and find what you are looking for here.

         •If you enter the students input, you can search by student 
    number or student name and surname in the students.txt file and 
    find what you are looking for here.

         •If you enter the taken input, if you enter the student's name 
    or number in the taken_books.txt file, you can see the books that 
    student took and, if so, the date of delivery.


5•Fifth menu element: give: To enter the give menu, simply type give.
Then, the first question you will be asked is takenn_book. Here you 
need to enter the book you want to give. Afterwards, it automatically 
checks the books.txt file here. It says T or F at the end of the book. 
T here indicates that the book is in the library. If it says F, 
it shows that the book is not in the library. The important thing here 
is that if the book is F, that is, if the book is not in the library, 
this give process continues to occur, but If T is here, even if you 
continue the transaction, no further transaction will be completed 
because a book in the library cannot be returned anyway. 
After this situation is checked, the info_number (student number) of the
person who delivered the book is asked, then info_name (student name) is 
asked, and then info_surname (student surname) is asked and the delivery 
date datee (input is asked). And the information here is written to 
taken_books.txt as {book name} was delivered by {name},{surname},{number} on {datee}.
And of course, if the book is in the library, it gives an error when you 
want to return it. And of course, the text F turns into T in books.txt


6•The sixth menu element is take: when you type take, you enter the take 
menu, then you enter which book you want to buy in the takenn_book input.
Afterwards, you must write the student number in the student_id input.
During this process, T turns into F in the books.txt file,and the student
number,student name,student surname are printed in the taken_books.txt 
file, respectively, and the book name is written on the line below it.


7•When you type list:list for the seventh menu element, you will be greeted with 3 submenus.
        •If you type books, it will print all the data in books.txt, 
    which contains the book information, as it is. This process also allows
    you to check whether a book is T F or not. (If you want to check a 
    single book, you need to follow the find-books process order.)
        •If you type students, it prints all the data in students.txt, 
    which contains student information.
        •If you type takens, it prints the data in the taken_books.txt
        file containing the books taken.


8•Quit, which is the last menu element and also the last command that 
will allow you to exit this code sequence: if you type quit, all these 
loops will be stopped and the code sequence will be exited.