# Import libraries
from bs4 import BeautifulSoup, SoupStrainer
import requests
import validators

# Prompt user to enter the URL
url = input("Enter your url: ")

# Make a request to get the URL
page = requests.get(url)

# Get the response code of given URL
response_code = str(page.status_code)


# Display the text of the URL in str
data = page.text

# Use BeautifulSoup to use the built-in methods
soup = BeautifulSoup(data)

# Iterate over all links on the given URL with the response code next to it
for link in soup.find_all('a'):
    # print(f"Url: {link.get('href')} " + f"| Status Code: {response_code}"+ f"| Name: {link.contents[0]}")

    print(link.get('href'))

    URL =link.get('href')

    try:
        response = requests.head(URL)
    except Exception as e:
        print(f"NOT OK: {str(e)}")
    else:
        if response.status_code == 200:
            print("200")
        else:
            print(f"NOT OK: HTTP response code {response.status_code}")
    #
    try:
        print(link.contents[1])
    except:
        print(link.contents[0])