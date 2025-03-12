import argparse
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests
import markdownify
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def load_html(source_url):
    """
    Loads the HTML code at the specified URL and converts it to Markdown.

    :param source_url: URL of the page to load
    :return: Markdown text
    """
    try:
        response = requests.get(source_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')
        markdown = markdownify.MarkdownConverter()
        return markdown.convert_soup(soup)
    except requests.RequestException as e:
        logging.error(f"Error loading URL: {e}")
        return None


def is_valid_url(url):
    """
    Checks if a string is a valid URL.

    :param url: The string to check
    :return: True if the URL is valid, False otherwise
    """
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def save_to_file(markdown_text, filename):
    """
    Saves text in Markdown format to a file.

    :param markdown_text: Text to save
    :param filename: File name to save
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(markdown_text)
        logging.info(f"File saved successfully as: {filename}")
    except IOError as e:
        logging.error(f"Error saving file: {e}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Converts HTML page to Markdown and saves to file.")
    parser.add_argument('url', type=str, help="URL page to convert")
    parser.add_argument('-o', '--output', type=str, default='output.md', help="Output file name (default: output.md)")
    args = parser.parse_args()

    if not is_valid_url(args.url):
        logging.error("Incorrect URL")
        exit(1)

    markdown_text = load_html(args.url)
    if markdown_text:
        save_to_file(markdown_text, args.output)
