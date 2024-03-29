# Paystack with Django

This repository contains a simple implementation of Paystack payment gateway integration with a Django application.

## Features

* Integration of Paystack API for secure payment processing
* Django views and templates for handling payment process
* Use of Python for server-side scripting

## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have installed Python 3.x
* You have a Django project set up
* You have registered on Paystack and obtained your public key and secret key

## Setting Up a Virtual Environment

Before installing the dependencies, it's recommended to set up a virtual environment. A virtual environment is a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages. This allows you to isolate the dependencies for each project separately.

Here are the steps to create a virtual environment:

1. Navigate to the directory where you want to create your project.
2. Run the following command to create a virtual environment:

   For Unix/MacOS:
   python3 -m venv env


   For Windows:
   py -m venv env


3. After creating the virtual environment, you need to activate it:

   For Unix/MacOS:
   source env/bin/activate


   For Windows:
   .\env\Scripts\activate

## Installing

To install, follow these steps:

1. Clone the repository: `git clone https://github.com/Ikar700/paystack_with_django.git`
2. Navigate into the cloned directory: `cd paystack_with_django`
3. Install the required Python packages: `pip install -r requirements.txt`

## Using

After installation, you can start using the payment system. Here's how:

1. Run your Django server: `python manage.py runserver`
2. Open your web browser and navigate to `http://localhost:8000/`
3. Follow the instructions to make a payment.

Please note that you will need to replace the placeholder public and secret keys in the settings file with your actual keys from Paystack.

## Contributing

If you want to contribute to this project, please fork this repository and submit a pull request. Any contributions you make are greatly appreciated.

## License

This project uses the following license: [MIT](LICENSE).

## Contact

If you want to contact me, you can reach me at `Cornex111@gmail.com`.
