#!/usr/bin/python3
"""
This module sets up a basic Flask application that serves web pages using Jinja templates.
It demonstrates the use of reusable components in templates to maintain a consistent layout
across multiple pages. The application includes routes for home, about, and contact pages.

Routes:
- /: Renders the home page.
- /about: Renders the about page.
- /contact: Renders the contact page.

The templates include reusable header and footer components for consistency.

Usage:
Run this script to start the Flask application. Ensure that you have Flask installed.
Navigate to http://127.0.0.1:5000/ in your browser to view the pages.

Example:
    $ python3 task_01_jinja.py

Dependencies:
    - Flask (pip install Flask)
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """
    Renders the home page.

    Returns:
        str: The rendered HTML template for the home page.
    """
    return render_template('index.html')

@app.route('/about')
def about_html():
    """
    Renders the about page.

    Returns:
        str: The rendered HTML template for the about page.
    """
    return render_template('about.html')

@app.route('/contact')
def contact_html():
    """
    Renders the contact page.

    Returns:
        str: The rendered HTML template for the contact page.
    """
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)