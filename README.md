# SafeKeep
#### Video Demo:  https://www.youtube.com/watch?v=DSxv5b84eWo
#### Description: A simple and secure password manager built using the Flask web framework and Flask extensions.

## Features

- User registration and authentication
- Secure password storage using a SQL database
- Easy-to-use web interface for managing passwords
- Responsive design using Bootstrap

## Requirements

- Python 3.10 or higher
- Flask
- Flask-WTForms
- Flask-Login
- Flask-Bootstrap
- Flask-SQLAlchemy

## Installation

1. Clone this repository:

```
git clone https://github.com/username/password-manager
```

```
pip install -r requirements.txt
```

## Usage
To start the password manager, run the following command:

```
flask run
```
By default, the app redirects guest users to authenticate. In order to access the private pages, follow this set up:

* Start the app via flask run
* Access the registration page and create a new user:
    * http://127.0.0.1:5000/register
* Access the login page and authenticate
    * http://127.0.0.1:5000/login

## Code-base structure
The project is coded using blueprints, app factory pattern, dual configuration profile (development and production) and an intuitive structure presented bellow:

```
< PROJECT ROOT >
   |
   |-- app/                                 # Our Application Module
   |    |
   |    |-- main/ 
             |-- __init__.py
   |    |    |-- views.py
             |-- errors.py
   |    |
   |    |-- auth/                           # Handles auth routes (login and register)
   |    |    |-- views.py                   # Define authentication routes  
   |    |    |-- __init__.py 
   |    |
   |    |-- pgenerator/                     # Handles the generation of the password
   |    |   |-- views.py
   |    |   |--__init__.py
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>          # CSS files, Javascripts files
   |    |
   |    |-- templates/                      # Templates used to render pages
   |    |    |-- vault/                     # vault pages
   |    |    |    |-- credentials.html      # view saved credentials page
   |    |    |    |-- add_credential.html   # add new credential page
   |    |    |    |-- edit_credential.html  # Edit credential page
   |    |    |
   |    |    |
   |    |    |-- auth/                      # Authentication pages
   |    |    |    |-- login.html            # Login page
   |    |    |    |-- register.html         # Register page
   |    |    |    |-- logout.py             # Logout page
   |    |    |
   |    |    |-- errors/                    # Error Pages
   |    |    |    |-- 500.html              # 500 page
   |    |    |    |-- 404-page.html         # 404 page
   |    |    |
   |    |    |-- pgenerator/
   |    |    |    |-- pgenerator.html       #Password generator page
   |    |    |
   |    |    |-- layout.html                # App Layout
   |    |    |-- footer.html                # App Footer
   |    |    |-- index.html                 # App homepage
   |    |
   |    |-- __init__.py                     # Initialize the app
   |    |-- forms.py
   |    |-- models.py
   |    |--*.py                             # All other python files
   |
   |-- config.py                            # Set up the app
   |-- requirements.txt                     # App Dependencies
   |
   |-- .env                                 # Inject Configuration via Environment
   |-- safekeep.py                          # Start the app - WSGI gateway
   |
   |-- ************************************************************************
```

## License
This project is licensed under the MIT License. See LICENSE for more details.


