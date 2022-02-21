import tweepy
import credentials
import random
import pandas as pd


def get_tweet_string():
    movies_info = pd.read_csv(
        'https://raw.githubusercontent.com/CreamBBQ/webScraping_IDMb/master/korean_movies.csv')
    random_integer = random.randint(0, 922)
    random_movie = movies_info.iloc[[random_integer]]
    name = random_movie.iloc[0, 0]
    year = random_movie.iloc[0, 1]
    stars = random_movie.iloc[0, 2]
    abstract = random_movie.iloc[0, 3]
    string = f"{name} {year}\n⭐{stars}\n\n{abstract}"
    return string, random_integer


def get_client():
    client = tweepy.Client(
        bearer_token=credentials.bearer,
        consumer_key=credentials.key,
        consumer_secret=credentials.key_secret,
        access_token=credentials.token,
        access_token_secret=credentials.token_secret)
    return client


def tweet():
    client = get_client()
    movie_info, random_integer = get_tweet_string()
    if len(movie_info) < 281:
        client.create_tweet(text=movie_info)
    else:
        except_msg = f"@CreamBBQ La película ubicada en la fila {random_integer} superó el límite de carácteres"
        client.create_tweet(text=except_msg)


def run():
    tweet()


if __name__ == '__main__':
    run()
