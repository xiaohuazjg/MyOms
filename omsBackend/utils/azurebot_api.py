# -*- coding: utf-8 -*-
# author: huashaw

import requests
import datetime


class BotAPI(object):
    def __init__(self, client_id, client_secret):
        self.login_url = 'https://login.microsoftonline.com/botframework.com/oauth2/v2.0/token'
        self.bot_url = 'https://smba.trafficmanager.net/apis/v3/conversations/'
        self.grant_type = "client_credentials"
        self.scope = "https://api.botframework.com/.default"
        self.client_id = client_id
        self.client_secret = client_secret
        self.__header = dict()
        self.token_s_time = ''
        self.__token = self.get_token()

    def get_token(self):
        """
        登录获取token
        """
        self.__header["Accept"] = "application/x-www-form-urlencoded"
        data = {
            "grant_type": self.grant_type,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "scope": self.scope
        }
        req = requests.post(self.login_url, data=data, headers=self.__header, verify=False)
        try:
            token = req.json()["access_token"]
            self.token_s_time = datetime.datetime.now()
            return token
        except KeyError:
            raise KeyError

    def http_request(self, url, data):
        """
        接收请求，返回结果
        """
        self.__header["Accept"] = "application/json"
        self.__header["Authorization"] = "Bearer " + self.__token
        token_e_time = datetime.datetime.now()
        print("token_e_time: %s" % token_e_time)
        print("token_s_time: %s" % self.token_s_time)

        if (token_e_time - self.token_s_time).seconds > 4000:
            print("Bot token is Expired")
            self.get_token()

        # 传入data参数字典，data为None 则方法为get，有date为post方法
        data["from"] = {"id": self.client_id}
        req = requests.post(url, json=data, headers=self.__header, verify=False)
        try:
            return req.json()
        except:
            print(req.content)

    def send_message(self, sender, message):
        url = self.bot_url + sender + '/activities/'

        payload = {
            "type": "message",
            "text": message
        }
        content = self.http_request(url, payload)
        try:
            return content['id']
        except:
            return {'msg': 'send msg error'}

    def create_buttons(self, type, name, value):
        buttons_dict = {}
        buttons_dict["type"] = type
        buttons_dict["title"] = name
        # buttons_dict['image'] = image
        buttons_dict["value"] = value
        return buttons_dict

    def create_card_image(self, url, alt):
        img_dict = {}
        img_dict["url"] = url
        img_dict["alt"] = alt
        return img_dict

    def create_card_attachment(self, type, title, subtitle, text, images, buttons):
        card_attachment = {
            "contentType": "application/vnd.microsoft.card." + type,
            "content": {
                "title": title,
                "subtitle": subtitle,
                "text": text,
                "images": images,
                "buttons": buttons
            }
        }

        return card_attachment

    def send_media(self, sender, type, contentUrl):
        url = self.bot_url + sender + '/activities/'
        payload = {
            "type": "message",
            "attachments": [{
                "contentType": type,
                "contentUrl": contentUrl
            }]
        }
        content = self.http_request(url, payload)
        print(content)

    def send_card(self, sender, type, card_attachment, summary, text):
        url = self.bot_url + sender + '/activities/'
        payload = {
            "type": "message",
            "attachmentLayout": type,
            "summary": summary,
            "text": text,
            "attachments": card_attachment
        }
        content = self.http_request(url, payload)
        print(content)

    def send_action(self, sender):
        url = self.bot_url + sender + '/activities/'
        payload = {
            "type": "typing"
        }
        content = self.http_request(url, payload)
        print(content)

    def create_animation(self, type, url, images, title, subtitle, text, buttons):
        card_animation = {
            "contentType": "application/vnd.microsoft.card." + type,
            "content": {
                "autoloop": True,
                "autostart": True,
                "shareable": True,
                "media": [{"profile": "gif", "url": url}],
                "title": title,
                "subtitle": subtitle,
                "text": text,
                "images": images,
                "buttons": buttons
            }
        }
        return card_animation


if __name__ == '__main__':
    bot_info = {
        "grant_type": "client_credentials",
        "client_id": "43ceb722-a3a5-4de3-9f31-2e04dd89efc4",
        "client_secret": "tCM6526@ifokqgTABTN4=_{",
        "scope": "https://api.botframework.com/.default"
    }
    bot = BotAPI(bot_info['client_id'], bot_info['client_secret'])
    sender = '19:629c0056c46f435291b24339fed22a09@thread.skype'

    # send message
    message = "你好！很高兴认识你"
    # bot.send_message(sender, message)

    # send imgae
    url1 = 'http://s5.sinaimg.cn/mw690/003PHSZvgy6Yw3HTXikf4'
    url2 = 'http://source.chengdumote.com/wp-content/uploads/2017/09/1.jpg'
    img1 = bot.create_card_image(url1, alt="夏美酱")
    img2 = bot.create_card_image(url2, alt="夏美酱")
    #bot.send_media(sender, "image/jpg", url1)

    # send card
    button1 = bot.create_buttons("imBack", "喜欢我", "喜欢")
    button2 = bot.create_buttons("openUrl", "更多我", "https://www.nvshens.com/g/26067/")
    attachment1 = bot.create_card_attachment("hero", "夏美酱", subtitle="性感女神", text="童颜巨乳", images=[img1], buttons=[button1, button2])
    attachment2 = bot.create_card_attachment("hero", "夏美酱", subtitle="性感女神", text="国色天香", images=[img2], buttons=[button1, button2])
    bot.send_card(sender, "carousel", [attachment1, attachment2], summary=message, text="夏美酱")

    # send action
    #bot.send_action(sender)