print('Welcome to the library! ')


while 1:
    todo = input("Library Management System Menu\n"
    "---------------\n"    
    "->Add          \n"
    "->Find         \n"
    "->Take         \n"
    "->Give         \n"
    "->Delete       \n"
    "->Register     \n"
    "->List         \n"
    "->Quit         \n"
    "---------------\n"
    "*-").lower()


    if todo == 'add':
        print('*--Add ')
        while True: 
            isbn_number = input("Enter ISBN number: ").lower()
            book_name = input("Enter Book name: ").lower()
            author = input("Enter the author's name: ").lower()
            
            files_name = "books.txt"
            
            with open(files_name, 'a') as file:
                file.write(f"{isbn_number},{book_name},{author},T\n")

                add_or_not = input('cont/q > ').lower()
            
            if add_or_not== 'cont':
                continue
            elif add_or_not== 'q':
                break
            else:
                print("You must writing cont or q")
                break
        print(f"Informaions added to file {files_name}.")
    
    elif todo == 'register':
        print('*--Register ')
        while True:
            files_name = "students.txt"

            student_name = input("Enter student's name: ").lower()
            student_surname = input("Enter student's surname: ").lower()
            student_id = input("Enter student's ID: ").lower()

            with open(files_name, 'a') as file:
                file.write(f"{student_name},{student_surname},{student_id}\n")

                add_or_not = input('cont/q > ').lower() 

            if add_or_not== 'cont':
                continue
            elif add_or_not== 'q':
                break
            else:
                print("You must writing cont or q")
                break
        print(f"Student information added to file {files_name}.")

    elif todo == 'delete':
        print('*--Delete\n  *--Book\n  *--Student')

        book_or_student = input('Which one do you want to delete Book/Student').lower()

        if book_or_student == 'book':
            print('  *--Delete Book')        
            files_name = "books.txt"

            try:
                with open(files_name, 'r') as file:
                    lines = file.readlines()

                delete_book = input("Which book do you want to delete? Enter the ISBN number or Book's Name: ").lower()

                with open(files_name, 'w') as file:
                    for line in lines:
                        if delete_book in line:
                            continue
                        file.write(line)

                print(f"The book with ISBN {delete_book} has been deleted.")

            except FileNotFoundError:
                print(f"{files_name} file not found.")
            except Exception as hata:
                print(f"Something went wrong: {hata}")

        elif book_or_student == 'student':
            print('  *--Delete Student')        
            files_name = "students.txt"

            try:
                with open(files_name, 'r') as file:
                    lines = file.readlines()

                delete_student = input("Which student do you want to delete? Enter the Student's ID or Student Surname: ").lower()

                with open(files_name, 'w') as file:
                    for line in lines:
                        if delete_student in line:
                            continue
                        file.write(line)

                print(f"The student with ID {delete_student} has been deleted.")

            except FileNotFoundError:
                print(f"{files_name} file not found.")
            except Exception as hata:
                print(f"Something went wrong: {hata}")

    
    elif todo == 'find':
        print('  *--Books\n  *--Students\n  *--Taken\n')
        user_wanttt=input('   -').lower()
        
        
        if user_wanttt == 'books':
            print('*--books ')
            files_name = "books.txt"


            try:
                with open(files_name, 'r') as file:
                    lines = file.readlines()
                    
                    found_info = input("Enter ISBN number or Book's: ").lower()

                    print('\n')
                    print('-'*100)

                    for line in lines:
                        if found_info in line.lower():
                            print(line.strip())
                    
                    print('-'*100)
                    print('\n')
                
            except FileNotFoundError:
                print(f"{files_name} file not founded.")
            except Exception as hata:
                print(f"Something went wrong: {hata}")


        elif user_wanttt == 'students':

            print('*--students ')
            files_name = "students.txt"


            try:
                with open(files_name, 'r') as file:
                    lines = file.readlines()
                    
                    found_info = input("Enter Students ID or Students name: ").lower()

                    print('\n')
                    print('-'*100)


                    for line in lines:
                        if found_info in line.lower():
                            print(line.strip())

                    print('-'*100)
                    print('\n')

            except FileNotFoundError:
                print(f"{files_name} file not founded.")
            except Exception as hata:
                print(f"Something went wrong: {hata}")

        elif user_wanttt == 'taken':
            print('*--taken ')
            files_name = "taken_books.txt"

            try:
                with open(files_name, 'r') as file:
                    lines = file.readlines()

                    found_info = input("Enter ISBN number or Books name or Student's ID: ").lower()

                    print('\n')
                    print('-'*100)

                    for i, line in enumerate(lines):
                        if found_info in line.lower():
                            print(line.strip())


                            if i < len(lines) - 1:
                                print(lines[i + 1].strip())

                    print('-'*100)
                    print('\n')

            except FileNotFoundError:
                print(f"{files_name} not founded.")
            except Exception as hata:
                print(f"Something went wrong: {hata}")

        else:
            print('Invalid command!')

    elif todo == 'give':
        print('*--Give ')
        files_name_books = "books.txt"
        taken_files_name = "taken_books.txt"

        try:
            with open(files_name_books, 'r') as file:
                lines = file.readlines()

            takenn_book = input("Which book do you want to give? Enter the ISBN number: ").lower()


            is_checked_out = any(takenn_book in line and 'F' not in line for line in lines)

            if is_checked_out:
                print("Warning: The book is checked out. You can't delete a checked-out book.")
            else:
                with open(files_name_books, 'w') as file:
                    for line in lines:
                        if takenn_book in line:
                            file.write(line.replace('F', 'T'))
                        else:
                            file.write(line)

                with open(taken_files_name, 'a') as taken_file:
                    
                    info_number = input("What is your students number: ").lower()
                    info_name = input("What is your name: ").lower()
                    info_surname = input("What is students surname: ").lower()
                    
                    datee = input("What is the release date of the book:  ").lower()
                    
                    taken_file.write(f"{takenn_book} was delievered by {info_name},{info_surname},{info_number} on {datee} \n")

                print(f"{takenn_book} has been given.")

        except FileNotFoundError:
            print(f"{files_name_books} file not founded.")
        except Exception as hata:
            print(f"Something went wrong: {hata}")

    
    elif todo == 'take':
        print('*--Take ')
        files_name_books = "books.txt"
        files_name_students = "students.txt"
        files_name_taken_books = "taken_books.txt"

        try:
            with open(files_name_books, 'r') as book_file:
                book_lines = book_file.readlines()

            takenn_book = input("Which book do you want to take? Enter the ISBN number: ").lower()
            student_id = input("Enter student's ID: ").lower()
            
            with open(files_name_students, 'r') as student_file:
                students_lines = student_file.readlines()
                student_info = [line.strip().split(',') for line in students_lines if student_id in line]

                if not student_info:
                    print(f"Student with ID {student_id} not found.")
                    continue

                student_name, student_surname, _ = student_info[0]

            with open(files_name_books, 'w') as book_file, open(files_name_taken_books, 'a') as taken_file:
                for line in book_lines:
                    if takenn_book in line:
                        taken_file.write(f"{student_id},{student_name},{student_surname}\n{takenn_book}\n")
                        book_file.write(line.replace('T', 'F'))
                    
                    else:
                        book_file.write(line)

            print(f"The book with ISBN {takenn_book} has been taken by the student with ID {student_id}.")

        except FileNotFoundError:
            print(f"One of the files ({files_name_books}, {files_name_students}, {files_name_taken_books}) not found.")
        except Exception as hata:
            print(f"An error occurred: {hata}")
    
    elif todo == 'list':
        print('  *--Books\n  *--Students\n  *--Takens')
        user_want = input('   -').lower()
        
        if user_want == 'books':
            files_name = "books.txt"


            try:
                with open(files_name, 'r') as file:
                    lines = file.readlines()
                
                print('\n')
                print('-'*100)
                
                for line in lines:
                    print(line.strip())
                
                print('-'*100,'\n')
            
            except FileNotFoundError:
                print(f"{files_name}file not founded.")
            except Exception as hata:
                print(f"Something went wrong: {hata}")
        elif user_want == "students":
            files_name = "students.txt"
            try:
                with open(files_name, 'r') as file:
                    lines = file.readlines()
                
                print('\n')
                print('-'*100)

                for line in lines:
                    print(line.strip())

                print('-'*100,'\n')

            except FileNotFoundError:
                print(f"{files_name} has been not founded.")
            except Exception as hata:
                print(f"Something went wrong: {hata}")



        elif user_want == 'takens':
            files_name = 'taken_books.txt'

            try:
                with open(files_name, 'r') as file:
                    lines = file.readlines()

                print('\n')
                print('-'*100)

                for line in lines:
                    print(line.strip())
                
                print('-'*100,'\n')


            except FileNotFoundError:
                print(f"Something went wrong: {hata}")
            except Exception as hata:
                print(f"Something went wrong: {hata}")
            


    elif todo == 'quit':
        print('See u!')
        break


    else:
        print("Invalid command. Please enter add/find/take/quit.")