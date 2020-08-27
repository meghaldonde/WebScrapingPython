import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
#print(soup.body.contents)
#print(soup.find('a'))
#print(soup.find_all('div'))
# css selector
#print(soup.select(('#score_20514755'))
#print(soup.select('.score'))
links = soup.select('.storylink')
votes = soup.select('.score')
subtext = soup.select('.subtext')

links2 = soup2.select('.storylink')
votes2 = soup2.select('.score')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_stories_by_votes(hnlist):
	return sorted(hnlist, key = lambda k:k['votes'], reverse = True)


def create_custom_hacker_news(links, subtext):
	hn=[]
	for index, item in enumerate(links):

		title = links[index].getText()
		href=links[index].get('href',None)
		vote = subtext[index].select('.score')
		if len(vote):
			points=int(vote[0].getText().replace(' points',''))
			if points >= 100:
				
				hn.append({'title':title,'link':href,'votes':points})
	return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hacker_news(mega_links,mega_subtext))