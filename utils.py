
from file_manager import read_file

def word_alpha(word: str):

    res = 0
    for i in word[0:len(word)-10]:
        if i.isalpha() and i.islower():
            res += 1
        elif i.isdigit():
            res += 1

    if res == len(word) - 10 and word.endswith("@gmail.com"):
        return True
    return False

def check_password(passw: str):
    res = 0

    for i in passw:
        if i.isalnum():
            res += 1

    return True if res == len(passw) else False

def check_user_and_teacher(email: str, passw: str):
    info = read_file(filename="data/users.csv")
    for user in info:
        if email in user and passw in user:
            return "USER"


    info1 = read_file(filename="data/teachers.csv")
    for teacher in info1:
        if email in teacher and passw in teacher:
            return "TEACHER"

    for user in info:
        if email in user and not passw in user:
            return "Parol xato"
    return None


# def check_data(email: str, passw: str, filename):
