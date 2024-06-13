import http.client as hc, urllib.parse as up

username_file = open("nomi_utenti.txt")
password_file = open("password.txt")

user_list = username_file.readlines()
pwd_list = password_file.readlines()

for user in user_list:
    for pwd in pwd_list:
        print(f"{user} - {pwd}")