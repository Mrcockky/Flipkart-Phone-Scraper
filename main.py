import requests
from bs4 import BeautifulSoup
import pandas as pd

# Headers to mimic a real browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}

for i in range(1, 7):
    url = f"https://www.flipkart.com/search?q=phone+under+10000&page={i}"
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    
    # Extracting product names
    names = soup.findAll("div", class_="_4rR01T")
    product_name = [name.text for name in names]
    
    # Extracting prices
    prices = soup.findAll("div", class_="_30jeq3 _1_WHN1")
    price_list = [price.text for price in prices]
    
    # Extracting descriptions
    descriptions = soup.findAll('ul', class_="_1xgFaf")
    desc_list = [desc.text for desc in descriptions]
    
    # Extracting overall ratings
    overall_rating = soup.findAll('div', class_="_3LWZlK")
    rating_list = [rating.text for rating in overall_rating[:len(product_name)]]  # Adjust the length to match product names
    
    # Creating the DataFrame
    df = pd.DataFrame({
        "Product name": product_name, 
        "Price": price_list, 
        "Description": desc_list, 
        "Overall rating": rating_list
    })
    
    # Saving the DataFrame to an Excel file
    df.to_excel(f"flipkart_product_list_{i}.xlsx", index=False)
    print(f"Program {i} completed")
