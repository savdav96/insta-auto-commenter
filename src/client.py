from InstagramAPI import InstagramAPI
import requests

print("[INFO] Welcome to Instagram Auto Commenter")
user = input("Username: ")
while True:
    pwd = input("Password: ")
    API = InstagramAPI(user, pwd)
    API.login()
    status = API.LastResponse.status_code

    if status == 200:
        print("[INFO] Successfully logg'd in")
        break
    elif API.LastJson['invalid_credentials'] is True:
        print("[ERROR] Incorrect password ")
    else:
        print("[ERROR] " + str(status) + ", exiting...")
        exit(-1)


def get_media_id(url):
    url = "https://www.instagram.com/p/"+url
    req = requests.get('https://api.instagram.com/oembed/?url={}'.format(url))
    return req.json()['media_id']
