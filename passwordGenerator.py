import random

def main():
    setOfCharacters = "abcdefijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%!()&"
    passwordLength = 8
    password = "".join(random.sample(setOfCharacters,passwordLength))
    print(password)

if __name__ == "__main__":
    print("Here is your password!!")
    main()
