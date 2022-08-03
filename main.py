import requests
import random
from bs4 import BeautifulSoup
from pyarabic.araby import strip_tatweel, strip_shadda
from pyarabic import araby
import time
import tweepy

CK= "your consumer_key"
CS ="Your consumer_secret"
AT="your access_token"
AS = "your access_token_secret"

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS) 
api = tweepy.API(auth) 

def main():
    link = f'https://www.aldiwan.net/poem{random.randint(1, 104878)}.html'
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

while True:
    main()   
    time.sleep(1800)
