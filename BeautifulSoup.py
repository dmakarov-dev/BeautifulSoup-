import requests
from bs4 import BeautifulSoup

# Replace 'https://example.com' with the URL of the website you want to render
url = 'https://example.com'

try:
    # Make an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Print the title of the page
        title = soup.title.string
        print(f'Title: {title}')

        # You can do more with the parsed HTML, such as extracting links, text, etc.
        # For example, print all the links on the page
        links = soup.find_all('a')
        print('\nLinks:')
        for link in links:
            print(link.get('href'))

    else:
        print(f'Failed to retrieve the page. Status code: {response.status_code}')

except Exception as e:
    print(f'An error occurred: {e}')
