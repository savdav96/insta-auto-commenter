from InstagramAPI import InstagramAPI
import re, time, requests


friends = []
i = 0
f = open("f.txt", "r", encoding="utf-8")

lines = f.readlines()

for line in lines:
    if i % 4 == 0:
        if not re.match(r'\w*Verificato', line):
            line = line.rstrip("\n")
            friends.append(line)
    i += 1

friends[0] = "arancicarini"
composite_list = [friends[x:x+3] for x in range(0, len(friends),3)]
print(composite_list)

API = InstagramAPI("savoebbasta", "")
API.login()


def get_media_id(url):

    req = requests.get('https://api.instagram.com/oembed/?url={}'.format(url))
    return req.json()['media_id']


media_id = get_media_id("https://www.instagram.com/p/BmN5eBWlfum/?utm_source=ig_share_sheet&igshid=1cp7rvqw7jnnh")

count = 0
for item in composite_list:

    comment = "@"+item[0] + " " + "@"+item[1] + " " + "@"+item[2]

    API.comment(media_id, comment)
    status = API.LastResponse.status_code

    if status != 200:
        print(status)
        time.sleep(3600)
    else:
        print("Done: " + comment)
        count = count + 1
        if count == 15:
            time.sleep(3600)
            count = 0
        else:
            time.sleep(15)

print("Success!")
