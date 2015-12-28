from urlparse import urlparse

from bs4 import BeautifulSoup
import requests


def url_validate(url):
    url = urlparse(url)
    return (url.scheme + "://" + url.netloc + url.path, url.scheme + "://" + url.netloc)

def get_title(response):
    soup = BeautifulSoup(response, "html.parser")
    return soup.title.string

def entity_extraction(response):
    soup = BeautifulSoup(response, "html.parser")
    text = soup.find_all('p')
    print text
    return []
