import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    
    # Do something with the credentials
    database_name = os.getenv("DATABASE_NAME")
    database_host = os.getenv("DATABASE_HOST")
    database_username = os.getenv("DATABASE_USERNAME")
    database_password = os.getenv("DATABASE_PASSWORD")
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    
    print("Hello, World!")