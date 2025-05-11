from file_manager import generate_id, write_to_file, read_file
from datetime import datetime

def create_course(teacher_id: str):
    print("Kurs yaratish.")

    gen_id = generate_id(filename="data/created_courses.csv")
    name = input("Ismingizni kiriting: ")
    surname = input("Familyanigzni kiriting: ")
    sana = datetime.now()
    course_name = input("Kurs nomini kiriting: ")
    price = input("Kurs narxini kiriting: ")
    data = [gen_id,teacher_id,name,surname,sana,course_name,price]
    write_to_file(filename="data/created_courses.csv", data=data, mode='a')
    return f"{course_name.title()} kursi muvaffaqiyatli yaratildi."

def course_members(teacher_id: str):
    print("Siz yaratgan kurslar royhati: \n")
    courses = read_file(filename="data/created_courses.csv")
    result = []
    index = 1
    for course in courses:
        if course[1] == teacher_id:
            print(f"{index}. Kurs nomi: {course[5].title()}, Narxi: {course[6]}")
            index += 1
            result.append(course[5].lower())
    course_name = input("Qaysi kurs oquvchilar royhati kerak: ")
    if course_name.lower() not in result:
        return False
    student_data = read_file(filename="data/attend_courses.csv")
    teacher_data = read_file(filename="data/created_courses.csv")
    counter = 0
    for student in student_data:
        if student[5].lower() == course_name.lower():
            for teacher in teacher_data:
                if teacher[0] == student[6]:
                    counter += 1
                    print(f"{counter}. Ismi: {student[2].capitalize()}, Familiyasi: {student[3].capitalize()}")
                    break
    return counter



def change_price_course(teacher_id: str):
    courses_data = read_file(filename="data/created_courses.csv")
    counter = 0
    result = list()
    print("Siz yaratgan kurslar: \n")
    for course in courses_data:
        if course[1] == teacher_id:
            counter += 1
            print(f"{counter}.{course[5].capitalize()}")
            result.append(course[5].lower())
    if counter != 0:
        course_name = input("Qaysi kursni narxini ochirish kerak: ")
        if course_name.lower() in result:
            for arg in courses_data:
                if arg[1] == teacher_id and course_name.lower() == arg[5].lower():
                    price = arg[6]
                    print(f"{course_name.title()} kurs narxi {price} so'm.")
                    change_price = input("Nech pulga o'zgartirish kerak: ")
                    arg[6] = change_price
                    write_to_file(filename="data/created_courses.csv", data=courses_data)
                    return True
    return False










