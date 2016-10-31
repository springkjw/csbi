# -*- coding: utf-8 -*-
import requests
import re

from bs4 import BeautifulSoup


def publication_c():
    # journal
    j_lists_url = []
    for i in range(1, 7):
        list_url = "http://csbi.kaist.ac.kr/pub/index.php?page=" + str(i) + "&mode=plist&tp=1&st=1&sk="
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }
        list_source_code = requests.get(list_url, headers=headers)
        list_plain_text = list_source_code.text
        list_soup = BeautifulSoup(list_plain_text, "html.parser")

        list = list_soup.findAll('a', href=re.compile("index.php\?mode=pview"))

        for item in list:
            j_lists_url.append(item.get('href'))

    for item in j_lists_url:
        serializer_c(item, 'journal')

    # patents
    p_lists_url = []
    for i in range(1, 2):
        list_url = "http://csbi.kaist.ac.kr/pub/index.php?page=" + str(i) + "&mode=plist&tp=2&st=1&sk="
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }
        list_source_code = requests.get(list_url, headers=headers)
        list_plain_text = list_source_code.text
        list_soup = BeautifulSoup(list_plain_text, "html.parser")

        list = list_soup.findAll('a', href=re.compile("index.php\?mode=pview"))

        for item in list:
            p_lists_url.append(item.get('href'))

    for item in p_lists_url:
        serializer_c(item, 'patents')

    # conference
    c_lists_url = []
    for i in range(1, 5):
        list_url = "http://csbi.kaist.ac.kr/pub/index.php?page=" + str(i) + "&mode=plist&tp=3&st=1&sk="
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }
        list_source_code = requests.get(list_url, headers=headers)
        list_plain_text = list_source_code.text
        list_soup = BeautifulSoup(list_plain_text, "html.parser")

        list = list_soup.findAll('a', href=re.compile("index.php\?mode=pview"))

        for item in list:
            c_lists_url.append(item.get('href'))

    for item in c_lists_url:
        serializer_c(item, 'conference')

    # book
    b_lists_url = []
    for i in range(1, 2):
        list_url = "http://csbi.kaist.ac.kr/pub/index.php?page=" + str(i) + "&mode=plist&tp=4&st=1&sk="
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }
        list_source_code = requests.get(list_url, headers=headers)
        list_plain_text = list_source_code.text
        list_soup = BeautifulSoup(list_plain_text, "html.parser")

        list = list_soup.findAll('a', href=re.compile("index.php\?mode=pview"))

        for item in list:
            b_lists_url.append(item.get('href'))

    for item in b_lists_url:
        serializer_c(item, 'book')


def serializer_c(url_c, type_c):
    url = "http://csbi.kaist.ac.kr/pub/" + str(url_c)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    source_code = requests.get(url, headers=headers)
    plain_text = source_code.text

    soup = BeautifulSoup(plain_text, "html.parser")

    # get_title
    title = soup.find(text="Title")
    title_td_tag = title.parent
    title_ = title_td_tag.findNext('td').findNext('td').contents[0]

    # get_author
    author = soup.find(text="Author")
    author_td_tag = author.parent
    author_ = author_td_tag.findNext('td').findNext('td').contents[0]
    author_r = author_.split(',')

    # get_year
    year = soup.find(text="Year of Pub. ")
    year_td_tag = year.parent
    year_ = year_td_tag.findNext('td').findNext('td').contents[0]

    # get_type
    if type_c == 'journal':
        search = re.compile('Journal')
    elif type_c == 'patents':
        search = re.compile('Patents')
    elif type_c == 'conference':
        search = re.compile('Conference')
    elif type_c == 'book':
        search = re.compile('Book Chapter')

    type = soup.findAll(text=search)
    type_td_tag = type[1].parent
    type_content_ = type_td_tag.findNext('td').findNext('td').contents[0]

    obj = {
        "title": title_,
        "author": author_,
        "author_r": author_r,
        "year": year_,
        "type": type_c,
        "type_content": type_content_,
    }

    if type_c == 'journal':
        instance = Publication.objects.get_or_create(
            type=obj['type'],
            title=obj['title'],
            author=obj['author'],
            year=obj['year'],
            journal=obj['type_content'],
        )
    elif type_c == 'patents':
        instance = Publication.objects.get_or_create(
            type=obj['type'],
            title=obj['title'],
            author=obj['author'],
            year=obj['year'],
            patent=obj['type_content'],
        )
    elif type_c == 'conference':
        try:
            instance = Publication.objects.get_or_create(
                type=obj['type'],
                title=obj['title'],
                author=obj['author'],
                year=obj['year'],
                conference=obj['type_content'],
            )
        except:
            instance = Publication.objects.get_or_create(
                type=obj['type'],
                title=obj['title'],
                author=obj['author'],
                year=obj['year'],
            )
    elif type_c == 'book':
        instance = Publication.objects.get_or_create(
            type=obj['type'],
            title=obj['title'],
            author=obj['author'],
            year=obj['year'],
            book=obj['type_content'],
        )
