from newspaper import Article

def download_article(url):
    """
    Downloads and extracts the content of an article from the given URL.

    Args:
        url (str): The URL of the article.

    Returns:
        str: Extracted article text or None if download fails.
    """
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        print(f"Error fetching article from {url}: {e}")
        return None

if __name__ == "__main__":
    # Example usage:
    article_url = "https://www.theguardian.com/fashion/2024/feb/12/the-latest-it-bag-is-a-joke-inside-the-wacky-world-of-mschf"
    downloaded_text = download_article(article_url)
    if downloaded_text:
        print("Article downloaded successfully:")
        print(downloaded_text)
    else:
        print("Failed to download the article.")

# https://www.theguardian.com/fashion/2024/feb/12/the-latest-it-bag-is-a-joke-inside-the-wacky-world-of-mschf
# https://www.theguardian.com/wellness/2024/feb/12/dating-app-fatigue-tips
# https://www.theguardian.com/lifeandstyle/2024/feb/12/i-feel-smug-in-yoga-class-but-is-hypermobility-a-blessing-or-a-curse
# https://www.theguardian.com/fashion/2024/feb/12/the-hidden-plastics-in-our-clothes-and-how-to-avoid-them
# https://www.theguardian.com/lifeandstyle/2024/feb/13/size-inclusive-sustainable-brands-australian-fashion-professionals-share-their-favourites