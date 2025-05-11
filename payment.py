
from datetime import datetime
from file_manager import read_file, write_to_file, generate_id


def payment_user(user_id: str, course_name: str):
    filename = "data/payment.csv"
    course_data = read_file(filename="data/created_courses.csv")
    course_price = ""
    for data in course_data[::-1]:
        if course_name in data:
            course_price = data[-1]
            break

    print(f"""
    Kurs Narxi: {course_price} so'm.
    """)

    paid = input("Qancha to'lov qilmoqchisiz(eng kamida 50%): ")
    if int(paid) >= int(course_price) / 2:
        data = [generate_id(filename=filename), user_id, datetime.now(), course_name, paid]
        write_to_file(filename=filename, data=data, mode='a')
        return True
    return False



    # payment_history = read_file(filename=filename)
    #
    # paid = input("Qa")
    # summa = 0
    # for user in payment_history:
    #     if user[1] == user_id:
    #         summa += int(user[1])
    #
