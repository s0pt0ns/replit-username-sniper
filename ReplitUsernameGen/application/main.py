import requests
import json
import random
import colorama
import time
from colorama import Fore, Style
import threading

colorama.init()

threads = int(input('Threads: '))
length = int(input('Length of username: '))

def username_generate():
    global threads
    global length

    url = "https://replit.com/data/user/exists"
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']    

    while True:
        username = ''.join(random.choice(chars) for i in range(length))
        payload={"username":username}
        headers={
            'accept': 'application/json',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            'cookie': 'ajs_anonymous_id=5f170bbd-fab0-4e37-a680-18dba5e56bc6; _ga=GA1.2.1471855747.1662314853; __stripe_mid=761157a9-fdb4-4e07-af7a-32c89d99c5ff044672; connect.sid=s%3A-2iURbby6IC3TID3LGoclXwNR2V6G8NL.O%2FP9PYhzOrTZ8srxlSGkWdMZrLu1nxJNLw9LLw5paf4; gating_id=5f170bbd-fab0-4e37-a680-18dba5e56bc6; gating_id=5f170bbd-fab0-4e37-a680-18dba5e56bc6; _gid=GA1.2.646178534.1662948306; hubspotutk=7942af751e7a6ff226a4bedc36dda721; __hssrc=1; amplitudeSessionId=1662952762; _gat=1; replit_ng=1662952763.256.43.508746|8035451343a2d8f3e54599c71b2aec19; __hstc=205638156.7942af751e7a6ff226a4bedc36dda721.1662948306106.1662948306106.1662952763873.2; __hssc=205638156.1.1662952763873; __stripe_sid=07b73579-b31b-4964-a166-f9cf5b7b4abdd170e0; _dd_s=logs=1&id=99eb4c7b-4847-43aa-b208-6cbcb4c9c2b2&created=1662950608230&expire=1662953670275&rum=0',
            'origin': 'https://replit.com',
            'referer': 'https://replit.com/signup',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
        }
        r = requests.post(url, headers=headers,json=payload)
        try:
            r = r.json()
        except:
            print(f"{Fore.RED}Error")
        try:
            j = r['exists']
        except:
            print(f"{Fore.RED}Error")
            j = True
        if requests.post(url, headers=headers, json=payload).text == "too many requests":
            print(f"{Fore.RED}Too many requests")
            print(f"{Fore.BLUE}Cooling down for a second...")
            time.sleep(16.5)
        if j == False:
            print(f"{Fore.GREEN}{username}{Style.RESET_ALL} valid!")
            file = open('valid.txt', 'a')
            file.write(f'\n{username}')
            file.close()
        else:
            print(f"{Fore.YELLOW}Invalid username!")

for i in range(threads):
    threading.Thread(target=username_generate).start()
