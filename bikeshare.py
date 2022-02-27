import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months_list=['january', 'february', 'march', 'april', 'may', 'june','all']

days_list=['monday', 'tuesday' , 'wednesday' , 'thursday' , 'friday' , 'saturday' , 'sunday' , 'all']

choices_list=['day','month']


def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    
    city=input('Would you like to see data for Chicago, New york city or Washington?\n').lower() 
    while city not in CITY_DATA.keys():
        city=input('Invalid input, please enter chicago, new york city or washington.\n').lower()
    print('looks like you want to hear about {}! If this is not true, restart the program now!\n\n'.format(city.title()))

    
    month=input('Which month?  Enter a month from january to june or all.\n').lower()
    while month not in months_list:
        month=input('Invalid input, please enter a month from january to june or all.\n').lower()
            
            
    day=input('Which day? Type a day monday, tuesday, wednesday, thursday, friday, saturday, sunday or all.\n').lower()
    while day not in days_list:
        day=input('Invalid input, please enter a day of monday, tuesday, wednesday, thursday, friday, saturday, sunday or all.\n').lower()
            
        
        
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    dic=CITY_DATA.get(city)
    df=pd.read_csv(dic)
    df['month']=pd.to_datetime(df['Start Time']).dt.month
    df['day']=pd.to_datetime(df['Start Time']).dt.day_name()
    
    if month!='all':
        df=df[df['month']==months_list.index(month)+1]
        
    if day!='all':
        df=df[df['day']==day.title()]

    return df


def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    most_common_month=df['month'].value_counts().idxmax()
    print('The most frequent month is {}.'.format(most_common_month))

    most_common_day=df['day'].value_counts().idxmax()
    print('The most frequent day is {}.'.format(most_common_day))

    df['hour']=pd.to_datetime(df['Start Time']).dt.hour
    most_common_hour=df['hour'].value_counts().idxmax()
    print('The most frequent hour is {}.'.format(most_common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    most_common_start_station= df['Start Station'].value_counts().idxmax()
    print('The most commonly start staion is {}.'.format(most_common_start_station))

    most_common_end_station= df['End Station'].value_counts().idxmax()
    print('The most commonly end staion is {}.'.format(most_common_end_station))

    most_common_combination=df.groupby(['Start Station','End Station']).size().idxmax()
    print('The most commonly start-end staion trip is {}.'.format(most_common_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time_seconds=np.sum(df['Trip Duration'])
    total_travel_time_minutes=total_travel_time_seconds//60
    total_travel_time_hours=total_travel_time_minutes//60
    total_travel_time_minutes_wihout_hours = total_travel_time_minutes % 60
    total_travel_time_seconds_wihout_minutes_and_hours = total_travel_time_seconds % 60
    
    if total_travel_time_minutes >60:
        print('Total travel time is {} hours, {} minutes and {} seconds.'.format(total_travel_time_hours, total_travel_time_minutes_wihout_hours, total_travel_time_seconds_wihout_minutes_and_hours))
    else:
        print('Total travel time is {} minutes and {} seconds.'.format(total_travel_time_minutes, total_travel_time_seconds_wihout_minutes_and_hours))
    
    
    mean_travel_time_seconds=int(np.mean(df['Trip Duration']))
    mean_travel_time_minutes=mean_travel_time_seconds//60
    mean_travel_time_hours=mean_travel_time_minutes//60
    mean_travel_time_minutes_wihout_hours = mean_travel_time_minutes % 60
    mean_travel_time_seconds_wihout_minutes_and_hours = mean_travel_time_seconds % 60
    
    if mean_travel_time_minutes >60:
        print('Average travel time is {} hours, {} minutes and {} seconds.'.format(mean_travel_time_hours, mean_travel_time_minutes_wihout_hours, mean_travel_time_seconds_wihout_minutes_and_hours))
    else:
        print('Average travel time is {} minutes and {} seconds.'.format(mean_travel_time_minutes, mean_travel_time_seconds_wihout_minutes_and_hours))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    counts_of_user_types=df.groupby(['User Type']).size()
    print('Counts of user types:\n {}.'.format(counts_of_user_types))
    
    try:
        counts_of_gender=df.groupby(['Gender']).size()
        print('Counts of user gender:\n {}.'.format(counts_of_gender))
            
        
        earliest_birth_year= int(np.min(df['Birth Year']))
        print('Earliest birth year is {}.'.format(earliest_birth_year))
            
        most_recent_birth_year=int(np.max(df['Birth Year']))
        print('Most recent birth year is {}.'.format(most_recent_birth_year))
            
        most_common_birth_year=int(df['Birth Year'].value_counts().idxmax())
        print('Most common birth year is {}.'.format(most_common_birth_year)) 
            
    except:
        print('There is no Gender or Birth Year features in this dataset')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)   


def view_data(df):
    answer=input('Do you want to view the first 5 rows of the data? type yes or no.\n').lower()
    answer_list=['yes','no']
    
    while answer not in answer_list:
        answer=input('Invalid option, please enter \"yes\" or \"no\".\n').lower()
        
    row_count=0
    
    while answer=='yes':
        print(df.iloc[row_count:row_count+5])
        row_count+=5
        answer=input('Do you want to view the next 5 rows of the data? type yes or no.\n').lower()
        
        while answer not in answer_list: 
            answer=input('Invalid option, please enter \"yes\" or \"no\".\n').lower()
            
            

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        try:
            time_stats(df)
            station_stats(df) 
            trip_duration_stats(df)
            user_stats(df)
            view_data(df)
            
        except:
            print('There is no values or features in this dataset (Empty dataset), try another filter next time.')
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()