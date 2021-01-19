from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from get_domain_name import get_random_word
import time
import random
import csv

chrome_options = Options()  
chrome_options.add_argument("--headless") 
browser = webdriver.Chrome(options=chrome_options)
url = 'https://uk.godaddy.com/domainsearch/find?checkAvail=1&domainToCheck=domainnamehellothere.com'

while True:
	print("----------------------------------")
	print("SEARCHING...")
	print("----------------------------------")

	domain_name = get_random_word()
	#domain_name = 'trcarney'

	url = 'https://godaddy.com/domainsearch/find?checkAvail=1&domainToCheck=' + domain_name + ".com"

	browser.get(url)
	time.sleep(2)
	available = ''
	try:
		available = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div/div/div[1]').text
	except:
		print('Exception Thrown')
	
	try:
		available = available.split(' ')[1].split('\n')[0]
		print(available)
		if available == 'Available' or available ==  'Domain':
			price = ''
			try:
				price = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div/div/div[2]/div[1]/div[2]/div/span[1]/div').text
			except:
				pass

			print(domain_name + ".com" + " is available!")
			if price != '' and  '$' in price:
				print('Price:', price)

			with open('domains.csv', 'a') as f:
				row = [domain_name + '.com', price]
				writer = csv.writer(f)
				writer.writerow(row)
		else:
			print(domain_name + ".com" + " is taken!")
			pass
	except:
		print(available)

	# Sleep for 35 sec so we don't go over out data limit
	print("Waiting so I don't have to pay!")
	time.sleep(35) 