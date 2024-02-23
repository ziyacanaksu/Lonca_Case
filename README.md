# Lonca_Case
## Project Summary

This project demonstrates the successful development of a pipeline that extracts product information from an XML file and stores it in a MongoDB database, ensuring data integrity and avoiding duplication on subsequent runs. The implementation showcases efficient XML parsing, data manipulation, and interaction with MongoDB to achieve near real-time integration of supplier stock systems into our database.

## Key Achievements

- **Efficient XML Parsing**: Developed a robust parser that extracts required product information from an XML file, catering to the needs of dynamic and complex data structures.
- **Intelligent Data Storage**: Implemented a MongoDB-based storage solution that inserts new product entries and updates existing ones without creating duplicates, preserving the integrity of the database.
- **Data Consistency and Formatting**: Enforced a consistent formatting rule for product names and other fields to maintain data uniformity across the database.
- **Dynamic Data Handling**: The script is designed to handle thousands of products efficiently, showcasing scalability and robustness in data processing and storage.

## Technical Overview

### Parsing and Data Extraction

Using Python’s `xml.etree.ElementTree`, the script parses the XML file to extract product details, demonstrating effective handling of nested structures and various data types.

### MongoDB Integration

The `pymongo` library facilitates the interaction with the MongoDB database, where the script checks for existing entries using the `stock_code` as a unique identifier and performs insertions or updates accordingly. Special attention is given to the `createdAt` and `updatedAt` fields to track the lifecycle of each product entry accurately.

### Data Formatting

Custom logic is applied to ensure that product names and other textual data are formatted according to the specified guidelines, enhancing data readability and consistency.

## Screenshots and Demonstrations

![Screenshot 2024-02-23 144512](https://github.com/ziyacanaksu/Lonca_Case/assets/130456179/66f16180-0327-4b16-bfc2-96d322d8abce)
![Screenshot 2024-02-23 144622](https://github.com/ziyacanaksu/Lonca_Case/assets/130456179/eec481d2-e6b4-45cd-a09c-eebcdec6e9a0)
![Screenshot 2024-02-23 144828](https://github.com/ziyacanaksu/Lonca_Case/assets/130456179/367df3ef-9c95-44f8-ab1e-dc46a1dd5340)
![Screenshot 2024-02-23 144912](https://github.com/ziyacanaksu/Lonca_Case/assets/130456179/22a523ba-3c41-41b7-98ac-d683e37d963e)
