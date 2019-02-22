import tweepy
import flask
from flask import Flask
import time
import random

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello there<\h1>'
cnt = 0


quotes = [
'Live life to the fullest, and focus on the positive.',
'Good, better, best. Never let it rest. \'Til your good is better and your better is best.',
'The past cannot be changed. The future is yet in your power.',
'With the new day comes new strength and new thoughts.',
'It does not matter how slowly you go as long as you do not stop.',
'Expect problems and eat them for breakfast.',
'Your talent is God\'s gift to you. What you do with it is your gift back to God.',
'Quality is not an act, it is a habit.',
'Perseverance is not a long race; it is many short races one after the other.',
'Either you run the day or the day runs you.',
]


facts = [
'McDonald’s once made bubblegum-flavored broccoli',
'Peanuts aren’t technically nuts',
'Armadillo shells are bulletproof',
'Firefighters use wetting agents to make water wetter',
'Octopuses lay 56,000 eggs at a time',
'Kleenex tissues were originally intended for gas masks',
'Iceland’s last McDonald’s burger was sold eight years ago',
'The American flag was designed by a high school student',
'Only a quarter of the Sahara Desert is sandy',
'There were active volcanoes on the moon when dinosaurs were alive'
]

puns = [
'Q. How much money does a pirate pay for corn? A. A buccaneer.',
'Don’t interrupt someone working intently on a puzzle. Chances are, you’ll hear some crosswords.',
'I’m a big fan of whiteboards. I find them quite re-markable.',
'Yesterday, a clown held the door open for me. It was such a nice jester!',
'The machine at the coin factory just suddenly stopped working, with no explanation. It doesn’t make any cents!',
'I was going to make myself a belt made out of watches, but then I realized it would be a waist of time.',
'Q: Why do teenagers always travel in groups of 3, 5, or 7? A: Because they can’t even.',
'I knew a mathematician who couldn’t afford lunch. He could binomial.',
'Did you hear about the semi-colon that broke the law? He was given two consecutive sentences.',
'What’s the difference between a good joke and a bad joke timing.'
]

def return_random_thingy(what):
    x = random.randint(0,9)
    print("x = ")
    print(x)
    if what == 1:
        return quotes[x]
    elif what == 2:
        return facts[x]
    else:
        return puns[x]


def gives_what_you_want(wanted):
    if(wanted.find('joke') > -1 or wanted.find('pun') > -1 or wanted.find('one-liner') > -1 or wanted.find('one liner') > -1):
        return 3
    elif(wanted.find('fact') > -1 or wanted.find('trivia') > -1):
        return 2
    elif(wanted.find('quote') > -1 or wanted.find('motivation') > -1 or wanted.find('saying') > -1):
        return 1
    else:
        return 0


last_id = "xyz"
while(1):
    try:
        auth = tweepy.OAuthHandler('Yybj9Zxli9kQ7xaveSRrnfLab', '972KkTPmMHFpnZdE8yfD8Q1gQVqFzjToXJsvhuKoQVzHBZwCCU')
        auth.set_access_token("423504117-DnuIawnocUV7QUGOqCFRVIZbI7zDRftN6reEPLZN", "e53YQ4gVddD5GqiSukYXUqIPDjhbiwrxnc4s3VXtVIICl")
        api = tweepy.API(auth)
        print("In the loop")
        prev_tweet = ""

        for mentions in tweepy.Cursor(api.mentions_timeline).items(1):
            name = str(mentions.user.screen_name)
            print("mentions id = ")
            print(mentions.id)
            print("last id = ")
            print(last_id)
            if mentions.id == last_id:
                print('Didnt tweet, Already tweeted to this person')
            else:
                print('Tweeted')
                last_id = mentions.id
                api.update_status('@' + name + '#' + str(random.randint(1, 100000)) + ': ' + return_random_thingy(gives_what_you_want(str(mentions.text))))

        print("Done")
        time.sleep(60)
    except:
        print("Something went wrong, trying again...")
