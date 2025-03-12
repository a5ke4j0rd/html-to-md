from bs4 import BeautifulSoup
import requests
import markdownify


def load_html(source_url):
    response = requests.get(source_url)
    markdown = markdownify.MarkdownConverter()
    return markdown.convert_soup(BeautifulSoup(response.text, 'lxml'))


def save_to_file(markdown_text):
    filename = input('Save file as: ')
    with open(filename, 'w') as file:
        file.write(markdown_text)


if __name__ == '__main__':
    url = input('Input URL: ')
    html = load_html(url)
    save_to_file(html)
