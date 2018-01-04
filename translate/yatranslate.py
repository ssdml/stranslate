# import urllib
import translate 
import urllib.request
import urllib.parse
import json
from functools import lru_cache

class YaTranslate():
    def __init__(self, key):
        self.host = 'https://translate.yandex.net'
        self.key = 'key=' + key

    def get_response(self, url_param, method="GET"):
        return json.loads(self.connect(url_param, method="GET"))

    def connect(self, url_param, method="GET"):
        html = ''
        with urllib.request.urlopen(self.host + url_param) as response:
            html = response.read()
            return html

    def get_support_languages(self):
        url_param = '/api/v1.5/tr.json/getLangs?'
        url_param += self.key
        return self.get_response(url_param)

    def detect_language(self, text):
        url_param = '/api/v1.5/tr.json/detect?'
        url_param += self.key
        url_param +=  '&text=' + text
        return self.get_response(url_param)

    @lru_cache(maxsize=1024)
    def translate(self, text, lang='ru'):
        if not text:
            return ''
        url_param = '/api/v1.5/tr.json/translate?'
        url_param += self.key
        url_param += '&' + urllib.parse.urlencode({'text': text})
        url_param += '&lang=' + lang

        self.resonse = self.get_response(url_param)
        return self.resonse['text'][0]
