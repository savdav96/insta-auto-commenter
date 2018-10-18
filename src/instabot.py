from random import randint
from src.connection import API, get_media_id
from src.antiantispam import run


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

    print("[INFO] Collected " + str(len(followers)) + " usernames")
    return followers


def mass_comment(followers, api, media_id):
    
    composite_list = [followers[x:x + 3] for x in range(0, len(followers), 3)]
    count = 0

    for group in composite_list:

        comment = "@" + group[0] + " " + "@" + group[1] + " " + "@" + group[2]

        api.comment(media_id, comment)
        status = api.LastResponse.status_code

        if status != 200:
            print("[ERROR]" + str(status))
            run(1, randint(3600, 5400))
        else:
            print("[INFO] Done: " + comment)
            count = count + 1
            if count > randint(13, 16):
                print("[WARNING] Over 13 to 16 comments")
                run(randint(0, 9), randint(3600, 5400), randint(3600, 5400))
                count = 0
            else:
                run(randint(0, 1), randint(100, 200))
    print("[INFO] Success!")


if __name__ == "__main__":

    friends = get_usernames(API, API.username_id)
    friends.remove("schiavo.bancomat")
    mass_comment(friends, API, get_media_id("https://www.instagram.com/p/BpFJRcuCoux/"))

