from article_downloader import download_article
from article_processor import process_article

def main():
    # Read the URLs from your text file (replace with actual file path)
    with open("news_urls.txt", "r") as file:
        urls = file.read().splitlines()

    for i, url in enumerate(urls, start=1):
        article_text = download_article(url)
        if article_text:
            processed_text = process_article(article_text)
            if processed_text:
                filename = f"Data/processed/article_{i}.txt"
                with open(filename, "w", encoding="utf-8") as article_file:
                    article_file.write(processed_text)
                print(f"Article {i} processed and saved to {filename}.")
            else:
                print(f"Failed to process article {i} from {url}.")
        else:
            print(f"Failed to download article {i} from {url}.")

if __name__ == "__main__":
    main()
