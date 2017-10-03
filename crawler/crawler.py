import sqlite3
import sys
import time

import bs4
import requests

from database.dbase import create_table, data_entry, get_language_name


# parses article links for text
def get_text(link):
    url = requests.get(link)
    try:
        url.raise_for_status()
    except Exception as exc:
        print('There was a problem: %s' % exc)

    output_text = ''
    main_url_soup = bs4.BeautifulSoup(url.text, "html.parser").find_all('p')
    for f in main_url_soup:
        output_text += str(f.get_text())
    return output_text


# crawls wikipedia for keyword and returns data in lists
def get_all_languages(keyword):
    base_url = 'https://en.wikipedia.org/wiki/'
    keys = []
    links = []
    texts = []
    lang_codes = []
    lang_names = []

    # delay for harmful crawling = + 1s
    time.sleep(1.5)
    main_url = base_url + keyword
    url = requests.get(main_url)
    url.raise_for_status()
    keys.append(keyword)
    # base article (english) to database input lists
    links.append(main_url)
    lang_codes.append('en')
    lang_names.append('english')
    texts.append(get_text(main_url))
    print(keyword + ' -> English language processed')
    # other languages articles to database input lists
    language_soup = bs4.BeautifulSoup(url.text, "html.parser").find_all("a", class_="interlanguage-link-target")
    for i in language_soup:
        # crawling delay for other languages
        time.sleep(1.5)
        # if language in language code base
        try:
            lang_name = get_language_name(i.get('lang'))
        except TypeError:
            print('WARNING: language code: ' + i.get('lang') + ' not found.')
            continue
        lang_names.append(lang_name)
        link = i.get('href')
        links.append(link)
        texts.append(str(get_text(link)))
        lang_codes.append(i.get('lang'))
        print(keyword + ' -> ' + lang_name + ' language processed')
    return links, texts, lang_codes, lang_names, keys


with open("crawler/keywords.txt") as file:
    keywords = [line.strip() for line in file]
create_table()
for keyword in keywords:
    try:
        links, texts, lang_codes, lang_names, keys = get_all_languages(keyword)
        data_entry(links, texts, lang_codes, lang_names, keys)
    except sqlite3.OperationalError as sqlerr:
        message = 'ERROR: %s. Migrate language codes by running language_loader.py' % sqlerr
        with open("Log.txt", "a") as text_file:
            text_file.write(message + '\n')
        sys.exit(message)

    except requests.HTTPError as exc:
        message = 'There was a problem: %s' % exc
        print(message)
        with open("Log.txt", "a") as text_file:
            text_file.write(message + '\n')
        continue
