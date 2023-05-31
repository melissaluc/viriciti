import os
from dotenv import load_dotenv

curr_dir = os.path.dirname(__file__)
dotenv_path = os.path.realpath(
    os.path.join(curr_dir, '..', 'secrets', 'credentials.env')
    )

load_dotenv(dotenv_path=dotenv_path)

# Account Login Credentials
USERNAME = os.getenv('ACCOUNT_USERNAME')
PASSWORD = os.getenv('ACCOUNT_PASSWORD')

# Database Connection Credentials
ORACLE_DB_USERNAME = os.getenv('ORACLE_DB_USERNAME')
ORACLE_DB_PASSWORD = os.getenv('ORACLE_DB_PASSWORD')
ORACLE_DB_HOSTNAME = os.getenv('ORACLE_DB_HOSTNAME')
ORACLE_DB_PORTNUM =  os.getenv('ORACLE_DB_PORTNUM')
ORACLE_DB_SERVICENAME =  os.getenv('ORACLE_DB_SERVICENAME')