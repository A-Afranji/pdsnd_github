import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs:
    city = input("Insert a city from (chicago, new york city, washington): " ).lower()
    while city not in CITY_DATA.keys():
        print("Invalid city name")
        city = input("Insert a city from: (chicago, new york city, washington) " ).lower()
    

    # TO DO: get user input for month (all, january, february, ... , june):
    months = ['january', 'february', 'march', 'april', 'may', 'june','all']
    while True:
        month = input("Insert a month or all for all months from: ('january', 'february', 'march', 'april', 'may', 'june','all') ").lower()
        if month in months:
            break
        else:
            print("Invalid month")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday):
    days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']
    while True:
        day = input("Insert a day or all for all days from: ('sunday','monday','tuesday','wednesday','thursday','friday','saturday','all')").lower()
        if day in days:
            break
        else:
            print("Invalid day")
            
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    
    df["month"] = df["Start Time"].dt.month_name()
    df["day of week"] = df["Start Time"].dt.day_name()
    df["start hour"] = df["Start Time"].dt.hour
    
    
    if month != "all":
        df = df[df["month"] == month.title()]
    
    if day != "all":
        df = df[df["day of week"] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month:
    print("The most common month:", df["month"].mode()[0]) 

    # TO DO: display the most common day of week:
    print("The most common day of week: ", df["day of week"].mode()[0])

    # TO DO: display the most common start hour:
    print("The most common start hour: ", df["start hour"].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station:
    print("The most commonly used start station: ", df["Start Station"].mode()[0])

    # TO DO: display most commonly used end station:
    print("The most commonly used end station: ", df["End Station"].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip:
    df["path"] = df["Start Station"] + "-" + df["End Station"]
    print("The most frequent combination road path from the start and end stations:", df["path"].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time:
    print("The total travel time: {} hours".format((df["Trip Duration"].sum()/3600).round()))

    # TO DO: display mean travel time:
    print("The mean travel time: {} minutes".format((df["Trip Duration"].mean()/60).round()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types:
    print("The counts of user types: ", df["User Type"].value_counts().to_frame())

    # TO DO: Display counts of gender:
    if city != "washington":
        print("The counts of gender: ", df["Gender"].value_counts().to_frame())

    # TO DO: Display earliest, most recent, and most common year of birth:
        print("The earliest year of birth: ", int(df["Birth Year"].min()))
        print("The recent year of birth: ", int(df["Birth Year"].max()))
        print("The most common year of birth: ", int(df["Birth Year"].mode()[0]))
    else:
        print("There is no data for this city about gender or birth year.")
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    

def display_data(df):
    """Displays data in order to prompt the users if they want to see 5 lines of raw data."""
    
    print("\nThe raw data is ready to be checked....\n")
    
    i = 0
    user_input = input("Do you want to display 5 rows of raw data?, please insert yes or no").lower()
    if user_input not in ["yes","no"]:
        print("Invalid input, please insert yes or no")
        user_input = input("Do you want to display 5 rows of raw data?, please insert yes or no").lower()
    
    elif user_input != "yes":
        print("Thank you")
    
    else:
        while i+5 < df.shape[0]:
            print(df.iloc[i:i+5])
            i +=5
            user_input = input("Do you want to display more 5 rows of raw data?, please insert yes or no").lower()
            if user_input != "yes":
                print("Thank you")
                break    
    
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            

        


if __name__ == "__main__":
	main()
