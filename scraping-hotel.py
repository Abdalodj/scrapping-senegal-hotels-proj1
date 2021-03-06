import requests
from bs4 import BeautifulSoup
import time

links = []

for i in range(1, 24):
  url = "https://vymaps.com/SN/Dakar/hotel/" + str(i)
  response = requests.get(url)
  if response.ok:
    try:
      print('Page' + str(i))
      print(response)
      soup = BeautifulSoup(response.text, "html.parser")
      contents = soup.findAll('b')[5:-2]
      """ print(contents) """
      links += [elt.find('a')['href'] for elt in contents if elt.text != 'Email: ']
    except:
      print([elt.text for elt in contents])

  else:
    print('err')

with open('urls_hotels.txt', 'w+') as file:
  for link in links:
    file.write(link + '\n')


print(len(links))