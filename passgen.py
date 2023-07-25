import secrets
import string
def passgen(length):
    password=""
    for i in range(length):
        letter=secrets.choice(string.ascii_letters)
        digit=secrets.choice(string.digits)
        punctuation=secrets.choice(string.punctuation)
        password += letter + digit + punctuation
        if len(password)>length:
            break
    return password

length=10

print(passgen(length))
print ("Successfully generated a password of"+ str(length) + "characters long")