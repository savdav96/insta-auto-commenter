from InstagramAPI import InstagramAPI

def getTotalFollowers(api, user_id):
    followers = []

    next_max_id = True

    while next_max_id:

        if next_max_id is True:
            next_max_id = ''

        api.getUserFollowers(user_id, maxid=next_max_id)

        followers.extend(api.LastJson.get('users', []))

        next_max_id = api.LastJson.get('next_max_id', '')

    return followers

def get_users(followers):
    cleaned = []
    i = 0
    while i<len(followers):
        item = followers[i]["username"]
        cleaned.append(item)
        i = i+1
    return cleaned

if __name__ == "__main__":

    api = InstagramAPI("savoebbasta", "Ignazio96")
    api.login()

    user_id = api.username_id

    followers = getTotalFollowers(api, user_id)
    cleaned = get_users(followers)

    print('Number of followers:', len(followers))
    print(cleaned)

