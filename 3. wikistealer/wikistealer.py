import os
from pathlib import Path
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
    :return: list of src for each img in soup
    """
    images = soup.find_all('img')
    return [img['src'] for img in images]


def create_word_dir(word: str):
    """
    :param word: the searched word
    :return: the dir path of the current search of the word
    """
    Path(f"results/{word}").mkdir(exist_ok = True)
    current_time = datetime.datetime.now()
    format_time = current_time.strftime("%Y-%m-%d %H-%M-%S")
    images_path = f"results/{word}/{format_time}"
    os.mkdir(images_path)
    return images_path


def check_https(url: str):
    """
    :param url: url to check
    :return: url starting with https:// 
    """
    if url.startswith('https://'):
        return url
    if url.startswith('//'):
        return f"https:{url}"
    if url.startswith('/'):
        return f"https://en.wikipedia.org{url}"
    return f"https://{url}"


def insert_images(images_src: list[str], path: str):
    """
    :param images_src: list of src of all images in page
    :param path: path to write img files to
    """
    for img_src in images_src:
        valid_src = check_https(img_src)
        search_img = requests.get(valid_src)
        img_content = search_img.content
        img_name = img_src.split('/')[-1].replace('?','')
        with open(f"{path}/{img_name}",'wb') as f:
            f.write(img_content)
                

def wikistealer():
    input_word = input('Search a word: ')
    soup = wiki_search_word(input_word)
    images_info = img_extractor(soup)
    path = create_word_dir(input_word)
    insert_images(images_info, path)


wikistealer()
