__author__ = 'sshejko'

import httplib, urllib
import os
import xml.etree.ElementTree as ET

class yandex_spellchecker:

    base_url = r'http://speller.yandex.net/services/spellservice/checkText'
    post_url = r'/services/spellservice/checkText'

    def __init__(self):
        pass


    def get_result_post(self, text_in, c_lang):
        params = urllib.urlencode({'text': text_in, 'format': "plain", 'lang': c_lang})
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        conn = httplib.HTTPConnection("speller.yandex.net")
        conn.request("POST", self.post_url, params, headers)
        response = conn.getresponse()
        print response.status, response.reason
        data = response.read()
        print(data)
        conn.close()
        return data


    def get_result_get(self, text_in, c_lang):
        #params = urllib.urlencode({'text': text_in, 'format': "plain", 'lang': c_lang})
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        new_url = self.post_url + '?text=' + text_in.replace(' ', '+') + '&' + 'format=plain' + '&' + 'lang=' + c_lang
        conn = httplib.HTTPConnection("speller.yandex.net")
        conn.request("GET", new_url, headers=headers)
        response = conn.getresponse()
        print response.status, response.reason
        data = response.read()
        print(data)
        conn.close()
        return data

    def check_text(self, text_in, c_lang):
        result_xml = self.get_result_post(text_in, c_lang)
        root = ET.fromstring(result_xml)
        errors = root.findall("./error")
        words = []
        pos = []
        for err in errors:
            c_word = err.find("./word").text
            c_pos = err.attrib
            #print(c_word)
            #print(c_pos)
            words.append(c_word)
            cur_pos = (int(c_pos['pos']), int(c_pos['len']))
            pos.append(cur_pos)

        return words, pos
