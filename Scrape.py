import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_actual_price(product):
    actual_price_element = product.find("div", class_="_30jeq3")
    if actual_price_element:
        return actual_price_element.text
    else:
        return "N/A"

def get_discounted_price(product):
    discounted_price_element = product.find("div", class_="_3I9_wc _27UcVY")
    if discounted_price_element:
        return discounted_price_element.text
    else:
        return "N/A"

# Create empty lists to store the data
Product_name = []
Actual_price = []
Discounted_price = []
Image = []
RAM = []
Description = []
Reviews = []

total_pages = 5

for i in range(1, 51):
    url = f"https://www.flipkart.com/search?q=mobiles++phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&sort=popularity&page={i}"

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    products = soup.find_all("div", class_="_1AtVbE")

    for product in products:
        # Product Name
        name_element = product.find("div", class_="_4rR01T")
        if name_element:
            Product_name.append(name_element.text)
        else:
            Product_name.append("N/A")

        # Actual Price
        Actual_price.append(get_actual_price(product))

        # Discounted Price
        Discounted_price.append(get_discounted_price(product))

        # Image URL
        image_element = product.find("img", class_="_396cs4")
        if image_element:
            Image.append(image_element["src"])
        else:
            Image.append("N/A")

        # RAM
        ram_element = product.find("li", class_="rgWa7D")
        if ram_element:
            RAM.append(ram_element.text)
        else:
            RAM.append("N/A")

        # Description
        desc_element = product.find("ul", class_="_1xgFaf")
        if desc_element:
            Description.append(desc_element.text)
        else:
            Description.append("N/A")

        # Reviews
        review_element = product.find("div", class_="_3LWZlK")
        if review_element:
            Reviews.append(review_element.text)
        else:
            Reviews.append("N/A")

# Create a DataFrame
data = {
    "Product Name": Product_name,
    "Actual Price": Actual_price,
    "Discounted Price": Discounted_price,
    "Image URL": Image,
    "RAM": RAM,
    "Description": Description,
    "Reviews": Reviews
}

df = pd.DataFrame(data)

# Print the entire DataFrame
df.to_csv("E:/flipkartcomplete.csv")
