# Udacity Bikeshare.py project created by Boxcar2923

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ""
    while True:
        city_inp = input("Please tell me whether you want to view data from Chicago, New York City or Washington: " )
        if city_inp.lower() in CITY_DATA:
            print("Great let's explore the data of {}.".format(city_inp.title()))
            city = city_inp.lower()
            break
        else:
            print("The city you put in is not know to the Dataset. Please try again.")

    # TO DO: get user input for month (all, january, february, ... , june)
    month = ""
    while True:
        month_inp = input("Please tell me from what month you would like to see the data (all, january, february, ... , june): " )
        if month_inp.lower() in {"all", "january", "february", "march", "april", "may", "june"}:
            print("Great let's explore the data of {}.".format(month_inp.title()))
            month = month_inp.lower()
            break
        else:
            print("The month you put in is not know to the Dataset. Please try again.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ""
    while True:
        day_inp = input("Please tell me from what day you would like to see the data (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday): " )
        if day_inp.lower() in {"all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"}:
            print("Great let's explore the data of {}.".format(day_inp.title()))
            day = day_inp.lower()
            break
        else:
            print("The month you put in is not know to the Dataset. Please try again.")

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    #print("--------------HEAD------------------")
    #print(df.head())
    #print("--------------INFO------------------")
    #print(df.info())
    #print("--------------DESCRIBE------------------")
    #print(df.describe())

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    #print(df.head())
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("The most popular month is: {}".format(popular_month))

    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print("The most popular day of the week is: {}".format(popular_day_of_week))

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print("The most popular hour is: {}".format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return df

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df["Start Station"].mode()[0]
    print("The most commonly used start station is: {}.".format(popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station = df["End Station"].mode()[0]
    print("The most commonly used end station is: {}.".format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    # Combine dataframes
    combined_df = pd.concat([df["Start Station"], df["End Station"]], axis=1)
    #print(combined_df.head())

    # Find the most frequent combination
    most_frequent_combination = combined_df.groupby(['Start Station', 'End Station']).size().reset_index(name='counts').sort_values(by='counts', ascending=False).head(1)

    # Display the result
    print("The most frequent combination of start and end station is: '{}' AND '{}'.".format(most_frequent_combination.iloc[0,0],most_frequent_combination.iloc[0,1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    total_travel_time = df["Trip Duration"].sum()
    print("The total time travel on bikes based on your filters is: {}".format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("The mean time traveled on bikes based on your filters is: {}".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The counts of user types are:\n{}".format(user_types))
    print("\n")

    # TO DO: Display counts of gender
    try:
        user_gender = df['Gender'].value_counts()
        print("The counts of user gender are:\n{}".format(user_gender))
        print("\n")
    except KeyError:
        print("Sorry we cannot provide statistics on the gender because there is no information on the gender.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        eldest = int(df["Birth Year"].min())
        youngest = int(df["Birth Year"].max())
        averagest = int(df["Birth Year"].mode()[0])
        print("The earliest birth year is '{}', the most recent '{}', the most common '{}'".format(eldest, youngest, averagest))
    except KeyError:
        print("Sorry we cannot provide statistics on the birth year because there is no information on the birth year.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
    
    
    
def more_information(df):
    """Displays raw data on bikeshare users."""
    
    counter = 0
    
    while True:
        more_data = input("Would you like to see more data in form of raw data. Please enter 'Yes' or 'No':")
        if more_data.lower() == "no":
            break
        elif more_data.lower() == "yes":
            if counter < len(df):
                end_position = counter + 5
                if end_position > len(df):
                    end_position = len(df)
                    
            print('\nGathering User Stats...\n')
            start_time = time.time()
            raw_data = df[counter:end_position]
            print(raw_data)
            print("\nThis took %s seconds." % (time.time() - start_time))
            counter += 5
        else:
            print("Please enter 'Yes' or 'No':")
        

    print('-'*40)
    counter = 0
    
    
    
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        more_information(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
