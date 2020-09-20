import requests
from bs4 import BeautifulSoup

link_cr = 'https://www.the12rings.com'


def lead_webcr(arg):
    page = '/login'
    url = link_cr + page
    credentials = {
        'email': '12rbot.OP@gmail.com',
        'password': '12rgobrrrr'
    }
    text = ''
    res = []
    lvl = 0
    with requests.Session() as s:
        p = s.post(url, data=credentials)
        #   print(p)
        source = s.get(link_cr + '/leaderboard')
        plaintext = source.text
        bsoup = BeautifulSoup(plaintext, features="html.parser")
        f = open("bruh.txt", "w")
        for data_lead in bsoup.findAll(attrs={'id': 'tableData'}):
            text += str(data_lead)
        text = text.replace('<div id="tableData" style="display:none;">[', '')
        text = text.replace(']</div>', '')
        f.write(text)
        f.close()
        #print(text)
        temp = ''
        for i in range(len(text)):
            if text[i] == '{':
                temp += text[i]
            elif text[i] == '}':
                temp += text[i]
                res.append(temp)
                temp = ''
            if '{' in temp and text[i] != '{':
                temp += text[i]

        complete = []
        flag = False
        for i in range(0,arg):
            complete.append(res[i])
        return complete



def leaderb():
    page = '/login'
    url = link_cr + page
    credentials = {
        'email': '12rbot.OP@gmail.com',
        'password': '12rgobrrrr'
    }
    text = ''
    res = []
    lvl = 0
    with requests.Session() as s:
        p = s.post(url, data=credentials)
        #   print(p)
        source = s.get(link_cr + '/leaderboard')
        plaintext = source.text
        bsoup = BeautifulSoup(plaintext, features="html.parser")
        f = open("bruh.txt", "w")
        for data_lead in bsoup.findAll(attrs={'id': 'tableData'}):
            text += str(data_lead)
        text = text.replace('<div id="tableData" style="display:none;">[', '')
        text = text.replace(']</div>', '')
        f.write(text)
        f.close()
        #print(text)
        temp = ''
        for i in range(len(text)):
            if text[i] == '{':
                temp += text[i]
            elif text[i] == '}':
                temp += text[i]
                res.append(temp)
                temp = ''
            if '{' in temp and text[i] != '{':
                temp += text[i]


        flag = False
        return res