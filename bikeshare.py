import time
import pandas as pd

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
    city_check = ["new york city" , "washington" , "chicago"]
    month_check = ["january" , "february" , "march" , "april" , "may" , "june" , "all"]
    day_check = ["sunday" , "monday" , "tuesday" , "wednesday" , "thursday" , "friday" , "saturday" , "all"]

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("From which city you want to see the data ?\n[ new york city , washington , chicago ].")
    city = city.lower()

    if city not in city_check:
        while city not in city_check:
            city = input("City is undefined \nPlease try again")


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input(" What is the month that you want to filter by?\n[ January , February , March , April , May , June , all:(for no month filter) ] ")
    month = month.lower()

    if month not in month_check:
        while month not in month_check:
            month = input("Month is undefined \nPlease try again")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("What is the day that you want to filter by?\n[ Sunday , Monday , Tuesday , Wednsday , Thursday , Friday , Saterday , all (to apply no month filter) ]")
    day = day.lower()

    if day not in day_check:
        while day not in day_check:
            day = input("Day is undefined \nPlease try again")

    print('-'*40)
    return city, month, day


def load_data(city , month , day):
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

    # convert the Start Time column to datetime
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    # extract month and day of week from Start Time to create new columns
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.weekday_name

    # filter by month if applicable
    if month != "all":
        # use the index of the months list to get the corresponding int
        months = ["january" , "february" , "march" , "april" , "may" , "june"]
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df["month"] == month]
    # filter by day of week if applicable
    if day != "all":
        # filter by day of week to create the new dataframe
        df = df[df["day_of_week"] == day.title()]
    return df

def time_stats(df , month , day):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    if month == "all":
        common_month = df["month"].mode()[0]
        months_count = df["month"].value_counts()
        print("\nThe Most Common Month\n{}\n\nCount\n{}\n".format(common_month , months_count[common_month]))
    # TO DO: display the most common day of week
    if day == "all":
        common_day = df["day_of_week"].mode()[0]
        days_count = df["day_of_week"].value_counts()
        print("\nThe Most Common Day Of The Week\n{}\n\nCount\n{}\n".format(common_day , days_count[common_day]))
    # TO DO: display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    common_hour = df["hour"].mode()[0]
    hours_count = df["hour"].value_counts()
    print("\nThe Most Common Hour Of The Day\n{}\n\ncount\n{}\n".format(common_hour , hours_count[common_hour]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df["Start Station"].mode()[0]
    starts_counter = df["Start Station"].value_counts()
    print("\nMost Commonly Used Start Station \n{}\n\ncount\n{}\n".format(common_start , starts_counter[common_start]))

    # TO DO: display most commonly used end station
    common_end = df["End Station"].mode()[0]
    ends_counter = df["End Station"].value_counts()
    print("\nMost Commonly Used End Station\n{}\n\ncount\n{}\n".format(common_end, ends_counter[common_end]))

    # TO DO: display most frequent combination of start station and end station trip
    df["Trip From Start To End"] = "Start Station: " + df["Start Station"] + "     " + "End Station: " + df["End Station"]
    common_trip = df["Trip From Start To End"].mode()[0]
    trips_counter = df["Trip From Start To End"].value_counts()
    print("\nMost Common Trip\n({})\n\ncount\n{}\n".format(common_trip , trips_counter[common_trip]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    durations_sum = df["Trip Duration"].sum()
    durations_mean = df["Trip Duration"].mean()

    # TO DO: display total travel time
    print("\nTotal Travel Time\n{}\n".format(durations_sum))
    # TO DO: display mean travel time
    print("\nAverage Travil Time\n{}\n".format(durations_mean))

    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    type_counter = df["User Type"].value_counts()
    print("Counts of user types\n{}\n".format(type_counter))

    # TO DO: Display counts of gender
    if city != "washington":
        gender_counter = df["Gender"].value_counts()
        print("\nCounts Of Gender\n{}\n".format(gender_counter))

    # TO DO: Display earliest, most recent, and most common year of birth
    if city != "washington":
        common_birth = df["Birth Year"].mode()[0]
        birth_counter = df["Birth Year"].value_counts()
        recent_date = df["Birth Year"].max()
        earliest_date = df["Birth Year"].min()
        print("\nEarliest year of birth\n{}\ncount\n{}\n\nMost recent year
        of birth\n{}\ncount\n{}\n\nMost common year of birth\n{}\ncount\n{}\n".format(
        earliest_date , birth_counter[earliest_date] , recent_date ,
        birth_counter[recent_date] , common_birth ,birth_counter[common_birth]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        counter_1 = 0
        counter_2 = 5

        while True:
            data_display = input("\nWould you like to view individual data ? Type yes or no\n")
            five_rows = df[counter_1:counter_2]

            print("\nIndividual Data\n" ,five_rows)
            counter_1 += 5
            counter_2 += 5

            if data_display.lower() != "yes":
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
