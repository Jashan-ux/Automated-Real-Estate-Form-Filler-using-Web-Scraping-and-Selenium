import requests
from bs4 import BeautifulSoup
from form_filler import FormFiller



def clean_price(price_string):
    if "$" in price_string:
        result = ""
        for char in price_string:
            if char.isdigit() or char in "$,":  #here we keep dollar sign , digit and commmas. okayy!
                result += char
            else:
                break  
        return result
    return None


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url = " https://appbrewery.github.io/Zillow-Clone/" , headers= headers)

soup =BeautifulSoup(response.text , "lxml")

prices = soup.find_all(name ="span" ,class_ = "PropertyCardWrapper__StyledPriceLine")

rent_prices = []
for price in prices :
    rent_prices.append(clean_price(price.text))
# print(rent_prices)

links = soup.find_all(name = "a" , class_ ="StyledPropertyCardDataArea-anchor")
add_links = [link.get('href') for link in links]
# print(add_links)

addresses = soup.find_all(name= "address")
cleaned_addresses = [
    ' '.join(address.text.replace('|', '').strip().split())  #Remove pipes |, stripping whitespace,and deleting unneceesary  spaces
    for address in addresses
]
# print(cleaned_addresses)

listings = {
    f"property_{i+1}": {"price": price, "address": address, "link": link}
    for i, (price, address, link) in enumerate(zip(rent_prices, cleaned_addresses, add_links))
    if price and address and link
}
# enumerate(zip()) makes the tuple of by taking elemnts from 3 lists..
# print(listings)


bot = FormFiller("https://forms.gle/z8FedgnyJQxm6qCk7")
try:
    
    bot.fill_multiple_forms(listings)
    bot.open_spreadsheet()
finally:
   
    bot.close_driver()

    



