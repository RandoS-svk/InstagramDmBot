from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random
import os
from selenium.webdriver.common.by import By

from get_users import GetUsers
# Username and password of your instagram account:
my_username = input('Instagram username: ')
#my_password = pwinput.pwinput(prompt='Instagram password: ')

my_password = input('Instagram password: ')
# Instagram username list for DM:

# Messages:
message = input('Message: ')

# Delay time between messages in sec:
between_messages = 2000

CURRENT_PATH = os.getcwd()


# Authorization:
def Main(username, password):
	try:
		browser = webdriver.Chrome(f'{CURRENT_PATH}/chromedriver')
		browser.get('https://instagram.com')
		time.sleep(random.randrange(2,4))

		browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]').click()
		time.sleep(2)
		input_username = browser.find_element('name','username')
		input_password = browser.find_element('name','password')

		input_username.send_keys(username)
		time.sleep(random.randrange(1,2))
		input_password.send_keys(password)
		time.sleep(random.randrange(1,2))
		input_password.send_keys(Keys.ENTER)
		time.sleep(10)

	except Exception as err:
		print(err)
		browser.quit()

	usernames = list()

	with open('usernames.txt', 'r') as file:
		for line in file:
			usernames.append(line.strip())
	try:
		browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button').click()
		time.sleep(10)
		browser.get('https://www.instagram.com/direct/inbox/')
		time.sleep(15)
		browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
		time.sleep(10)
		for user in usernames:
			browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/div[1]/div/div[3]/button').click()
			time.sleep(10)
			input_search = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/input')
			input_search.send_keys(user)
			time.sleep(10)
			browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[3]/button').click()
			time.sleep(10)
			browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[3]/div/button').click()
			time.sleep(10)
			chat_input = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
			chat_input.send_keys(message)
			time.sleep(12)
			chat_input.send_keys(Keys.ENTER)
			time.sleep(10)
	except Exception as err:
		print(err)
		browser.quit()

GetUsers(my_username, my_password)
Main(username=my_username, password=my_password)
