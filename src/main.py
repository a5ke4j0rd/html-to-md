from bs4 import BeautifulSoup
import requests
import markdownify


def load_html(url):
    response = requests.get(url)
    markdown = markdownify.MarkdownConverter()
    return markdown.convert_soup(BeautifulSoup(response.text, 'lxml'))


# def convert_md(html_src):
#     return markdownify.markdownify(html_src)

if __name__ == '__main__':
    url = input('Input URL: ')
    html = load_html(url)
    print(html)
