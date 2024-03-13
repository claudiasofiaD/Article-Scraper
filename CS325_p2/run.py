# FindPath: This method sets the paths for raw and processed data directories.
# FindArticle: It retrieves a list of URLs using first.FileManager.openFile(). 
# For each URL, it fetches the article content using second.Scrapper.article(url) 
# and the raw article content using second.Scrapper.rawArticle(url). If the content
# is available, it writes it to the processed output file using first.FileManager.writeFile().

from module_1 import part1 as first
from module_2 import part2 as second
import os

class ProjectManager:
    def FindPath(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))

        self.output_raw = os.path.join(script_dir, "data", "raw")
        self.output_processed = os.path.join(script_dir, "data", "processed")

    def FindArticle(self):
        urls = first.FileManager.openFile()

        if urls:
            for index, url in enumerate(urls):
                content = second.Scrapper.article(url)
                raw_content = second.Scrapper.rawArticle(url)

                if content:
                    first.FileManager.writeFile(self.output_processed, content, index, self.output_raw, raw_content)

def main():
    obj = ProjectManager()
    obj.FindPath()
    obj.FindArticle()

if __name__ == "__main__":
    main()
