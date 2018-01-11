import requests
from bs4 import BeautifulSoup
import time

def continue_crawl(search_history, target_url):
	if search_history[-1] == target_url:
		print("We've found the target article!")
		return False
	elif len(search_history) > 25: # 25 is the max steps we set
		print("The search has gone on suspiciously long, aborting search!")
		return False
	elif search_history[-1] in search_history[:-1]:
		print("We've been in a cycle, giving up search!")
		return False
	else:
		return True

def find_first_link(url):
	# access the last article in article chain
	response = requests.get(url[-1])
	# download the content of the last article
	html_content = response.text
	# partse the content
	parsed_html = BeautifulSoup(html_content, 'html.parser')
	# locate the first link or set it to None
	


while continue_crawl(article_chain, target_url):
	# download html of last article in article chain
	# find the first link in that html
	first_link = find_first_link(article_chain[-1])
	# add the first link to article_chain
	article_chain.append(first_link)
	# pause for two seconds
	time.sleep(2)