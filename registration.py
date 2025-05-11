
from file_manager import write_to_file, read_file, generate_id
from utils import word_alpha, check_password


def register_user():
    filename = "data/users.csv"
    print("""
                W E L C O M E !!!
                """)

    while True:
        email = input("Enter your email: ")
        word = word_alpha(word=email)
        if word:
            if len(email[0:len(email)-10]) >= 5:
                break
            else:
                print("Email length is less than 5 characters.")
        else:
            print("Email Error.")
    read_user = read_file(filename=filename)
    for user in read_user:
        if email in user:
            print("You have already registered.")
            return
        continue


    while True:
        password = input("Create a new password: ")
        password1 = input("Enter again password: ")
        passw = check_password(passw=password)
        if passw:
            if len(password) >= 8:
                if password == password1:
                    print("""
                    Congratulations, you have successfully registered.
                            """)
                    break
                else:
                    print("Parol bir biriga mos emas.")
                    continue
            else:
                print("""           
                Password length is less than 8 characters
                """)
                continue
        else:
            print("""Password error.""")

    user_id = generate_id(filename=filename)
    user_info = [user_id, email, password]
    write_to_file(filename=filename, data=user_info, mode='a')


def register_teacher():
    filename = "data/teachers.csv"
    print("""
                W E L C O M E !!!
                """)

    while True:
        email = input("Enter your email: ")
        word = word_alpha(word=email)
        if word:
            if len(email[0:len(email)-10]) >= 5:
                break
            else:
                print("Email length is less than 5 characters.")
        else:
            print("Email Error.")
    read_teacher = read_file(filename=filename)
    for teacher in read_teacher:
        if email in teacher:
            print("You have already registered.")
            return
        continue


    while True:
        password = input("Create a new password: ")
        password1 = input("Enter again password: ")
        passw = check_password(passw=password)
        if passw:
            if len(password) >= 8:
                if password == password1:
                    print("""
                    Congratulations, you have successfully registered.
                            """)
                    break
                else:
                    print("Parol bir biriga mos emas.")
                    continue
            else:
                print("""           
                Password length is less than 8 characters
                """)
                continue
        else:
            print("""Password error.""")

    user_id = generate_id(filename=filename)
    user_info = [user_id, email, password]
    write_to_file(filename=filename, data=user_info, mode='a')


