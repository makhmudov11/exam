from file_manager import generate_id, read_file, write_to_file
from glob import return_id, send_email
from payment import payment_user
from datetime import datetime

def course_purchase(email: str):
    print("Kurs sotib olish sahifasi:\n")

    user_id = return_id(gmail=email, filename="data/users.csv")
    new_id = generate_id(filename="data/attend_courses.csv")
    name = input("Ismingizni kiriting: ")
    surname = input("Familiyangizni kiriting: ")

    courses = read_file(filename="data/created_courses.csv")
    if not courses:
        print(" Hozircha kurslar mavjud emas.")
        return

    print("Mavjud kurslar:")
    for index, course in enumerate(courses, start=1):
        print(f"{index}. {course[5].title()}")

    course_name = input("Qaysi kursni tanlaysiz?: ")
    pay_data = read_file(filename="data/attend_courses.csv")
    for user in pay_data[::-1]:
        if user_id == user[1] and user[5].lower() == course_name.lower():
            print(f"Siz {course_name.title()} kursiga  qoshilgansiz.")
            return
    for res in courses:
        if course_name == res[5]:
            print(""" Kursga qo‘shilish uchun to‘lov qilishingiz kerak.""")
            if payment_user(user_id=user_id, course_name=course_name):
                teacher_data = read_file(filename="data/created_courses.csv")
                teacher_id = None
                for teacher in teacher_data[::-1]:
                    if teacher[5] == course_name:
                        teacher_id = teacher[0]
                        break
                sana = datetime.now()
                data = [new_id, user_id, name, surname,sana, course_name,teacher_id]
                write_to_file(filename="data/attend_courses.csv", data=data, mode='a')
                print("Siz kursga muvaffaqiyatli qo‘shildingiz!")
            else:
                print("To‘lov amalga oshmadi.")
                print("Kamida 50 foiz tolov qilish kerak")
            break
    else:
        print("Bunday kurs topilmadi.")
    return


def purchased_courses(email: str):
    user_data = read_file(filename="data/users.csv")
    user_id = None
    for user in user_data:
        if email in user:
            user_id = user[0]
            break
    if user_id is None:
        return "Siz avval royhatdan otishingiz kerak."

    index = 1
    courses = read_file(filename="data/attend_courses.csv")
    for course in courses:
        if course[1] == user_id:
            print(f"{index}. Kurs nomi: {course[5].title()}")
            index += 1

    if index == 1:
        return "Siz bironta ham  kursga qoshilmagansiz."
    return True


def send_message_teacher(email: str):
    result = purchased_courses(email=email)
    if isinstance(result, str):
        print(result)
        return result

    course_name = input("Qaysi kurs o‘qituvchisiga yuborish kerak: ").strip().lower()
    course_data = read_file(filename="data/created_courses.csv")
    teacher_id = None
    for data in course_data[::-1]:
        if course_name.lower() in data:
            teacher_id = data[1]
            break


    if teacher_id is None:
        return "Siz kiritgan kurs bo‘yicha ma'lumot topilmadi."

    teacher_data = read_file(filename="data/teachers.csv")
    teacher_email = None
    for teacher in teacher_data:
        if teacher[0] == teacher_id:
            teacher_email = teacher[1]
            break

    if teacher_email is None:
        return "Siz kiritgan kurs boyicha azolik topilmadi."
    message = input("Xabar kiriting: ")
    send_email(receiver_email=teacher_email, message=message)
    return "Xabar yuborildi"
