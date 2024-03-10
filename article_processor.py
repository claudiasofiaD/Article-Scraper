def process_article(raw_text):
    """
    Processes the raw article text to extract only the article content.

    Args:
        raw_text (str): The raw article text.

    Returns:
        str: Processed article content or None if processing fails.
    """
    try:
        paragraphs = raw_text.split("\n\n")  # Split by paragraphs
        article_content = "\n\n".join(p for p in paragraphs if "by " not in p.lower())
        return article_content.strip()  # Remove leading/trailing whitespace
    except Exception as e:
        print(f"Error processing article: {e}")
        return None
