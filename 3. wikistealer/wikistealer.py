import os
import datetime
import requests
from bs4 import BeautifulSoup


def wiki_search_word(word: str):
    """
    :param word: word to search for in wikipedia
    :return: soup for the searched word
    """
    response = requests.get(f"https://en.wikipedia.org/wiki/{word}")
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


def img_extractor(soup):
    """
    :param soup: soup to extract imgs from
    :return: list of (alt, src) for each img in soup
    """
    images = soup.find_all('img')
    return [(img['alt'], img['src']) for img in images]


def create_word_dir(word):
    """
    :param word: the searched word
    :return: the dir path of the current search of the word
    """
    os.mkdir(word)
    current_time = datetime.datetime.now()
    format_time = current_time.strftime("%Y-%m-%d %H-%M-%S")
    images_path = f"{word}/{format_time}"
    os.mkdir(images_path)
    return images_path


def wikistealer():
    input_word = input('Search a word: ')
    soup = wiki_search_word(input_word)
    images_info = img_extractor(soup)
    create_word_dir(input_word)


wikistealer()
