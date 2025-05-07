def calculate_arrival_time_pure_math():
    """
    Calculates the arrival time using only arithmetic and modulo operations.
    Assumes valid integer input within the expected ranges.
    """
    current_hour = int(input("Current hour (0-23)? "))
    current_minute = int(input("Current minute (0-59)? "))
    trip_minutes = int(input("Trip time (in minutes)? "))

    current_total_minutes = (current_hour * 60) + current_minute
    arrival_total_minutes = current_total_minutes + trip_minutes

    arrival_hour = (arrival_total_minutes // 60) % 24
    arrival_minute = arrival_total_minutes % 60

    print(f"\nEstimated time of arrival: {arrival_hour} hours and {arrival_minute} minutes.")

if __name__ == "__main__":
    calculate_arrival_time_pure_math()
