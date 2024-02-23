from Parse_Xml import parse_xml
from db_manager import insert_product
from pymongo import MongoClient

# Parse the XML file
mongo_uri = "mongodb://localhost:27017"
client = MongoClient(mongo_uri)
db = client['Lonca_DB']
collection = db['products']
products = parse_xml('lonca-sample.xml')

# Insert products into MongoDB
for product in products:
    #print(product)
    insert_product(product,collection)