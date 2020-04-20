import tweepy
import time

print('this is my twitter bot')

CONSUMER_KEY = 'gs4MwAboD5N19jCDLbfUtjmra'
CONSUMER_SECRET = 'KHApNxfWfH3CxeUlYzSx8QolRyLNXDo8NB1L6xuLl39i90vH8f'
ACCESS_KEY = '1143485395184885760-PaFEmF0Xk4r1TrRtQmFMoeQuoFvXBu'
ACCESS_SECRET = 'ps6C4jXxw8gKJM2WQFQCeI1US7KjB2Hgz6Rq7bnWHzR11'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'


def retrive_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id


def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


def replay_to_tweets():
    print("retrieving replaying to tweets...")
    last_seen_id = retrive_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')

    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#helloworld' in mention.full_text.lower():
            print('found #helloworld!')
            print('responding back...')
            api.update_status('@' + mention.user.screen_name + '#HelloWorld back to you!', mention.id)


while True:
    replay_to_tweets()
    time.sleep(15)
