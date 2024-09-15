#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json(file_path):
    """
    Reads a JSON file and returns the data as a list of dictionaries.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        list: A list of dictionaries containing the data read from the JSON file.
    """
    with open(file_path, 'r') as file:
        return json.load(file)

def read_csv(file_path):
    """
    Reads a CSV file and returns the data as a list of dictionaries.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        list: A list of dictionaries containing the data read from the CSV file.
    """
    products = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

def read_sqlite(database_path):
    """
    Reads data from a SQLite database and returns it as a list of dictionaries.

    Args:
        database_path (str): The path to the SQLite database file.

    Returns:
        list: A list of dictionaries containing the data read from the SQLite database.
    """
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()
    products = [{'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]} for row in rows]
    conn.close()
    return products

@app.route('/products')
def products():
    """
    Renders the products page based on the source and product ID provided in the query parameters.

    Query Parameters:
        source (str): The source of the data, either 'json', 'csv', or 'sql'.
        id (int, optional): The ID of the product to filter by.

    Returns:
        str: The rendered HTML template for the products page.
    """
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    if source == 'json':
        products = read_json('products.json')
    elif source == 'csv':
        products = read_csv('products.csv')
    else:
        products = read_sqlite('products.db')

    if product_id:
        product_id = int(product_id)
        filtered_products = [product for product in products if product['id'] == product_id]
        if not filtered_products:
            return render_template('product_display.html', error="Product not found")
        products = filtered_products

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)