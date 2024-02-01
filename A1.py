#webscraped the files ending in .tar.gz recursively
#of the website https://ftp.gnu.org/pub/gnu/ and saved it to text.txt
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = 'https://ftp.gnu.org/pub/gnu/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

def getLinks(soup):
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.endswith('/'):
            links.append(href)
    return links

def crawlPage(url, visited, output):
    if url in visited:
        return
    visited.add(url)
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch {url}")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    content =soup.get_text()
    output.write(content)
    links = getLinks(soup)
    for link in links:
        nextUrl = urljoin(url, link)
        if 'https://ftp.gnu.org/pub/gnu/' in nextUrl:
            crawlPage(nextUrl, visited, output)    
        
if __name__ == "__main__":
    url = 'https://ftp.gnu.org/pub/gnu/'
    output_path = ('text.txt')
    visited = set()
    
    with open(output_path, 'w', encoding = 'utf-8') as outputFile:
        crawlPage(url, visited, outputFile) 
    
    print(f"Content saved to {output_path}")