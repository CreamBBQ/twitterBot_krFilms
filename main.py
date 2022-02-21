import tweepy
import credentials


def get_client():
    client = tweepy.Client(
    bearer_token=credentials.bearer,
    consumer_key=credentials.key,
    consumer_secret=credentials.key_secret,
    access_token=credentials.token,
    access_token_secret=credentials.token_secret)
    return client


def get_user_info():
    client = get_client()
    user = client.get_user(username="CreamBBQ")
    return user.data.name



client = get_client()
client.create_tweet(text = 'Hola mundo')



