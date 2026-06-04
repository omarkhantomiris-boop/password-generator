import random
import string

def generate_password(length):
    c = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(c) for _ in range(length))

length = int(input("Пароль ұзындығын енгізіңіз: "))

if length < 8:
    print("Пароль ұзындығы кемінде 8 болуы керек!")
else:
    print("Пароль:", generate_password(length))