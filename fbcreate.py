import os
import re
import random
import requests
import time
from faker import Faker
"""this code was written by tech Michael 
auto create Project with fb automation...
GitHub Profile https://github.com/Tech-Michael112
I'm not responsible for any damages caused by you"""


fake = Faker()
import random

def generate_phone_number():
    exp = ['80', '81', '90', '70']
    prefix = random.choice(exp)
    codef = random.randint(1, 9)
    line_number = random.randint(1000000, 9999999)
    return f"+234{prefix}{codef}{line_number}"

ug = []
for _ in range(1111):
    az = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    xr = random.choice(az)
    eith = str(random.randint(100, 811))
    zx = random.choice([xr, eith])
    build = f"{str(random.choice(zx))}{random.randint(11, 616)}{xr}"
    ver = ["11", "12", "14", "15", "6", "7", "8", "9", "4", "2", "1", "6"]
    version = random.choice(ver)
    dev = [
        "Samsung Galaxy S21 Ultra", "Samsung Galaxy Note 20", "Samsung Galaxy A52", "Samsung Galaxy Z Fold 3",
        "iPhone 13 Pro Max", "iPhone 12 Mini", "iPhone SE (2020)",
        "Xiaomi Redmi Note 10", "Xiaomi Mi 11 Ultra", "Xiaomi Poco X3 Pro",
        "OnePlus 9 Pro", "OnePlus Nord 2", "OnePlus 8T",
        "Huawei P50 Pro", "Huawei Mate 40", "Huawei Nova 7"
    ]
    dev = random.choice(dev)
    red = [
        "Redmi Note 13", "Redmi Note 13 Pro", "Redmi Note 8T", "Redmi Note 7",
        "Redmi Note 7 Pro", "Redmi Note 6 Pro", "Redmi Note 5", "Redmi Note 5 Pro",
        "Redmi Note 4", "Redmi Note 4X", "Redmi Note 3", "Redmi Note 3 Pro"
    ]
    redmi = random.choice(red)
    opx=random.choice(['SM-G920F','SM-T231','SM-J320F','GT-N7100','SM-T561','GT-I9500','SM-G930F','SM-J510FN','GT-I9500','SM-T561','SM-T531','SM-PH-L720','SM-J320F', 'KTU84P', 'SM-G900F', 'SM-S7390', 'SM-J320F', 'SM-P5100', 'SM-A500FU', 'SM-G930F', 'SM-J510FN', 'SM-T561', 'GT-N8000', 'SM-T531', 'SM-J510FN', 'SM-J510FN', 'SM-J320F', 'SN-P5110', 'GT-I9301I', 'SM-A500F', 'SM-G930F', 'SM-T311', 'SM-P5200', 'GT-I9301I', 'SM-J320M', 'SM-T531', 'SM-T820', 'GT-I9192', 'SM-G935F', 'SM-J701F;', 'GT-I9301I', 'SM-J320FN', 'SM-T111', 'SM-A500F', 'SM-J510FN', 'SM-T705', 'SM-G920F', 'GT-N5100', 'GT-I9300I', 'GT-I9300I', 'GT-N8000', 'GT-N8000', 'SM-A500F', 'GT-I9190H', 'SM-J510FN', 'SM-J320F', 'GT-P5100', 'GT-I9300I', 'GT-N5100', 'GT-N8000', 'GT-I9500'])
    samm = [
        "Samsung Galaxy S24 Ultra", "Samsung Galaxy S24 Plus", "Samsung Galaxy S24",
        "Samsung Galaxy S23 FE", "Samsung Galaxy S20 Ultra", "Samsung Galaxy S20 Plus",
        "Samsung Galaxy S20", "Samsung Galaxy A12", "Samsung Galaxy A11", "Samsung Galaxy A10s"]
    sung = random.choice(samm)
    samm=random.choice(['SAMSUNG SM-T530','SAMSUNG SM-T805','SAMSUNG SM-G530AZ','SAMSUNG SM-G925K','SAMSUNG SM-G925L','SAMSUNG SM-G925T','SAMSUNG SM-T337A','SAMSUNG SM-J110F','SAMSUNG SM-G890A','SAMSUNG SM-T355Y','SAMSUNG SM-T817T','SAMSUNG SM-G925F','SAMSUNG SM-G928F','SAMSUNG SM-W2021','SAMSUNG SM-A225F','SAMSUNG SM-A326B','SAMSUNG SM-A526B','SAMSUNG SM-A725F','SAMSUNG SM-A908B','SAMSUNG SM-T500','SAMSUNG SM-T720','SAMSUNG SM-T860','SAMSUNG SM-T970','SAMSUNG SM-T976B','SAMSUNG SM-F127G','SAMSUNG SM-F426B','SAMSUNG SM-F707B','SAMSUNG SM-F916U','SAMSUNG SM-F7110','SAMSUNG SM-N960F','SAMSUNG SM-N986B','SAMSUNG SM-N990F','SAMSUNG SM-N975F','SAMSUNG SM-N986U'])  
    realme_ua = f"Mozilla/5.0 (Linux; Android {version}; RMX{random.randint(3706, 58866)} Build/UKQ1.{random.randint(230, 711)}{random.randint(924, 1000)}.00{random.randint(1, 9)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randint(120, 818)}.0.{random.randint(6099, 9199)}.{random.randint(144, 515)} Mobile Safari/537.36"
    realme_ua1 = f"Mozilla/5.0 (Linux; Android {version}; RMX{random.randint(3706, 58866)}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randint(116, 617)}.0.0.0 Mobile Safari/537.36"
    realme_ua2 = f"Mozilla/5.0 (Linux; U; Android {random.randint(11, 15)}; en-us; RMX{random.randint(3706, 8886)}{xr}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randint(90, 777)}.0.{random.randint(4430, 72222)}.{random.randint(61, 777)} Mobile Safari/537.36"
    useragent_chrome = f"Mozilla/5.0 (Linux; U; Android {random.randint(6, 15)}; en-us; {random.randint(2206123, 99999999)}SC Build/UKQ1.{random.randint(231003, 99999999)}.00{random.randint(2, 7)}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randint(209, 777)}.0.{random.randint(5414, 8777)}.{random.randint(118, 666)} Mobile Safari/537.36"
    ua12 = f"Mozilla/5.0 (Linux; U; Android {version}; en-us; {dev} Build/UP1A.{random.randint(230905, 8888888)}.0{random.randint(11, 22)}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randint(109, 888)}.0.{random.randint(5414, 9999)}.{random.randint(118, 599)} Mobile Safari/537.36"
    sm = f"Mozilla/5.0 (Linux; Android {random.randint(8, 15)}; {sung} Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randint(81, 777)}.0.{random.randint(1044, 6566)}.{random.randint(111, 666)} Safari/537.36"
    redd = f"Mozilla/5.0 (Linux; Android {random.randint(5, 10)}.{random.randint(0, 9)}.{random.randint(0, 10)}; {redmi} Build/{random.randint(112184, 845424)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(80, 911)}.0.{random.randint(3987, 8188)}.{random.randint(149, 888)} Mobile Safari/537.36"
    rmm5=f"Mozilla/5.0 (Linux; Android {random.randint(6,15)}; {opx}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(79,90)}.0.{random.randint(3945,72727)}.{random.randint(136,777)} Mobile Safari/537.36"
    bsgt=f"Mozilla/5.0 (Linux; Android {random.randint(2,15)}; SAMSUNG {opx}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{random.randint(1,15)}.1 Chrome/{random.randint(75,622)}.0.{random.randint(2770,6665)}.{random.randint(143,777)} Mobile Safari/537.36"
    ass=f"Mozilla/5.0 (Linux; Android {random.randint(11,15)}; {samm} Build/QP1A.{random.randint(190711,888888)}.0{random.randint(20,66)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randint(27,77)}.0.{random.randint(4692,8888)}.{random.randint(22,68)} Mobile Safari/537.36"
    u = random.choice([realme_ua, realme_ua1, realme_ua2, useragent_chrome, ua12, sm, redd,rmm5,bsgt,ass])   
    ug.append(u)

def generate_usa_phone_number():
    area_code = random.randint(200, 999)
    prefix = random.randint(200, 999)
    line_number = random.randint(1000, 9999)
    return f"+1{area_code}{prefix}{line_number}"

    
def create_fake_name():
    full_name = fake.name()
    first_name, last_name = full_name.split()[:2]
    return first_name, last_name

def main():
    try:
        os.system('clear')
        print("\t   [ Author : Tech - Michael ] ")
        print("\t   [ Version 2.0.0A ] ")
        
        print("\t   [ FB Auto Create Main Menu ] ")
        print(53 * "_")
        print("1. Create Nigeria Facebook  ")
        print("2. Create USA Facebook")      
        print("3. Mail Service by Michael")
        print(53 * "_")
        ot = input(' Choose an option: ')
        if ot == '1':
            create_multi()
        elif ot == '2':
            create_usa()
        elif ot == '3':
            mail() 
        
    except KeyError as Error:
        print(f'Something went wrong: {Error}')
        pass

ok=[]
def create_multi():
    while True:
        print("\t setting up mail servers...")
        time.sleep(1)
        try:
            print("\n")
            limit = int(input('How many accounts do you want to create? '))
        except ValueError as bin:
            print(f"Error: {bin}")
            continue
        
        for _ in range(limit):
            session = requests.session()
            
            print(f"[Creating...] \033[1;32m|{str(len(ok))}|\033[1;0m")
            url = 'https://web.facebook.com/r.php'
            try:
                rs = session.get(url)
                
                rs.raise_for_status()
            except requests.RequestException as e:
                

                continue

            try:
                
                jazoest = re.search(r'name="jazoest" value="(.*?)"', str(rs.text)).group(1)
                lsd = re.search(r'name="lsd" value="(.*?)"', str(rs.text)).group(1)
                reg_instance = re.search(r'name="reg_instance" value="(.*?)"', str(rs.text)).group(1)
                ri = re.search(r'name="ri" value="(.*?)"', str(rs.text)).group(1)
                captcha_persist_data = re.search(r'name="captcha_persist_data" value="(.*?)"', str(rs.text)).group(1)
                 
            except AttributeError as e:
                continue

            
            pas = "SSN@!16@6799"       
            first_name, last_name = create_fake_name()
            n = generate_phone_number()
            us=random.choice(ug)
            
            ue=f"Mozilla/5.0 (Android) AppleWebKit/{random.randint(589,900)}.{random.randint(8,14)}.{random.randint(1,17)} (KHTML, like Gecko) Chrome/{random.randint(110,777)}.0.{random.randint(8575,92989)} Safari/589.9.7"
            
            headersX = {
    'authority': 'www.facebook.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.facebook.com',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': us,
    'viewport-width': '980',
    'x-asbd-id': '129477',
    'x-fb-lsd': lsd,}
            dataX = {
    'jazoest': jazoest,
    'lsd': lsd,
    'firstname': first_name,
    'lastname': last_name,
    'reg_email__': n,
    'reg_email_confirmation__': n,
    'reg_passwd__': pas,
    'birthday_day': str(random.randint(1, 20)),
    'birthday_month': str(random.randint(1, 12)),
    'birthday_year': f'19{random.randint(22, 79)}',
    'birthday_age': '',
    'did_use_age': 'false',
    'sex': str(random.randint(1, 2)),
    'preferred_pronoun': '',
    'custom_gender': '',
    'referrer': '',
    'asked_to_login': '0',
    'use_custom_gender': '',
    'terms': 'on',
    'ns': '0',
    'ri': ri,
    'action_dialog_shown': '',
    'ignore': 'captcha',
    'locale': 'en_GB',
    'reg_instance': reg_instance,
    'captcha_persist_data': captcha_persist_data,
    'captcha_response': '',
    '__user': '0',
    '__a': '1',
    '__req': '8',
    '__hs': '19934.BP:DEFAULT.2.0..0.0',
    'dpr': '2',
    '__ccg': 'GOOD',
    '__rev': '1015250448',
    '__s': '0fk0jz:jng6tr:a3pmr9',
    '__hsi': '7397378468620993870',
    '__dyn': '',
    '__csr': '',
    '__spin_r': '1015250448',
    '__spin_b': 'trunk',
    '__spin_t': '1722336390'
}
            
            try:
                response = session.post("https://www.facebook.com/ajax/register.php", headers=headersX, data=dataX)
                response.raise_for_status()
             #   print(response.content)
                
            except requests.RequestException as e:
                

                continue

            ck = '; '.join([str(x) + "=" + str(y) for x, y in session.cookies.get_dict().items()])
            print('\n')
            print(f" First Name : {first_name}")
            print(f" Last Name : {last_name}")
            print(f" Account Created {n}|{pas}\033[1;0m")
            time.sleep(1)
            print(f" Check-in if account is valid \033[1;0m")            
            try:
                ree = session.get('https://x.prod.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8').text 
                ua=random.choice(ug)
                head = {
                'User-Agent': ua,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Content-Type': 'application/x-www-form-urlencoded',
                'cache-control': 'max-age=0',
                'dpr': '2',
                'viewport-width': '980',
                'sec-ch-prefers-color-scheme': 'dark',
                'upgrade-insecure-requests': '1',
                'origin': 'https://mbasic.facebook.com',
                'x-requested-with': 'mark.via.gp',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
            }
            
                data = {
                'lsd': lsd,
                'jazoest': jazoest,
                'li': 'djalZs-Slr4WUsrUKuYtMQPG',
                'try_number': '0',
                'unrecognized_tries': '0',
                'email': n,
                'pass': pas,
                'login': 'Log in',
                'bi_xrwh': '92004344361786634',
            }
            
                
                url = "https://mbasic.facebook.com/login/device-based/regular/login/?next=https://mbasic.facebook.com/settings/account/&refsrc=deprecated&lwv=100&ref=dbl"
                try:
                    req = session.post(url, cookies={"cookie": ck}, headers=head, data=data)
                    req.raise_for_status()                   
                except requests.RequestException as e:                  
                    continue
                c = '; '.join([str(x) + "=" + str(y) for x, y in session.cookies.get_dict().items()])                           
                if "Confirm your account" in str(req.content):
                    uid=re.search("c_user=(\d+)",str(c)).group(1)                  
                    print(f"\033[1;32m [Successful] {n}|{pas}\033[1;0m")
                    print(f" [User ID] = {uid}\033[1;0m")             
                    print(f" Use any temporary mail for confirmation on {uid}")        
                    c = '; '.join([str(x) + "=" + str(y) for x, y in session.cookies.get_dict().items()])           
                    print(f" [Cookie_Data]= {c}")    
                    ok.append(n)              
                    open(f"SSN_CREATE.txt","a").write(f"{uid}|{n}|{pas}\n")  
                elif  "We need more information" in str(req.content) or "We're working on getting this fixed as soon as we can." in  str(response.content):                
                    print(f"\033[1;91m [Checkpoint] {n}|{pas}\033[1;0m")
            except requests.RequestException as e:               
                continue                


def create_usa():
    while True:
        print("\t setting up mail servers...")
        time.sleep(1)
        try:
            print("\n")
            limit = int(input('How many accounts do you want to create? '))
        except ValueError as bin:
            print(f"Error: {bin}")
            continue
        
        for _ in range(limit):
            session = requests.session()
            
            print(f"[Creating...] \033[1;32m|{str(len(ok))}|\033[1;0m")
            url = 'https://web.facebook.com/r.php'
            try:
                rs = session.get(url)
                
                rs.raise_for_status()
            except requests.RequestException as e:
                

                continue

            try:
                
                jazoest = re.search(r'name="jazoest" value="(.*?)"', str(rs.text)).group(1)
                lsd = re.search(r'name="lsd" value="(.*?)"', str(rs.text)).group(1)
                reg_instance = re.search(r'name="reg_instance" value="(.*?)"', str(rs.text)).group(1)
                ri = re.search(r'name="ri" value="(.*?)"', str(rs.text)).group(1)
                
                captcha_persist_data = re.search(r'name="captcha_persist_data" value="(.*?)"', str(rs.text)).group(1)
                
            except AttributeError as e:
                continue

            ua = random.choice(ug)
            pas = "SSN@!16@6799"       
            first_name, last_name = create_fake_name()
            m = generate_usa_phone_number()
            uuu=f"Mozilla/5.0 (CrOS) AppleWebKit/{str(random.randint(566,900))}.{random.randint(0,9)}.{random.randint(0,11)} (KHTML, like Gecko) Chrome/{random.randint(79,100)}.0.{random.randint(8485,98888)} Safari/{random.randint(266,666)}.{random.randint(5,14)}.{random.randint(0,11)}"       
            uakku=f"Mozilla/5.0 (Android) AppleWebKit/{random.randint(548,4443)}.{random.randint(8,92)}.2 (KHTML, like Gecko) Chrome/{random.randint(103,900)}.0.{random.randint(7954,99999)} Safari/{random.randint(548,1444)}.{random.randint(8,99)}.{random.randint(2,55)}"
            ue=f"Mozilla/5.0 (Android) AppleWebKit/{random.randint(589,900)}.{random.randint(8,14)}.{random.randint(1,17)} (KHTML, like Gecko) Chrome/{random.randint(110,777)}.0.{random.randint(8575,92989)} Safari/589.9.7"
            uaz=random.choice([uuu,uakku])
            
            headersX = {
    'authority': 'www.facebook.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.facebook.com',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': uaz,
    'viewport-width': '980',
    'x-asbd-id': '129477',
    'x-fb-lsd': lsd,}
            dataX = {
    'jazoest': jazoest,
    'lsd': lsd,
    'firstname': first_name,
    'lastname': last_name,
    'reg_email__': m,
    'reg_email_confirmation__': m,
    'reg_passwd__': pas,
    'birthday_day': str(random.randint(1, 20)),
    'birthday_month': str(random.randint(1, 12)),
    'birthday_year': f'19{random.randint(22, 79)}',
    'birthday_age': '',
    'did_use_age': 'false',
    'sex': str(random.randint(1, 2)),
    'preferred_pronoun': '',
    'custom_gender': '',
    'referrer': '',
    'asked_to_login': '0',
    'use_custom_gender': '',
    'terms': 'on',
    'ns': '0',
    'ri': ri,
    'action_dialog_shown': '',
    'ignore': 'captcha',
    'locale': 'en_GB',
    'reg_instance': reg_instance,
    'captcha_persist_data': captcha_persist_data,
    'captcha_response': '',
    '__user': '0',
    '__a': '1',
    '__req': '8',
    '__hs': '19934.BP:DEFAULT.2.0..0.0',
    'dpr': '2',
    '__ccg': 'GOOD',
    '__rev': '1015250448',
    '__s': '0fk0jz:jng6tr:a3pmr9',
    '__hsi': '7397378468620993870',
    '__dyn': '',
    '__csr': '',
    '__spin_r': '1015250448',
    '__spin_b': 'trunk',
    '__spin_t': '1722336390'
}
            url = "https://www.facebook.com/ajax/register.php"
            try:
                response = session.post(url, headers=headersX, data=dataX)
                response.raise_for_status()
                print(response.content)
                
            except requests.RequestException as e:
                

                continue

            ck = '; '.join([str(x) + "=" + str(y) for x, y in session.cookies.get_dict().items()])
            print('\n')
            print(f" First Name : {first_name}")
            print(f" Last Name : {last_name}")
            print(f" Account Created {m}|{pas}\033[1;0m")
            time.sleep(1)
            print(f" Check-in if account is valid \033[1;0m")            
            try:
                ree = session.get('https://x.prod.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8').text 
                ua=random.choice(ug)
                head = {
                'User-Agent': ua,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Content-Type': 'application/x-www-form-urlencoded',
                'cache-control': 'max-age=0',
                'dpr': '2',
                'viewport-width': '980',
                'sec-ch-prefers-color-scheme': 'dark',
                'upgrade-insecure-requests': '1',
                'origin': 'https://mbasic.facebook.com',
                'x-requested-with': 'mark.via.gp',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
            }
            
                data = {
                'lsd': lsd,
                'jazoest': jazoest,
                'li': 'djalZs-Slr4WUsrUKuYtMQPG',
                'try_number': '0',
                'unrecognized_tries': '0',
                'email': m,
                'pass': pas,
                'login': 'Log in',
                'bi_xrwh': '92004344361786634',
            }
            
                
                url = "https://mbasic.facebook.com/login/device-based/regular/login/?next=https://mbasic.facebook.com/settings/account/&refsrc=deprecated&lwv=100&ref=dbl"
                try:
                    req = session.post(url, cookies={"cookie": ck}, headers=head, data=data)
                    req.raise_for_status()                   
                except requests.RequestException as e:                  
                    continue
                c = '; '.join([str(x) + "=" + str(y) for x, y in session.cookies.get_dict().items()])                 

                
                if "Confirm your account" in str(req.content):
                    uid=re.search("c_user=(\d+)",str(c)).group(1)                  
                    print(f"\033[1;32m [Successful] {m}|{pas}\033[1;0m")
                    print(f" [User id = {uid}\033[1;0m")                            
                    c = '; '.join([str(x) + "=" + str(y) for x, y in session.cookies.get_dict().items()])           
                    print(f" [Cookie_Data]= {c}")                    
                    ok.append(m)              
                    open(f"SSN_CREATE_USA_LOGS.txt","a").write(f"{uid}|{m}{pas}\n")  
                elif  "We need more information" in str(req.content) or "We're working on getting this fixed as soon as we can." in  str(response.content):                
                    print(f"\033[1;91m.[Checkpoint] {m}|{pas}\033[1;0m")
            except requests.RequestException as e:               
                continue                


import requests
import re
import time
import os
from bs4 import BeautifulSoup as bs

os.system('clear')
session = requests.session()
"""mail server created by me"""
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 13; 23106RN0DA Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'x-requested-with': 'XMLHttpRequest',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://10minutemail.net/m/?lang=en',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

def get_email_session():
    url = bs(session.get('https://10minutemail.net/m/?lang=en', headers=headers, allow_redirects=True).content, 'html.parser')
    email_session = re.search('sessionid="(.*?)"', str(url)).group(1)
    return email_session

def get_temporary_email(email_session):
    time_ = str(time.time()).replace('.', '')[:13]
    dat = {'new': '1', 'sessionid': email_session, '_': time_}
    pos = session.post('https://10minutemail.net/address.api.php', data=dat, headers=headers, allow_redirects=True).json()
    email = pos['mail_get_mail']
    return email

def countdown_timer(seconds):
    for remaining in range(seconds, 0, -1):
        mins, secs = divmod(remaining, 60)
        timeformat = f'{mins:02}:{secs:02}'
        print(f"\rWaiting... for code - {timeformat}", end='', flush=True)
        time.sleep(1)
    print(f"\rTime Swap {remaining+1}            ")

def fetch_confirmation_code(email_session):
    cookie_email = '; '.join([str(x) + "=" + str(y) for x, y in session.cookies.get_dict().items()])
    check_interval = 10  
    total_wait_time = 60  
    elapsed_time = 0

    while elapsed_time < total_wait_time:
        time_ = str(time.time()).replace('.', '')[:13]
        dat = {'new': '1', 'sessionid': email_session, '_': time_}
        p = session.post('https://10minutemail.net/address.api.php', data=dat, headers=headers, cookies={'cookie': cookie_email}, allow_redirects=True).json()
        if p["mail_list"]:
            mail_id = p["mail_list"][0]["mail_id"]
            params = {
                'mailid': f'{mail_id}',
                'sessionid': f'{email_session}',
            }
            response = session.get('https://10minutemail.net//mail.api.php', params=params, cookies={"cookie": cookie_email}, headers=headers)
            cont = response.content.decode('utf-8')

            if 'registration@facebookmail.com' in cont:
                pattern = re.compile(r'FB-\d+')
                match = pattern.search(cont)
                
                if match:
                    return match.group(0)
       
        countdown_timer(check_interval)
        elapsed_time += check_interval

    return None

def mail():
    email_session = get_email_session()
    email = get_temporary_email(email_session)
    print(f'\033[1;32m mail - {email}\033[1;0m')
    print(" waiting for confirmation code from - " + email + "\033[1;0m")
    
    confirmation_code = fetch_confirmation_code(email_session)
    
    if confirmation_code:
        
        cof=confirmation_code[3:]
        print(f"\033[1;93m Confirmation Code : {cof}\033[1;0m")
       
    else:
        print("No code or email is not from registration@facebookmail.com")



main()
