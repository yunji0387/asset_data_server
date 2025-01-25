# Asset Management System

This is a Django-based web application for managing asset data and prices.

## Features

- Manage asset data
- Track asset prices
- REST API for asset data and prices

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply the migrations:
    ```sh
    python manage.py migrate
    ```

5. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Usage

- Access the application at `http://127.0.0.1:8000/`
- Use the admin interface at `http://127.0.0.1:8000/admin/` to manage asset data and prices

## Deployment

This project is configured to be deployed on Heroku. Ensure you have the Heroku CLI installed and follow these steps:

1. Login to Heroku:
    ```sh
    heroku login
    ```

2. Create a new Heroku app:
    ```sh
    heroku create
    ```

3. Deploy the application:
    ```sh
    git push heroku main
    ```

4. Run the migrations on Heroku:
    ```sh
    heroku run python manage.py migrate
    ```

## License

This project is licensed under the MIT License. See the [LICENSE](http://_vscodecontentref_/1) file for details.