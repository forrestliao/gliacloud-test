from bs4 import BeautifulSoup
from selenium.webdriver import Chrome, ChromeOptions
from configparser import ConfigParser


def get_content(main_content, time):
    content = main_content.text.split(time)[1].split("--")[0].strip()
    content = content.replace('%', '{mod}')
    return content



def parserArticle(board_name, article_id, browser):
    browser.get("https://www.ptt.cc/bbs/%s/%s.html" % (board_name, article_id))
    soup = BeautifulSoup(browser.page_source, "html.parser")

    config_parser = ConfigParser()
    config_parser[article_id] = {}
    time = ""
    for idx, article_mete_value in enumerate(soup.find_all('span', attrs={"class":"article-meta-value"})):

        if idx == 0:
            config_parser[article_id]["Author"] = article_mete_value.text
        elif idx == 1:
            config_parser[article_id]["Board"] = article_mete_value.text
        elif idx == 2:
            config_parser[article_id]["Title"] = article_mete_value.text
        elif idx == 3:
            config_parser[article_id]["Date"] = article_mete_value.text
            time =article_mete_value.text

    main_content = soup.find('div', attrs={'id': 'main-content'})
    config_parser[article_id]["Content"] = get_content(main_content, time)

    with open("Inis/%s.ini" % article_id, 'w', encoding='UTF-8') as f:
        config_parser.write(f)


if __name__ == '__main__':
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    browser = Chrome("chromedriver.exe", chrome_options=chrome_options)

    parserArticle('car', 'M.1552965005.A.9AA', browser)
    browser.close()