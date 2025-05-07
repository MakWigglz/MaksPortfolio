def calculate_arrival_time():
    """
    Calculates the arrival time based on the current time and trip duration.
    """
    try:
        current_hour = int(input("Current hour (0-23)? "))
        current_minute = int(input("Current minute (0-59)? "))
        trip_minutes = int(input("Trip time (in minutes)? "))

        if not (0 <= current_hour <= 23 and 0 <= current_minute <= 59 and trip_minutes >= 0):
            print("Invalid input. Please ensure the hour is between 0-23, the minute is between 0-59, and the trip time is non-negative.")
            return

        trip_hours = trip_minutes // 60
        remaining_minutes = trip_minutes % 60

        arrival_minute = (current_minute + remaining_minutes) % 60
        arrival_hour = (current_hour + trip_hours + (current_minute + remaining_minutes) // 60) % 24

        print(f"\nEstimated time of arrival: {arrival_hour} hours and {arrival_minute} minutes.")

    except ValueError:
        print("Invalid input. Please enter numeric values for time and duration.")

if __name__ == "__main__":
    calculate_arrival_time()
