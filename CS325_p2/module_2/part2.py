# Fetcher fetches HTML content from a given URL. It sends an HTTP request and 
# returns the response text or None if unsuccessful.

# Extractor: Contains two static methods:
# ArticleExtractor(html): Parses an HTML string using newspaper.Article, extracts the article text, and returns it.
# RawArticleExtractor(html): Currently identical to ArticleExtractor, but can be customized differently.

# Scrapper: has two static methods:
# article(url): Fetches HTML content, extracts the article text using ArticleExtractor, and returns it.
# rawArticle(url): Similar to article, but uses RawArticleExtractor.

import requests
import newspaper

class Fetcher:
    @staticmethod
    def fetch(url):
        response = requests.get(url)
        if response:
            return response.text
        else:
            print(f"Failed to fetch URL: {url}")
            return None

class Extractor:
    @staticmethod
    def ArticleExtractor(html):
        article = newspaper.Article('')
        article.set_html(html)
        article.parse()
        return article.text

    @staticmethod
    def RawArticleExtractor(html):
        # You can use the same method as ArticleExtractor
        return Extractor.ArticleExtractor(html)

class Scrapper:
    @staticmethod
    def article(url):
        html = Fetcher.fetch(url)
        if html:
            return Extractor.ArticleExtractor(html)
        else:
            return None

    @staticmethod
    def rawArticle(url):
        html = Fetcher.fetch(url)
        if html:
            return Extractor.RawArticleExtractor(html)
        else:
            return None
