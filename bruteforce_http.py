import http.client as hc, urllib.parse as up

username_file = open("nomi_utenti.txt")
password_file = open("password.txt")

user_list = username_file.readlines()
pwd_list = password_file.readlines()

for user in user_list:
    user =  user.rstrip()
    for pwd in pwd_list:
        pwd = pwd.rstrip()
        print(f"{user} - {pwd}")

        