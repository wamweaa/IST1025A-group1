CON-VERT UNIT CONVERSION APPLICATION
=====================================

PROJECT CONTENTS
----------------
app.py                 Flask application / backend server
conversions.py         Python conversion functions
templates/index.html   Front-end HTML
static/style.css       Front-end styling
static/script.js       Front-end JavaScript
requirements.txt       Python dependency

HOW TO RUN
----------
1. Install Python 3 if it is not already installed.
2. Open a terminal in this project folder.
3. (Optional but recommended) Create and activate a virtual environment:

   python -m venv venv

   Windows:
   venv\Scripts\activate

   macOS/Linux:
   source venv/bin/activate

4. Install Flask:

   pip install -r requirements.txt

5. Start the application:

   python app.py

6. Open this address in your browser:

   http://127.0.0.1:5000

HOW IT WORKS
------------
The user selects a category, enters a value and chooses a conversion.
JavaScript sends the information to the Flask /convert endpoint.
Flask calls the relevant Python function in conversions.py and sends
the calculated result back to the browser.

NOTE
----
The time conversion from days to months uses an approximate month
length of 30.44 days, matching the original Python program.
