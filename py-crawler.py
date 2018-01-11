import requests
from bs4 import BeautifulSoup
import time
import urllib

start_url = "https://en.wikipedia.org/wiki/Special:Random"
target_url = "https://en.wikipedia.org/wiki/Philosophy"
article_chain = [start_url]

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
	response = requests.get(url)
	# download the content of the last article
	html_content = response.text
	# partse the content
	soup = BeautifulSoup(html_content, 'html.parser')
	content_div = soup.find(id='mw-content-text').find(class_='mw-parser-output')
	# locate the first link or set it to None
	first_relative_link = None

	for element in content_div.find_all('p', recursive = False):
		if element.find('a', recursive = False):
			first_relative_link = element.find("a", recursive=False).get('href')
			break

	if not first_relative_link:
		return

	# build a full url from the relative link url
	first_link = urllib.parse.urljoin('https://en.wikipedia.org/', first_relative_link)

	return first_link

while continue_crawl(article_chain, target_url):
	print(article_chain[-1])
	# download html of last article in article chain
	# find the first link in that html
	first_link = find_first_link(article_chain[-1])
	if not first_link:
		print("We've arrived at an article with no links, aborting search!")
		break
	# add the first link to article_chain
	article_chain.append(first_link)
	# pause for two seconds
	time.sleep(2)