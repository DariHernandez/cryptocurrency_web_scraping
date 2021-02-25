#! python3

import requests, bs4, pprint

# List of coint to make web scraping
coins = [
    "ethereum",
    "bitcoin",
    "tether",
    "cardano",
    "monero",
    "tron",
    "eos"
]


def get_price (coins): 
    """
    Return te price of specific criptocurrency
    """

    # Dictionary to save the retur information: name of coins and price
    dic_return = {}

    # CSS selector fo the price of the coins
    selector = "div.priceTitle___1cXUG > div"

    # Loop for each coin in the list
    for coin in coins: 

        # Create the link
        web_page = "https://coinmarketcap.com/es/currencies/" + str(coin).lower().strip()

        # Make a request for the page
        res = requests.get (web_page)
        soup = bs4.BeautifulSoup (res.text, "html.parser")

        # Get the price of the 
        price = soup.select (selector)[0].getText()

        # Save the current coin in the dictionary
        dic_return[coin] = price

    return dic_return

cyptocoins = get_price (coins)
pprint.pprint (cyptocoins)