from InstagramAPI import InstagramAPI
import time, requests, random


def get_usernames(api, user_id):

    followers = []

    next_max_id = True

    while next_max_id:

        if next_max_id is True:
            next_max_id = ''

        api.getUserFollowers(user_id, maxid=next_max_id)

        cleared = [user['username'] for user in api.LastJson.get('users', []) if not user['is_verified']]
        followers.extend(cleared)
        next_max_id = api.LastJson.get('next_max_id', '')

    return followers


def get_media_id(url):
    req = requests.get('https://api.instagram.com/oembed/?url={}'.format(url))
    return req.json()['media_id']


def mass_comment(followers, api, media_id):
    
    composite_list = [followers[x:x + 3] for x in range(0, len(followers), 3)]
    count = 0

    for group in composite_list:

        comment = "@" + group[0] + " " + "@" + group[1] + " " + "@" + group[2]

        api.comment(media_id, comment)
        status = api.LastResponse.status_code

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


if __name__ == "__main__":

    API = InstagramAPI("savoebbasta", "Ignazio96")
    API.login()

    friends = get_usernames(API, API.username_id)
    print(len(friends))
    #mass_comment(friends, API, get_media_id(""))  # TODO search url


    random.randint(3600, 7200)
