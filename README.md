
### Flipkart Phone Scraper 

#### Overview

This script scrapes phone product information from Flipkart for phones priced under 10000 INR. It collects product names, prices, descriptions, and overall ratings from multiple pages and saves the data to Excel files.

#### Table of Contents

1.  [Requirements](#requirements)
2.  [Installation](#installation)
3.  [Usage](#usage)
4.  [Script Details](#script-details)
    -   [Imports](#imports)
    -   [Headers](#headers)
    -   [Main Loop](#main-loop)
    -   [Data Extraction](#data-extraction)
    -   [Create DataFrame](#create-dataframe)
    -   [Save to Excel](#save-to-excel)
5.  [Notes](#notes)
6.  [Troubleshooting](#troubleshooting)
7.  [Contribution](#contribution)

#### Requirements

-   Python 3.x
-   `requests` library
-   `beautifulsoup4` library
-   `pandas` library
-   `lxml` parser

#### Installation

1.  Ensure Python 3.x is installed on your system.
2.  Install required libraries using pip:
    
    bash
    
    Copy code
    
    `pip install requests beautifulsoup4 pandas lxml` 
    

#### Usage

1.  Run the script using Python:
    
    `python flipkart_phone_scraper.py` 
    

#### Script Details

The script fetches the first 6 pages of search results for phones under 10000 INR on Flipkart. For each page, it extracts:

-   **Product Name**
-   **Price**
-   **Description**
-   **Overall Rating**

The extracted data is saved into separate Excel files for each page.

##### Imports


`import requests
from bs4 import BeautifulSoup
import pandas as pd` 

##### Headers

Define headers to mimic a browser request.

`headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}` 

##### Main Loop

Loop through the first 6 pages of search results.

`for i in range(1, 7):
    url = f"https://www.flipkart.com/search?q=phone+under+10000&page={i}"
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')` 

##### Data Extraction

Extract product names, prices, descriptions, and overall ratings.

-   **Product Names**:
    
    `names = soup.findAll("div", class_="_4rR01T")
    product_name = [name.text for name in names]` 
    
-   **Prices**:
    
    `prices = soup.findAll("div", class_="_30jeq3 _1_WHN1")
    price_list = [price.text for price in prices]` 
    
-   **Descriptions**:
    
    `descriptions = soup.findAll('ul', class_="_1xgFaf")
    desc_list = [desc.text for desc in descriptions]` 
    
-   **Overall Ratings**:
  
    `overall_rating = soup.findAll('div', class_="_3LWZlK")
    rating_list = [rating.text for rating in overall_rating[:len(product_name)]]  # Match the length to product names` 
    

##### Create DataFrame

Organize data into a DataFrame.

`df = pd.DataFrame({
    "Product name": product_name, 
    "Price": price_list, 
    "Description": desc_list, 
    "Overall rating": rating_list
})` 

##### Save to Excel

Save each page's data to an Excel file.

`df.to_excel(f"flipkart_product_list_{i}.xlsx", index=False)
print(f"Program {i} completed")` 

#### Notes

-   The class names used for finding elements are based on the current structure of Flipkart's HTML. If the structure changes, these class names may need to be updated.
-   Ensure that you are not violating Flipkart’s terms of service by scraping their website.

#### Troubleshooting

-   **Incomplete Data**: Check the class names and update them if necessary.
-   **Blocked Requests**: Ensure that the headers mimic a real browser. Consider adding delays between requests to avoid being blocked.

#### Contribution

Feel free to submit issues or pull requests on GitHub if you find any bugs or have suggestions for improvements.
