
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()

from bs4 import BeautifulSoup
import requests
url = 'https://www.google.com.pk/search?q=dall%20latitude'
source = requests.get(url)
plain_text = source.text
# print plain_text
soup = BeautifulSoup(plain_text, "lxml")
for li in soup.findAll('a', {'id': 'fprsl'}):
    title = li.text.strip()
    print li
    print title
