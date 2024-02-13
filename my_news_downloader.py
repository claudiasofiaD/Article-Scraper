from newspaper import Article

def download_article(url):
    """ Downloads and extracts the content of an article from the given URL. """
    try:
        # Create an Article object with the URL
        article = Article(url)
        # Download and parse the article
        article.download()
        article.parse()
        # Return the article text
        return article.text
    except Exception as e:
        print(f"Error fetching article from {url}: {e}")
        return None

def main():
    # Read the URLs from your text file (replace with your actual file path)
    with open("news_urls.txt", "r") as file:
        urls = file.read().splitlines()

    # Download articles and save them to separate files
    for i, url in enumerate(urls, start=1):
        article_text = download_article(url)
        if article_text:
            with open(f"article_{i}.txt", "w", encoding="utf-8") as article_file:
                article_file.write(article_text)
            print(f"Article {i} downloaded successfully.")
        else:
            print(f"Failed to download article {i} from {url}.")

if __name__ == "__main__":
    main()
