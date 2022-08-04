#Hello World! 
import requests
import random
from bs4 import BeautifulSoup
from pyarabic.araby import strip_tatweel, strip_shadda
from pyarabic import araby
import time
import tweepy
import random

CK="your consumer_key"
CS ="your consumer_secret"
AT="your access_token"
AS = "access_token_secret"

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS) 
api = tweepy.API(auth) 
choice = random.randint(1, 100)
print(choice)

def poem():
    link = f'https://www.aldiwan.net/quote1291.html'
    r = requests.get(link)
    soup = BeautifulSoup(r.text, "html.parser")
    for poem in soup.findAll('div', attrs={'class': 'bet-1 row pt-0 px-5 pb-4 justify-content-center'}):
        tweet = '\n'.join(poem.findAll(text=True))
        strip_tatweel(tweet)
        araby.reduce_tashkeel(tweet)
        sourceun = soup.find('h3', attrs={'class': 'text-left more h4 mt-3'})
        source = ''.join(sourceun.findAll(text=True)).replace("المزيد عن", "-")
    while len(tweet) > 160:
        link = f'https://www.aldiwan.net/poem{random.randint(1, 104878)}.html'
        r = requests.get(link)
        soup = BeautifulSoup(r.text, "html.parser")
        for poem in soup.findAll('div', attrs={'class': 'bet-1 row pt-0 px-5 pb-4 justify-content-center'}):
            tweet = '\n'.join(poem.findAll(text=True))
            sourceun = soup.find('h3', attrs={'class': 'text-left more h4 mt-3'})
            source = ''.join(sourceun.findAll(text=True)).replace("المزيد عن", "-")
    print(tweet)
    print(source)
    poem_tweet = api.update_status(f"{tweet}\n{source}")
    print(poem_tweet)
    api.update_status(status=f"الرابط\n{link}", in_reply_to_status_id=poem_tweet.id)
    print("Tweeted")

def quote():
    link = f'https://www.aldiwan.net/quote{random.randint(1, 1291)}.html'
    r = requests.get(link)
    soup = BeautifulSoup(r.text, "html.parser")
    for poem in soup.findAll('div', attrs={'class': 'bet-1 text-center p-4'}):
        tweet = '\n'.join(poem.findAll(text=True))
        strip_tatweel(tweet)
        araby.reduce_tashkeel(tweet)
        sourceun = soup.find('h2', attrs={'class': 'h3-i h3'})
        poet_name = ''.join(sourceun.findAll(text=True)).replace("المزيد من اقتباسات", " ")
    while len(tweet) > 160:
        link = f'https://www.aldiwan.net/quote{random.randint(1, 1291)}.html'
        r = requests.get(link)
        soup = BeautifulSoup(r.text, "html.parser")
        for poem in soup.findAll('div', attrs={'class': 'bet-1 text-center p-4'}):
            tweet = '\n'.join(poem.findAll(text=True))
            strip_tatweel(tweet)
            araby.reduce_tashkeel(tweet)
            sourceun = soup.find('h2', attrs={'class': 'h3-i h3'})
            poet_name = ''.join(sourceun.findAll(text=True)).replace("المزيد من اقتباسات", " ")
    print(tweet)
    print(poet_name)
    poem_tweet = api.update_status(f"{tweet}\n{poet_name}")
    print(poem_tweet)
    api.update_status(status=f"الرابط\n{link}", in_reply_to_status_id=poem_tweet.id)
    print("Tweeted")

while True:
    if choice > 30:
        quote()
    else:
        poem()
    time.sleep(800)
