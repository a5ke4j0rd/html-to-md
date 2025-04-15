import argparse
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests
import markdownify
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')


def load_html(source_url):
    """
    Loads HTML content from the specified URL and converts it to Markdown format.

    Args:
        source_url: URL of the web page to fetch and convert

    Returns:
        Converted Markdown content if successful, None otherwise

    Raises:
        ValueError: If the provided URL is empty
    """
    if not source_url:
        raise ValueError("URL cannot be empty")

    try:
        response = requests.get(source_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')
        markdown = markdownify.MarkdownConverter()
        return markdown.convert_soup(soup)
    except requests.RequestException as e:
        logging.error(f"Error loading URL: {e}")
        return None
    except Exception as e:
        logging.error(f"Unexpected error during conversion: {e}")
        return None


def is_valid_url(url):
    """
    Validates whether the given string is a properly formatted URL.

    Args:
        url: String to validate as URL

    Returns:
        True if the URL is valid, False otherwise
    """
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False
    except Exception as e:
        logging.error(f"URL validation error: {e}")
        return False


def save_to_file(markdown_src, filename):
    """
    Saves Markdown formatted text to a specified file.

    Args:
        markdown_src: Markdown content to save
        filename: Destination file path

    Raises:
        IOError: If file writing operation fails
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(markdown_src)
        logging.info(f"File saved successfully as: {filename}")
    except IOError as e:
        logging.error(f"Error saving file: {e}")
    except Exception as e:
        logging.error(f"Unexpected file save error: {e}")


def main():
    """
    Main execution function that handles command line arguments and orchestrates
    the HTML to Markdown conversion process.
    """
    parser = argparse.ArgumentParser(
        description="Converts HTML page to Markdown and saves to file."
    )
    parser.add_argument('url', help="URL page to convert")
    parser.add_argument(
        '-o', '--output',
        default='output.md',
        help="Output file name (default: output.md)"
    )
    args = parser.parse_args()

    if not is_valid_url(args.url):
        logging.error("Incorrect URL")
        exit(1)

    markdown_text = load_html(args.url)
    if markdown_text:
        save_to_file(markdown_text, args.output)
    else:
        logging.error("Failed to convert HTML to Markdown")
        exit(1)


if __name__ == '__main__':
    main()
