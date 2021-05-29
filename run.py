import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():
    """
    Get sales figures input from the user
    """
    print("Please enter sales figures from the last market day")
    print("Input should be in the form 10, 20, 30, 40, 50, 60\n")

    data_str = input("Enter your data here: ")

    sales_data = data_str.split(",")
    validate_data(sales_data)

def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into ints,
    or if there are not exactly 6 values
    """
    try:
        if len(values) != 6:
            raise ValueError(
            f"Exactly 6 values required, you have provided {len(values)}")
    except ValueError as e:
        print(f"Invalid data: {e}, Essayez-vous encore une fois\n")



get_sales_data()
    