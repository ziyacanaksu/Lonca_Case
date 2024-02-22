import xml.etree.ElementTree as ET
from datetime import datetime
from html import unescape
import re
from bs4 import BeautifulSoup




def parse_description(description):
    soup = BeautifulSoup(description, 'html.parser')
    measurements = {
        'product_measurements': {},
        'model_measurements': {}
    }
    
    # Find all <li> elements
    for li in soup.find_all('li'):
        text = li.get_text(strip=True)
        
        fabric_match = re.search(r'Kumaş Bilgisi:(.*)',text)
        if fabric_match:
             fabric = fabric_match.group(1).strip() if fabric_match else ''
        # Check if it's a product measurement
        product_match = re.search(r'Ürün Ölçüleri[0-9]*:(.*)', text)
        if product_match:
            # Extract measurements using regex, capturing labels and values
            product_measurements = re.findall(r'(\w+): (\d+ cm)', product_match.group(1))
            measurements['product_measurements'] = {label: value for label, value in product_measurements}
            print(measurements['product_measurements'])
        
        # Check if it's a model measurement
        model_match = re.search(r'Model Ölçüleri:(.*)', text)
        if model_match:
            # Extract measurements using regex, capturing labels and values
            model_measurements = re.findall(r'(\w+): (\d+\.?\d*)', model_match.group(1))
            measurements['model_measurements'] = {
                label: (value + ('' if label == 'Kilo' else ' cm')) for label, value in model_measurements
            }
            print(measurements['model_measurements'])
        model_measurements_str = ", ".join(f"{k}: {v}" for k, v in measurements['model_measurements'].items())
        product_measurements_str = ", ".join(f"{k}: {v}" for k, v in measurements['product_measurements'].items())

    return fabric, model_measurements_str, product_measurements_str


   




def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    products = []
    
    for product in root.findall('Product'):
        description_text = unescape(product.find('Description').text)
        fabric, model_measurements_str, product_measurements_str = parse_description(description_text)
        
        product_data = {
            'stock_code': product.attrib['ProductId'],
            'color': '',  # This will be overwritten if color is found in ProductDetails
            'discounted_price': '',
            'images': [],  # This will be overwritten by the list of image paths
            'is_discounted': '',
            'name': capitalize_turkish(product.attrib['Name']),
            'price': '',
            'price_unit': '',
            'product_type': '',
            'quantity': '',
            'sample_size': '',
            'series': '',
            'status': '',
            'fabric': fabric,
            'model_measurements': model_measurements_str,
            'product_measurements': product_measurements_str,
            'createdAt': datetime.now(),
            'updatedAt': datetime.now(),
        }
        
        # Extract product details from ProductDetails
        details = product.find('ProductDetails')
        for detail in details:
            key = detail.attrib['Name']
            value = detail.attrib['Value'].replace(',', '.')
            if key == 'Price':
                product_data['price'] = float(value)
            elif key == 'DiscountedPrice':
                product_data['discounted_price'] = float(value)
                product_data['is_discounted'] = product_data['discounted_price'] < product_data['price']
            elif key == 'ProductType':
                product_data['product_type'] = value
            elif key == 'Quantity':
                product_data['quantity'] = int(value)
            elif key == 'Color':
                product_data['color'] = value  
            elif key == 'Series':
                product_data['series'] = value
            elif key == 'Season':
                product_data['status'] = "Active" if "Yaz" in value else "Inactive"
        
        # Add image paths to the product data
        images = product.find('Images')
        if images is not None:
            product_data['images'] = [img.attrib['Path'] for img in images.findall('Image')]
        
        products.append(product_data)
    
    return products


def capitalize_turkish(s):
    # Split the string into words to handle each word's first letter
    words = s.split()
    corrected_words = []

    for word in words:
        if not word:
            corrected_words.append(word)
            continue
        
        # Handle the first letter of each word
        first_letter = word[0]


        # Correctly handle the rest of the word
        rest = word[1:].replace('I', 'ı').lower()

        corrected_words.append(first_letter + rest)

    # Join the corrected words back into a string
    return ' '.join(corrected_words)

# Example usage
product_name = "Büzgü Kollu T-shirt"
formatted_name = capitalize_turkish(product_name)
print(formatted_name)