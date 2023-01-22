import random
from instagrapi import Client
from instagrapi.exceptions import (
    BadPassword, ReloginAttemptExceeded, ChallengeRequired,
    SelectContactPointRecoveryForm, RecaptchaChallengeForm,
    FeedbackRequired, PleaseWaitFewMinutes, LoginRequired
)



print('''
 __  __           _        _            __     __                
|  \/  |         | |      | |           \ \   / /                
| \  / | __ _  __| | ___  | |__  _   _   \ \_/ /   _ _ __   ___  
| |\/| |/ _` |/ _` |/ _ \ | '_ \| | | |   \   / | | | '_ \ / _ \ 
| |  | | (_| | (_| |  __/ | |_) | |_| |    | || |_| | | | | (_) |
|_|  |_|\__,_|\__,_|\___| |_.__/ \__, |    |_| \__,_|_| |_|\___/ 
                                  __/ |    https://github.com/Yqno                      
                                 |___/                           
''')

username = input("Username: ")
password = input("Password: ")

client = Client()
#client.handle_exception = handle_exception
client.login(username, password)



hashtag = ("yourhashtaghere")
hashtags = random.choice(hashtag)
comments = ["Keep up the Great Work!", "Great post!", "Incredible!", "Masterpiece!", "Awesome!", "Beautiful Post!"]
medias = client.hashtag_medias_recent(hashtag, 60)
topmedias = client.hashtag_medias_top(hashtag, 5)




for i, media in enumerate(medias):
    client.media_like(media.id)
    print(f"Liked post Number {i+1} of hashtag {hashtag}")
    if i % 5 == 0:
        client.user_follow(media.user.pk)
        print(f"Followed user {media.user.username} ")
        comment = random.choice(comments)
        client.media_comment(media.id, comment)
        print(f"Commented {comment} under post number {i+1} ")

for i, topmedia in enumerate(topmedias):
    client.media_like(media.id)
    print(f"Liked post Number {i+1} of hashtag {hashtag}")        
    if i % 5 == 0:
        client.user_follow(media.user.pk)
        print(f"Followed user {media.user.username} ")
        comment = random.choice(comments)
        client.media_comment(media.id, comment)
        print(f"Commented {comment} under post number {i+1} ")
