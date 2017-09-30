import time
import bs4
import requests

from dbase import create_table, data_entry, get_language_name


# creates wikipedia urls with keywords
def url_constructor(main_url, keywords):
    articles = []
    for word in keywords:
        current_article = main_url + word
        articles.append(current_article)
    return articles


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


def get_all_languages(articles):
    for article in articles:
        url = requests.get(article)
        try:
            url.raise_for_status()
        except Exception as exc:
            print('There was a problem: %s' % exc)

        language_soup = bs4.BeautifulSoup(url.text, "html.parser").find_all("a", class_="interlanguage-link-target")
        links = []
        texts = []
        lang_codes = []
        lang_names = []
        for i in language_soup:
            time.sleep(1.5)
            try:
                lang_name = get_language_name(i.get('lang'))
            except TypeError:
                print('WARNING: language code: ' + i.get('lang').capitalize + ' not found.')
                continue
            lang_names.append(lang_name)
            link = i.get('href')
            links.append(link)
            texts.append(str(get_text(link)))
            lang_codes.append(i.get('lang'))
            print(lang_name + ' language processed')
        create_table()
        data_entry(links, texts, lang_codes, lang_names)
        print(str(article) + ' processed')


with open("keywords.txt") as file:
    keywords = [line.strip() for line in file]
main_url = 'https://en.wikipedia.org/wiki/'
articles = url_constructor(main_url, keywords)
get_all_languages(articles)
