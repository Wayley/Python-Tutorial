from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests
import random
bot = Bot()


# linux执行登陆请调用下面的这句
#bot = Bot(console_qr=2,cache_path="botoo.pkl")
def get_news():
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    content = r.json()['content']
    note = r.json()['note']
    return content, note


def send_news():
    try:
        contents = get_news()
        # 你朋友的微信名称，不是备注，也不是微信帐号。
        my_friend = bot.friends().search('Omine')[0]
        my_friend.send(contents[0])
        my_friend.send(contents[1])
        my_friend.send(u"我是机器人wz, 前面两句是我在金山词霸上面抓取的英文和翻译~~~~ 爱雪宝宝的呀")

        ran_int = random.randint(0, 10)
        t = Timer(10 + ran_int, send_news)

        t.start()
    except:

        # 你的微信名称，不是微信帐号。
        my_friend = bot.friends().search('Omine')[0]
        my_friend.send(u"我是机器人wz,网络不好, -----爱雪宝宝的呀")


if __name__ == "__main__":
    send_news()
