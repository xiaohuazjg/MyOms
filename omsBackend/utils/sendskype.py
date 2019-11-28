# -*- coding: utf-8 -*-
# author: itimor

# 登录skype
from skpy import Skype

# skype账号//


SK_ACOUNT = {
    'sk_user': 'itimor@126.com',
    'sk_pass': 'xx'
}
#SK = Skype(SK_ACOUNT["sk_user"], SK_ACOUNT["sk_pass"])
SK = 'sk'


def skype_bot(user, content):
    chat = SK.chats[user]
    chat.sendMsg(content)


if __name__ == '__main__':
    skypeid = 'live:7ba0e5a23ae6d2a6'
    msg = 'aaaa hhhh'
    user = '8:' + skypeid  # skypeid 前面需要加 8
    skype_bot(user, msg)
