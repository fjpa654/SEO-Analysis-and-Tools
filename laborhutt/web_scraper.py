import requests
from bs4 import BeautifulSoup
import csv

def scrape_homepage(url):
    # Fetch the HTML content of the home page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract all links
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.startswith('http'):
            links.append(href)

    return links

def main():
    url = "https://www.laborhutt.com/"
    links = scrape_homepage(url)

    # Write links to CSV
    with open('laborhutt_links.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Link'])
        for link in links:
            writer.writerow([link])

if __name__ == "__main__":
    main()
