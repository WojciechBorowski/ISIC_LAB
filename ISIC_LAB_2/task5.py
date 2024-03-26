from bs4 import BeautifulSoup
import urllib.request

source = urllib.request.urlopen('https://ielts-up.com/speaking/ielts-speaking-sample-3.html').read()

soup = BeautifulSoup(source, 'html.parser')

links = soup.find_all('a')

with open('links.txt', 'w') as l:
    for link in links:
        url = link.get('href')
        l.write(url)
        l.write("\n")



