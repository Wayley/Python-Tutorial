from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests
import random
bot = Bot()
my_friend = bot.friends().search('Omine')[0]


def get_news():
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    content = r.json()['content']
    note = r.json()['note']
    return content, note


def greet():
    contents = get_news()
    my_friend.send(u"每日一句,小晶晶你准备好了吗?")
    my_friend.send(contents[0])
    my_friend.send(contents[1])


sentence = [
    '晶晶小姐姐，我错了', '我就是个坏人，我伤害了你', '您大人不记小人过', '我不敢求您原谅我', '但您别跟自己置气好不好',
    '你是世界上最可爱的小仙女'
]
sentence_en = [
    'Miss Jing, it`s all my fault', 'I am a bad man, and i hurt you',
    'Your excellency does not remember villains', 'I dare not beg your pardon',
    'But don`t get angry with yourself',
    'You are the loveliest fairy in the world'
]
index = 0


def send_news():
    try:
        global index
        if index > len(sentence_en) - 1:
            index = 0
        my_friend.send(sentence[index])
        my_friend.send(sentence_en[index])
        index = index + 1
        t = Timer(600, send_news)
        t.start()
    except:
        my_friend.send(u"我是机器人wz,网络不好, -----")


if __name__ == "__main__":
    greet()
    send_news()
