# coding:utf-8
from wxpy import *

base_bot = Bot(True)

# 查找指定群聊群聊
group = base_bot.groups().search('Python交流群')

# 自动接受新的好友请求
@base_bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    # 接受好友请求
    new_friend = msg.card.accept()
    # 向新的好友发送消息
    new_friend.send('你好，我是群聊机器人，回复口令进入群聊天哦！')

# 接收文字消息的装饰器
@base_bot.register(msg_types=TEXT)
def add_into_chatroom(msg):
    # 接收进群口令
    if msg.text.lower() == 'python':
        # use_invitation为True，发送群邀请，False则拉进群聊
        group[0].add_members(msg.sender, use_invitation=True)
    else:
        # 其他消息
        return u'收到：' + msg.text

base_bot.join()
