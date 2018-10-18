from InstagramAPI import InstagramAPI
import requests

API = InstagramAPI("savoebbasta", "Ignazio96")
API.login()
status = API.LastResponse.status_code

if status == 200:
    print("[INFO] Successfully logg'd in")
else:
    print("[ERROR]" + str(status))
    exit(-1)


def get_media_id(url):
    req = requests.get('https://api.instagram.com/oembed/?url={}'.format(url))
    return req.json()['media_id']
