import requests
import random
from bs4 import BeautifulSoup
import time
import tweepy
import random

#twitter api keys
CK="your consumer_key"
CS ="your consumer_secret "
AT="your access_token"
AS = "your access_token_secret"

#مصادقه مكتبه tweepy مايحتاج تغير فيه
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS) 
api = tweepy.API(auth) 



#داله القصائد
def poem():
    #رابط القصائد العشوائي
    link = f'https://www.aldiwan.net/poem{random.randint(1, 104878)}.html'
    #ارسال الريكويست
    r = requests.get(link)
    #تعريف مكتبة bs
    soup = BeautifulSoup(r.text, "html.parser")
    #يبحث عن الابيات
    for poem in soup.findAll('div', attrs={'class': 'bet-1 row pt-0 px-5 pb-4 justify-content-center'}):
        #يجمع الابيات في متغير واحد
        tweet = '\n'.join(poem.findAll(text=True))
        #يبحث عن اسم الشاعر
        sourceun = soup.find('h3', attrs={'class': 'text-left more h4 mt-3'})
        #يستخرج اسم الشاعر ويشيل الكلام الزايد
        source = ''.join(sourceun.findAll(text=True)).replace("المزيد عن", "-")
        #اذا كانت الابيات عدد احرفها فوق ال١٦٠ يرجع يختار مره ثانية ويسوي نفس الشغل فوق بالضبط لين يلقى قصيدة اقل من ١٦٠
    while len(tweet) > 160:
        link = f'https://www.aldiwan.net/poem{random.randint(1, 104878)}.html'
        r = requests.get(link)
        soup = BeautifulSoup(r.text, "html.parser")
        for poem in soup.findAll('div', attrs={'class': 'bet-1 row pt-0 px-5 pb-4 justify-content-center'}):
            tweet = '\n'.join(poem.findAll(text=True))
            sourceun = soup.find('h3', attrs={'class': 'text-left more h4 mt-3'})
            source = ''.join(sourceun.findAll(text=True)).replace("المزيد عن", "-")
    #طباعة اسم الابيات واسم الشاعر
    print(tweet)
    print(source)
    #متغير لأرسال تغريدة في تويتر مع الابيات واسم الشاعر
    poem_tweet = api.update_status(f"{tweet}\n{source}")
    #يرد على التغريدة حقت القصيدة الي رسلها تو مع الرابط
    api.update_status(status=f"الرابط\n{link}", in_reply_to_status_id=poem_tweet.id)
    #عشان تتاكد انه رسل
    print("Tweeted")

#داله الاقتباس
def quote():
    #رابط الاقتباس العشوائي من ١ الى ١٢٩١
    link = f'https://www.aldiwan.net/quote{random.randint(1, 1291)}.html'
    #ارسال الريكويست
    r = requests.get(link)
    #تعريف مكتبه bs4
    soup = BeautifulSoup(r.text, "html.parser")
    #يبحث عن الابيات
    for poem in soup.findAll('div', attrs={'class': 'bet-1 text-center p-4'}):
        #متغير يجمع الابيات كلها
        tweet = '\n'.join(poem.findAll(text=True))
        #يبحث عن اسم الشاعر
        sourceun = soup.find('h2', attrs={'class': 'h3-i h3'})
        #يحط اسم الشاعر في متغير ويشيل الزوائد من النص
        poet_name = ''.join(sourceun.findAll(text=True)).replace("المزيد من اقتباسات", " ")
        #اذا كانت الابيات فوق ال١٦٠ حرف يرجع يختار مره ثانيه ويسوي كل شي الين يلقى اقل من ١٦٠ حرف
    while len(tweet) > 280:
        link = f'https://www.aldiwan.net/quote{random.randint(1, 1291)}.html'
        r = requests.get(link)
        soup = BeautifulSoup(r.text, "html.parser")
        for poem in soup.findAll('div', attrs={'class': 'bet-1 text-center p-4'}):
            tweet = '\n'.join(poem.findAll(text=True))
            sourceun = soup.find('h2', attrs={'class': 'h3-i h3'})
            poet_name = ''.join(sourceun.findAll(text=True)).replace("المزيد من اقتباسات", " ")
    #طباعة الابيات
    print(tweet)
    #طباعه اسم الشاعر
    print(poet_name)
    #متغير لارسال التغريدة مع الابيات واسم الشاعر في تويتر
    poem_tweet = api.update_status(f"{tweet}\n{poet_name}")
    #يرد على التغريده الي نزلها بالرابط حق الاقتباس
    api.update_status(status=f"الرابط\n{link}", in_reply_to_status_id=poem_tweet.id)
    #عشان تعرف انه سوا كل شي
    print("Tweeted")




#تكرار
while True:
    #اختيار رقم عشوائي لتحديد بين قصيدة او اقتباس وطباعته
    choice = random.randint(1, 10)
    print(choice)
    #اذا كان الرقم العشوائي فوق الخمسه يختار اقتباس
    if choice > 5:
        print("Quote")
        quote()
    #اذا كان الرقم تحت الخمسه يختار قصيدة
    else:
        print("Poem")
        poem()
    #انتظار ٨٠٠ ثانية 
    time.sleep(800)
