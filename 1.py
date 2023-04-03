import requests
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
E = "\033[0;90m" #رمادي
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
P = '\033[1;34m' #purple

logo=f"""
{B}.d8888. {P}db      {B}d88888b {P}d88888b {B}d8888b. 
{B}88'  YP {P}88      {B}88'     {P}88'     {B}88  `8D 
{B}`8bo.   {P}88      {B}88ooooo {P}88ooooo {B}88oodD' 
  {B}`Y8b. {P}88      {B}88~~~~~ {P}88~~~~~ {B}88~~~   
{B}db   8D {P}88booo. {B}88.     {P}88.     {B}88      
{B}`8888Y' {P}Y88888P {B}Y88888P {P}Y88888P {B}88     

   {B}« {C}CODE BY Black {B}»
{P}┏{B}━━━━━━━━━━━━━━━━━━━━━━━━━━{P}┓    
{B}┃{C} ⌯ Telegram {B}› {C}@pppp8ppp {B} ┃
{P}┗{B}━━━━━━━━━━━━━━━━━━━━━━━━━━{P}┛                              
"""

print(logo)



user=str(input(X+' ⌯ username to get followers : '))
session=input(X+' ⌯ session id fake : ')
clean=input(X+' ⌯ do you want to clean the ids.txt file before adding new ids ? [y/n] : ')

if str(clean)=='y' or str(clean)=='Y':
	with open('ids.txt', 'w') as f:
		f.close()
elif str(clean)=='n' or str(clean)=='N':
	pass
else:
	print(X+'invalid input')
	exit()

try:
	id=str(requests.get(f"https://instagram.com/{user}").text.split('"profile_id":"')[1].split('"')[0])
	print(Z+f' ⌯ target id{P} : '+F+id)
except:
	print(X+'can not get your id')
	id=str(input(X+' ⌯ enter id to get followers : '))
counter=0
def scrap_big_list(next_max_id, counter):
	cookies = {
	    'sessionid': str(session),
	}
	
	headers = {
	    'authority': 'www.instagram.com',
	    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
	    'x-ig-app-id': '1217981644879628',
	    'x-ig-www-claim': 'hmac.AR21JXFX2e-KoaQwARsWvmgjpw3zdK4l6ArUdPC5An9POOz8',
	    'sec-ch-ua-mobile': '?1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.46 Mobile Safari/537.36',
	    'viewport-width': '393',
	    'accept': '*/*',
	    'x-csrftoken': 'biZW097YUwShj5LbUyY8rITHUR7pLviR',
	    'x-requested-with': 'XMLHttpRequest',
	    'x-asbd-id': '198387',
	    'sec-ch-prefers-color-scheme': 'dark',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-dest': 'empty',
	    'referer': f'https://www.instagram.com/{user}/followers/',
	    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
	}
	
	params = {
	    'count': '100',
	    'max_id': str(next_max_id),
	    'search_surface': 'follow_list_page',
	}
	
	response = requests.get(
	    f'https://www.instagram.com/api/v1/friendships/{id}/followers/',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	)
	if not "Please wait a few minutes before trying again." in response.text:
		if response.json()['users']:
			if response.json()['users']!=[]:
				users=response.json()['users']
				ids_list=[]
				for usr in users:
					counter+=1
					idd=str(usr['pk'])
					print(X+'['+Z+str(counter)+X+']'+P+' : '+F+idd)
					ids_list.append(str(idd))
				with open('ids.txt', 'a') as f:
					for iddd in ids_list:
						f.write(str(iddd)+'\n')
					f.close()
					ids_list=[]
				if response.json()['big_list']==True and response.json()['next_max_id']:
					next_max_id=str(response.json()['next_max_id'])
					scrap_big_list(next_max_id, counter)
				else:
					print(X+'finished saved '+str(counter)+' id in ids.txt')
			else:
				print(X+'can not scrap ids.')
	else:
		print(Z+'You are blocked, please use a VPN to change your IP and try again.')
		exit()



cookies = {
    'sessionid': str(session),
}

headers = {
    'authority': 'www.instagram.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
    'x-ig-app-id': '1217981644879628',
    'x-ig-www-claim': 'hmac.AR21JXFX2e-KoaQwARsWvmgjpw3zdK4l6ArUdPC5An9PONOS',
    'sec-ch-ua-mobile': '?1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.46 Mobile Safari/537.36',
    'viewport-width': '393',
    'accept': '*/*',
    'x-csrftoken': 'biZW097YUwShj5LbUyY8rITHUR7pLviR',
    'x-requested-with': 'XMLHttpRequest',
    'x-asbd-id': '198387',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': f'https://www.instagram.com/{user}/followers/',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

params = {
    'count': '100',
    'search_surface': 'follow_list_page',
}

response = requests.get(
    f'https://www.instagram.com/api/v1/friendships/{id}/followers/',
    params=params,
    cookies=cookies,
    headers=headers,
)
try:
	response.json()
except ValueError:
	print(Z+'invalid SessionId, please make sure then the SessionId is valid and try again.')
	exit()
if not "Please wait a few minutes before trying again." in response.text:
	if response.json()['users']!=[]:
		users=response.json()['users']
		ids_list=[]
		for usr in users:
			counter+=1
			idd=str(usr['pk'])
			print(X+'['+Z+str(counter)+X+']'+P+' : '+F+idd)
			ids_list.append(str(idd))
			with open('ids.txt', 'a') as f:
				for iddd in ids_list:
					f.write(str(iddd)+'\n')
				f.close()
			ids_list=[]
		if response.json()['big_list']==True and response.json()['next_max_id']:
			next_max_id=str(response.json()['next_max_id'])
			scrap_big_list(next_max_id, counter)
		else:
			print(X+'finished saved '+str(counter)+' id in ids.txt')
	else:
		print(X+'can not scrap ids.')
else:
	print(Z+'You are blocked, please use a VPN to change your IP and try again.')
	exit()