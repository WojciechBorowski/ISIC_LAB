import random
import string

def gen_passwd(length = 6):
    char = string.ascii_letters + string.digits
    return ''.join(random.choice(char) for _ in range(length))

def save_passwd(num, file):
    f = open(file, 'w')
    for _ in range(num):
        password = gen_passwd()
        f.write(password + "\n")


passwd_num = 1000
file = 'passwords.txt'
save_passwd(passwd_num, file)