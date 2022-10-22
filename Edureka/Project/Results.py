from distlib.compat import raw_input
from googlesearch import search

ip=raw_input("What would you like to search for? ")

for url in search(ip, stop=10):
     print(url)