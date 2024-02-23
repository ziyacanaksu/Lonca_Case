from datetime import datetime

def insert_product(product_data, db_collection):
    # Check if the product already exists
    existing_product = db_collection.find_one({'stock_code': product_data['stock_code']})
    if existing_product is None:
        # Insert the product if it does not exist
        db_collection.insert_one(product_data)
    else:
        # Update the existing product without altering the createdAt field
        update_data = product_data.copy()
        
        # Ensure createdAt from the existing product is preserved
        update_data['createdAt'] = existing_product['createdAt']
        
        # Set the updatedAt to current time
        update_data['updatedAt'] = datetime.now()
        
        # Perform the update
        db_collection.update_one(
            {'_id': existing_product['_id']},
            {'$set': update_data}
        )