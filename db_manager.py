from datetime import datetime

def insert_product(product_data, db_collection):
    # Check if the product already exists
    existing_product = db_collection.find_one({'stock_code': product_data['stock_code']})
    if existing_product is None:
        # Insert the product if it does not exist
        db_collection.insert_one(product_data)
    else:
        # Update the existing product, including the updatedAt field
        update_data = product_data.copy()
        update_data['updatedAt'] = datetime.now()  # Set the updatedAt to current time
        
        db_collection.update_one(
            {'_id': existing_product['_id']},
            {'$set': update_data}
        )