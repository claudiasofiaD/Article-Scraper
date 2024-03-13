# The Python class FileManager consists of two methods: openFile() and writeFile(). 
# The openFile() method reads URLs from a file named “news_urls.txt” and returns them as a list.
# Meanwhile, the writeFile() method takes processed content, an index, and raw content as input. 
# It then writes the processed content to a file named “article{index + 1}.text” and the raw 
# content to a file named “raw{index + 1}.txt”.

import os

class FileManager:
    def openFile():
        with open("news_urls.txt", "r") as file:
            urls = file.read().splitlines()

        return urls
    
    def writeFile(outputFile, content, index, outputRaw, content_raw):
        with open(os.path.join(outputFile, f'article{index + 1}.text'), 'w') as content_file:
            content_file.write(content)

        with open(os.path.join(outputRaw, f'raw{index + 1}.txt'), 'w') as raw_file:
            raw_file.write(content_raw)