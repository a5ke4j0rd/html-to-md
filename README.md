# Converter HTML to Markdown
![Header image](https://github.com/a5ke4j0rd/html-to-md/blob/main/logo.jpg)

Easily convert your website to a Markdown file. Very useful if you need to outline articles for GitHub or other applications that support Markdown styles. 
The application was written using the markdownify library by @matthewwithanm

## Usage

Exemple:

```bash
python main.py https://en.wikipedia.org/wiki/Burzum -o burzum.md
```

### Options

- `url` -> URL page to convert
  
- `-h, --help` -> show this help message and exit
  
- `-o` OUTPUT, `--output` OUTPUT -> Output file name (default: output.md)
  

---

## Requirements

- `beautifulsoup4==4.13.3`
- `bs4==0.0.2`
- `certifi==2025.1.31`
- `charset-normalizer==3.4.1`
- `idna==3.10`
- `lxml==5.3.1`
- `markdownify==1.1.0`
- `requests==2.32.3`
- `six==1.17.0`
- `soupsieve==2.6`
- `typing_extensions==4.12.2`
- `urllib3==2.3.0`

## License

MIT

## Author

Askefjord
