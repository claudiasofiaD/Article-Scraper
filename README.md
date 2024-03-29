# News Article Downloader

This is a Python script that downloads and extracts the content of news articles from a list of URLs.

## Requirements

- Python 3
- newspaper3k library (`pip install newspaper3k`)

## Usage

- Create a text file with one URL per line. For example:

- Save the file as `news_urls.txt` in the same directory as the script.
- Run the script with `python news_article_downloader.py`
- The script will download and save the articles as `article_1.txt`, `article_2.txt`, etc. in the same directory.
- If an article fails to download, the script will print an error message and skip to the next URL.

## Input

- The input file `news_urls.txt` should contain valid URLs of news articles, one per line.
- The URLs should point to web pages that contain the main article text, not just headlines or summaries.
- The URLs should not be too long or contain special characters that might cause errors.

## Output

- The output files `article_1.txt`, `article_2.txt`, etc. will contain the extracted article text, without any HTML tags, images, or ads.
- The output files will have the same encoding as the input file, which is UTF-8 by default.
- The output files will have the same order as the input file, unless some articles fail to download.

## Limitations

- The script relies on the newspaper3k library to download and parse the articles, which may not work for some websites or languages.
- The script does not handle redirects, authentication, or paywalls that might prevent access to some articles.
- The script does not check for duplicates, invalid URLs, or empty lines in the input file.
- The script does not handle errors or exceptions gracefully, and may terminate abruptly if something goes wrong.
