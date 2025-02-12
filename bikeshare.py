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

# User input for city and time filter
def get_filters():
    print('Hi, welcome to Motivate - Let\'s explore some bike share data.')

    while True:
        city = input('Select a city:\n1. Chicago\n2. New York\n3. Washington\n').strip().lower()
        if city == '1':
            city = 'chicago'
            break
        elif city == '2':
            city = 'new york'
            break
        elif city == '3':
            city = 'washington'
            break
        else:
            print('Invalid input. Please enter 1, 2, or 3.')

    while True:
        time_filter = input('Select a time filter:\n1. Month\n2. Day\n3. Not at all\n').strip().lower()
        if time_filter == '1':
            time_filter = 'month'
            break
        elif time_filter == '2':
            time_filter = 'day'
            break
        elif time_filter == '3':
            time_filter = 'not at all'
            break
        else:
            print('Invalid input. Please enter 1, 2, or 3.')

    month = day = None

    if time_filter == 'month':
        while True:
            month = input('Select a month:\n1. January\n2. February\n3. March\n4. April\n5. May\n6. June\n').strip().lower()
            if month in ['1', '2', '3', '4', '5', '6']:
                month = ['January', 'February', 'March', 'April', 'May', 'June'][int(month) - 1]
                break
            else:
                print('Invalid input. Please enter a number from 1 to 6.')

    elif time_filter == 'day':
        while True:
            day = input('Select a day:\n1. Monday\n2. Tuesday\n3. Wednesday\n4. Thursday\n5. Friday\n6. Saturday\n7. Sunday\n').strip().lower()
            if day in ['1', '2', '3', '4', '5', '6', '7']:
                day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][int(day) - 1]
                break
            else:
                print('Invalid input. Please enter a number from 1 to 7.')

    return city, time_filter, month, day

# Display raw data upon request
def display_raw_data(df):
    display_raw_data = input('\nWould you like to see the raw data? Enter yes or no.').strip().lower()
    start_idx = 0

    while display_raw_data == 'yes':
        print(df.iloc[start_idx:start_idx + 5])
        start_idx += 5

        if start_idx >= len(df):
            print("No more raw data to display.")
            break

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
