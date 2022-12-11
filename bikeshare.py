import time
import pandas as pd
import numpy as np
import datetime as dt


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city,ch month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    listcity = ['chicago' , 'new york city', 'washington']

    city = input("Please choose any city data you want chicago, new york city or Washington? ")
     
    while city.lower() not in listcity:
        city = input("try again please with the same spelling of city (chicago, new york city or Washington) ")

    # TO DO: get user input for filter the date 
    month =0
    day = 0
    datelist = ['month' , 'day', 'both', 'none']
    datefilter = input("Do you want to filter the date on the month or day or both or none? ")
    while datefilter.lower() not in datelist:
        datefilter = input("try again please with the same spelling ")
    
    if datefilter.lower() == "month":
        month =1
    elif  datefilter.lower() == "day":
        day = 1
    elif  datefilter.lower() == "both":
        month =1
        day = 1

    # TO DO: get user input for month (all, january, february, ... , june)
    monthS  = 'all'
    if month == 1:
        listmonth=['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
               'november', 'december']
        monthS = input("Please choose any month data you want ? ")
        while monthS.lower() not in listmonth:
            monthS = input("try again please with the same spelling of month like (january, february, march, april, may,june,july, august, september, october, november, december)  ")
   
   
   # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    dayS  = 'all'
    if day == 1:
        listDay= ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        dayS = input("Please choose any day data you want ? ")
        while dayS.lower() not in listDay:
            dayS = input("try again please with the same spelling of month like (monday, tuesday, wednesday, thursday, friday,saturday,sunday)  ")
            
    print('-'*40)
    city = city.lower()
    monthS = monthS.lower()
    dayS = dayS.lower()
    return city, monthS, dayS


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
     # read data 
    df = 'data'
    if city == 'chicago':
        df = pd.read_csv('chicago.csv')
    elif  city == 'new york city':
        df = pd.read_csv('new_york_city.csv')
    elif  city == 'washington':
        df = pd.read_csv('washington.csv')
   
    # filter month 
    if month != 'all':
        list_of_months = {'january': '1', 'february': '2', 'march': '3',
                              'april': '4', 'may': '5', 'june': '6', 'july': '7',
                              'august': '8', 'september': '9', 'october': '10',
                              'november': '11', 'december': '12'}
        month = int(list_of_months[month])
        df['Start Time'] = pd.to_datetime(df['Start Time'], errors='coerce')
        df['month'] = df['Start Time'].dt.month
        df = df[df['month'] == month]
        df.drop('month', axis=1, inplace=True)

    # filter day
    if day != 'all':
        #["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        list_of_days = {'monday': '1', 'tuesday': '2', 'wednesday': '3',
                              'thursday': '4', 'friday': '5', 'saturday': '6', 'sunday': '7'}
        month = int(list_of_days[day])
        df['Start Time'] = pd.to_datetime(df['Start Time'], errors='coerce')
        df['day'] = df['Start Time'].dt.dayofweek
        df = df[df['day'] == month]
        df.drop('day', axis=1, inplace=True)
    
    return df


def time_stats(df, month , day):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if month != 'all':
        print('\nYou select %s month' % month )
    else:
        df['Start Time'] = pd.to_datetime(df['Start Time'], errors='coerce')
        df['month'] = df['Start Time'].dt.month_name()
        MostMonth = df['month'].value_counts().idxmax()
        df.drop('month', axis=1, inplace=True)
        print('\nThe most common month is %s ' % MostMonth )
       
    # TO DO: display the most common day of week
    if day != 'all':
            print('\nYou select %s ' % day )
    else:
        df['Start Time'] = pd.to_datetime(df['Start Time'], errors='coerce')
        df['day'] = df['Start Time'].dt.strftime('%A')
        MostDay = df['day'].value_counts().idxmax()
        df.drop('day', axis=1, inplace=True)
        print('\nThe most common month is %s ' % MostDay )
    
    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'], errors='coerce')
    df['hour'] = df['Start Time'].dt.hour
    Mosthour = df['hour'].value_counts().idxmax()
    print('\nThe most common start hour  %s ' % Mosthour )
    df.drop('hour', axis=1, inplace=True)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df ):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    MostStartStation = df['Start Station'].value_counts().idxmax()
    print('\nThe most commonly used start station  %s ' % MostStartStation )
   
    # TO DO: display most commonly used end station
    MostEndStation = df['End Station'].value_counts().idxmax()
    print('\nThe most commonly used end station  %s ' % MostEndStation )

    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = 'From ' + df['Start Station'] + ' station To '+ df['End Station'] + ' station'
    MostTrip = df['trip'].value_counts().idxmax()
    df.drop('trip', axis=1, inplace=True)
    print('\nThe most frequent combination of start station and end station trip it is %s ' % MostTrip )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # Calculating Duration
    df['Start Time'] = pd.to_datetime(df['Start Time'], errors='coerce')
    df['End Time'] = pd.to_datetime(df['End Time'], errors='coerce')
    df['Duration'] =  pd.to_datetime(df['End Time'], errors='coerce') - pd.to_datetime(df['Start Time'], errors='coerce')
    # TO DO: display total travel time
    print('\nTotal travel time  %s ' % df['Duration'].sum() )
 
    # TO DO: display mean travel time
    print('\nMean travel time  %s ' % df['Duration'].mean() )
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""


    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nCounts of user types\n')
    print(df['User Type'].value_counts())
    # Check if you are in the washington city
    if city == 'washington':
        print("No data about user in washington" )  
        return 
    # TO DO: Display counts of gender
    print('\nCounts of user Gender\n')
    print(df['Gender'].value_counts())
    # TO DO: Display earliest, most recent, and most common year of birth
    print("\nEarliest year of birth for users %s " % df['Birth Year'].min() )
    print("\nMost recent of birth for users %s " % df['Birth Year'].max() )
    print("\nMost common year of birth for users %s " % df['Birth Year'].mean() )   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def  Row_Data(df):
    restart = input('\nWould you like to see some of row data? Enter yes or no.\n')
    start =0
    end = 4
    while restart.lower() == 'yes':
        print(df.loc[start:end,:])
        start = start + 5
        end = end +5
        restart = input('\nWould you like to see more row data? Enter yes or no.\n')

           
    
    

def main():
    while True:
        city, month, day = get_filters()
        
        df = load_data(city, month, day)
        
        Row_Data(df)

        time_stats(df,  month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df , city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("Thank you")
            break


if __name__ == "__main__":
	main()
