import time
from src.client import API, get_media_id


# define the function blocks
def none(arg1=None, arg2=None):
    print("[INFO] None operation performed")


def wait(seconds, arg1=None):
    print("[INFO] Waiting for " + str(seconds) + " seconds")
    time.sleep(seconds)


def comment(url_idx, str_idx):
    url_idx = url_idx % len(urls)
    str_idx = str_idx % len(strs)
    media_id = get_media_id(urls[url_idx])
    API.comment(media_id, strs[str_idx])
    print("[INFO] commented " + strs[str_idx] + " on " + urls[url_idx])


def like(url_idx, arg1=None):
    url_idx = url_idx % len(urls)
    media_id = get_media_id(urls[url_idx])
    API.like(media_id)
    print("[INFO] liked " + urls[url_idx])


def feed(arg1=None):
    API.getPopularFeed()
    print("[INFO] getting feed")


actions = {0: none,
           1: wait,
           2: wait,
           3: wait,
           4: comment,
           5: like,
           6: feed}


def run(action_number, *args):
    print("[INFO] AntiAntiSpam Enabled")
    actions[action_number](*args)


# Test
if __name__ == "__main__":
    run(2, "id", "ciao")


urls = ("https://www.instagram.com/p/BpEs3H3BfUn/",
        "https://www.instagram.com/p/BpDXZgclLFm/",
        "https://www.instagram.com/p/BpACo2WC4hB/",
        "https://www.instagram.com/p/BpBdjrnifA2/",
        "https://www.instagram.com/p/Bo_nFBniO70/",
        "https://www.instagram.com/p/BpDKY1yD08q/",
        "https://www.instagram.com/p/BpA_wgNnqRQ/",
        "https://www.instagram.com/p/Bo989LsBp5F/",
        "https://www.instagram.com/p/BpDYORwAM0F/",
        "https://www.instagram.com/p/BpFdfmBjlqH/",
        "https://www.instagram.com/p/BpFDg56D-eH/")

strs = ("Nice!",
        "Awesome",
        "itz Good!",
        "jhahahah",
        "aaghahah",
        "...",
        "@santoquelo",
        "nicezz",
        "likeit",
        "I loveit!",
        "yyeeah!")
