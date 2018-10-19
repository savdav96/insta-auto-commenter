from random import randint
from src.client import API, get_media_id
from src.antiantispam import run


def get_usernames(api, user_id):

    followers = []

    next_max_id = True

    while next_max_id:

        if next_max_id is True:
            next_max_id = ''

        api.getUserFollowers(user_id, maxid=next_max_id)

        names = [user['username'] for user in api.LastJson.get('users', []) if not user['is_verified']]
        followers.extend(names)
        next_max_id = api.LastJson.get('next_max_id', '')

    print("[INFO] Collected " + str(len(followers)) + " usernames")
    return followers


def mass_comment(followers, api, media_id):
    
    grouped_list = [followers[x:x + 3] for x in range(0, len(followers), 3)]
    count = 0

    for index, group in enumerate(grouped_list, start=1):

        comment = "@" + group[0] + " " + "@" + group[1] + " " + "@" + group[2]

        api.comment(media_id, comment)
        status = api.LastResponse.status_code

        if status != 200:
            print("[ERROR]" + str(status))
            run(1, randint(3600, 5400))
        else:
            print("[INFO] Commented: '" + comment + "' [" + str(index) + " of " + str(len(grouped_list)) + "]")
            count = count + 1
            if count > randint(13, 16):
                print("[WARNING] Reached 13 up to 16 comments")
                run(randint(0, 6), randint(2700, 3600), randint())
                count = 0
            else:
                run(randint(0, 2), randint(100, 200))
    print("[INFO] Success!")


if __name__ == "__main__":

    friends = get_usernames(API, API.username_id)
    mass_comment(friends, API, get_media_id("https://www.instagram.com/p/BpFJRcuCoux/"))

