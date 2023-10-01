import uuid
import requests
from bs4 import BeautifulSoup

def picker(name, weight):
    id = str(uuid.uuid4())  # Generate a unique ID for this search
    results1 = pick_zepto(name, weight, id)  # Call the pick_zepto function
    results2 = pick_instamart(name, weight, id)  # Call the pick_instamart function
    return results1 + results2

def pick_zepto(name, weight, id):
    if not name:
        return []
    if not isinstance(weight, int):
        return []
    if not id:
        return []

    # Send a request to the Zepto API with the name and weight parameters
    url = 'https://www.zeptonow.com/search?query=banana+robusta'
    # query = f'{name} {weight} grams'
    # params = {'query': query}
    response = requests.get(url)
    with open('response.html', 'w') as f:
        f.write(response.content.decode())
    # Parse the response to extract the relevant information
    results = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        print(soup)
        items = soup.select('[id^="store-product-"]')
        print(items)
        grid = soup.find('div', {'class': '_3dNoiD'})
        if grid is None:
            print('Error: Could not find grid element')
            return []
        for item in items[:10]:
            print(item)
            name = item.find('div', {'class': 'vhtkim'}).text.strip()
            weight = item.find('div', {'class': 'j7HcYM'}).text.strip()
            price = item.find('div', {'class': 'j7HcYM'}).find_next_sibling('div').text.strip()
            result = {
                'name': name,
                'weight': weight,
                'price': price
            }
            results.append(result)

    return results

def pick_instamart(name, weight, id):
    if not name:
        return []
    if not isinstance(weight, int):
        return []
    if not id:
        return []
    # Your code to search for the product in Instamart goes here
    return []