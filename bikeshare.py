import pandas as pd

# Data files for each city
chicago_data = 'chicago.csv'
new_york_data = 'new_york_city.csv'
washington_data = 'washington.csv'

# Data based on user's choice
def load_data(city):
    try:
        if city == 'chicago':
            return pd.read_csv(chicago_data)
        elif city == 'new york':
            return pd.read_csv(new_york_data)
        elif city == 'washington':
            return pd.read_csv(washington_data)
        else:
            return None
    except FileNotFoundError:
        return None

# Function to check data entry
def check_data_entry(prompt, valid_entries):
    try:
        user_input = str(input(prompt)).lower()
        while user_input not in valid_entries:
            print('It looks like your entry is incorrect.')
            print('Let\'s try again!')
            user_input = str(input(prompt)).lower()

        print('Great! You\'ve chosen: {}\n'.format(user_input))
        return user_input

    except:
        print('There seems to be an issue with your input.')

# User input for city and time filter
def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    valid_cities = ['chicago', 'new york city', 'washington']
    prompt_cities = 'Choose one of the 3 cities (Chicago, New York City, Washington): '
    city = check_data_entry(prompt_cities, valid_cities)

    valid_months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    prompt_month = 'Choose a month (all, January, February, ... , June): '
    month = check_data_entry(prompt_month, valid_months)

    valid_days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    prompt_day = 'Choose a day (all, Monday, Tuesday, ... Sunday): '
    day = check_data_entry(prompt_day, valid_days)

    print('-' * 40)
    return city, month, day

# Display raw data upon request
def display_raw_data(df):
    pd.set_option("display.max_columns", 200)  # To display all columns
    i = 0
    while True:
        display_data = input('\nDo you want to view 5 rows of raw data? Please enter yes or no.\n')
        if display_data.lower() != 'yes':
            break
        print(df.iloc[np.arange(0 + i, 5 + i)])
        i += 5

# Main function Data analysis
def main():
    city, time_filter, month, day = get_filters()
    df = load_data(city)

    if df is None:
        print('Error: Data file not found. Please make sure the data files exist in the current directory.')
        return

    if time_filter == 'month' and month is not None:
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df = df[df['Start Time'].dt.month == ['January', 'February', 'March', 'April', 'May', 'June'].index(month) + 1]

    elif time_filter == 'day' and day is not None:
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df = df[df['Start Time'].dt.day_name() == day]

    # Display raw data if the user requests it
    display_raw_data(df)

if __name__ == "__main__":
    main()
