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


def comment_by_tag(followers, api, media_id):
    
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


def comment_by_word(word, api, media_id):

    max_comments = 400
    count = 0

    while count < max_comments:
        if count % 40 == 0 and count != 0:
            print("[INFO] No. of comments reached: " + str(count))
            run(1, randint(3600, 4500))

        for letter in word:

            api.comment(media_id, letter)
            status = api.LastResponse.status_code

            if status != 200:
                print("[ERROR] " + str(status))
                run(1, randint(100, 200))

            else:
                count = count + 1
                print("[INFO] Commented: '" + letter + "' [" + str(count) + " of " + str(max_comments) + "]")
                run(1, randint(4, 10))

        run(1, randint(10, 20))

    print("[INFO] Reached " + str(max_comments) + " daily comments.")


if __name__ == "__main__":

    option = input("Welcome to Instagram mass commenter:\n"
                    "Choose option:\n"
                    "[1] For commenting by tagged followers\n"
                    "[2] For commenting by prompted word\n")

    if option == 1 :

        friends = get_usernames(API, API.username_id)
        link = input("Paste instagram link post\n")
        comment_by_tag(friends, API, get_media_id(link))

    else:
        link = input("Paste instagram link post\n")
        word = input("Type the comment\n")
        comment_by_word(word, API, get_media_id(link))


