import requests
from bs4 import BeautifulSoup

def continue_crawl(search_history, target_url):
	if search_history[-1] == target_url:
		print("We've found the target article!")
		return False
	elif len(search_history) > 25: # 25 is the max steps we set
		print("The search has gone on suspiciously long, give up the search!")
		return False
	elif search_history[-1] in search_history[:-1]:
		print("We've been in a cycle, give up the search!")
		return False
	else:
		return True


while continue_crawl(search_history, target_url):
	pass