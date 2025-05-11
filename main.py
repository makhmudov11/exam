

from registration import register_user, register_teacher
from utils import check_user_and_teacher
from glob import update_password, return_id
from students import course_purchase, purchased_courses, send_message_teacher
from teachers import create_course, course_members, change_price_course


def  main():
    print("""
    1.Register user
    2.Register teacher
    3.Sign in
    4.Logout
    """)
    choice = input("Enter your choice: ")

    if choice == '1':
        register_user()
    elif choice == '2':
        register_teacher()
    elif choice == '3':
        sign_in()
        return
    elif choice == '4':
        print("Good bye:)")
        return
    else:
        print("Invalid choice.")
    main()


def sign_in():
    print("""
    Login sahifasi: 
    """)
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    name = check_user_and_teacher(email=email, passw=password)
    if name is None:
        print("Siz avval ro'yhatdan otishingiz kerak")
        return main()
    if name == "USER":
        student_menu(email=email)
    elif name == "TEACHER":
        teacher_menu(email=email)
    else:
        print("""
    Parolingizni unutdingizmi?
                    1. Ha
                    2. Yo'q
            """)
        while True:
            choicee = input("Enter your choice: ")
            if choicee == '1':
                update_password(gmail=email)
                sign_in()
                break
            elif choicee == '2':
                sign_in()
                break
            else:
                print("Invalid choice.")
    return


def student_menu(email: str):
    print("""
    O'quvchi oynasi:
        1. Kurs sotib olish
        2. Sotib olingan kurslar royhatini korish
        3. Kurs oqituvchisiga habar yuborish
        4. Logout
        """)

    choice = input("Enter your choice: ")

    if choice == '1':
        course_purchase(email=email)
    elif choice == '2':
        print(purchased_courses(email=email))
    elif choice == '3':
       print(send_message_teacher(email=email))
    elif choice == '4':
        print("Good bye student:)")
        return
    else:
        print("Invalid choice.")
    student_menu(email=email)




def teacher_menu(email: str):
    print("""
O'qituvchi oynasiga xush kelibsiz: 
    1. Kurs yaratish
    2. Kurslarni sotib olganlarni korish
    3. Kurslarni narxini ozgartish
    4. Oquvchidan kelgan habarlarni korish    
    5. Logout
    """)
    choice = input("Enter your choice: ")
    teacher_id = return_id(gmail=email, filename="data/teachers.csv")
    if choice == '1':
        print(create_course(teacher_id=teacher_id))
    elif choice == '2':
        res = course_members(teacher_id=teacher_id)
        if res is False:
            print("Kurs topilmadi.")
        elif res == 0:
            print("Kursga hali hec kim qoshilmagan")
        else:
            print(f"Jami oquvchilar ro'yhati: {res}")
    elif choice == '3':
        res = change_price_course(teacher_id=teacher_id)
        if res:
            print("Kurs narxi muvaffaqiyatli ozgartirildi.")
        else:
            print("Kurs haqida ma'lumot topilmadi.")
    elif choice == '4':
        pass
    elif choice == '5':
        print("Good bye teacher:)")
        return
    else:
        print("Invalid choice.")
    teacher_menu(email=email)

if __name__ == '__main__':
    main()