import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from file_manager import read_file, write_to_file


def send_email(receiver_email: str, message: str = None):

    sender_email = "samandarmakhmudjanov14@gmail.com"
    password = "htfo sbuk pcqm qvbn" # send gmaildagi pochta app passwordi

    user_info = read_file(filename="data/users.csv")
    teacher_info = read_file(filename="data/teachers.csv")

    found = any(receiver_email in user for user in user_info + teacher_info)
    if not found:
        print("Malumot topilmadi")
        return None
    code = 0
    if message is None:
        code = random.randint(100000,999999)
        subject = "Tasdiqlash kodingiz"
        body = f"""
            Sizning tasdiqlash kodingiz: {code}
        """
    else:
        subject = "Training Center"
        body = message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
            print("Email sent successfully!")
            if message is None:
                return code
            return False
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
        return None

def update_password(gmail: str):
    code = send_email(receiver_email=gmail)
    if code is None:
        print(" Ma'lumot topilmadi.")
        return

    print("Gmailingizga kod yuborildi.")
    send_code = input("Kodni kiriting: ")

    if str(code) != send_code:
        print("Noto‘g‘ri kod!")
        return

    while True:
        password = input("Create a new password: ")
        password1 = input("Enter again password: ")
        if password == password1:
            break
        else:
            print("Parollar mos emas. Qaytadan kiriting.")

    updated = False

    user_info = read_file("data/users.csv")
    for user in user_info:
        if user[1] == gmail:
            user[-1] = password
            write_to_file("data/users.csv", user_info)
            updated = True
            break

    if not updated:
        teacher_info = read_file("data/teachers.csv")
        for user in teacher_info:
            if user[1] == gmail:
                user[-1] = password
                write_to_file("data/teachers.csv", teacher_info)
                updated = True
                break

    if updated:
        print("Parol muvaffaqiyatli yangilandi!")
    else:
        print("Bunday foydalanuvchi topilmadi.")
    return


def return_id(gmail: str, filename: str):
    read_data = read_file(filename=filename)
    user_id = ""
    for user in read_data:
        if gmail in user:
            user_id = user[0]
            return user_id
    return None
