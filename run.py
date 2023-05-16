# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPE_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPE_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')


def validate_data(values):
    '''
    Validate user's first input to get sales data
    '''
    try:
        if len(values) != 6:
            raise ValueError(
                f'6 values required, you input {len(values)}'
            )
    except ValueError as e:
        print(f'Invalid data: {e}, please try again\n')


def get_data_sales():
    '''
    Get sales figures input from the user.
    '''
    print("Please enter sales data from the last market.")
    print("Data should be six numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60\n")

    data_str = input('Enter your data here: ')
    sales_data = data_str.split(',')  # the array is here
    validate_data(sales_data)  # array to validate


get_data_sales()
