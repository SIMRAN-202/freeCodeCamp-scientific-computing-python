
def add_time(start, duration, week_day=None):


    # Split the start time into hour, minute, and meridiem (AM/PM)
    start_time = start.split(" ")
    start_hour = int(start_time[0].split(":")[0])
    start_minute = int(start_time[0].split(":")[1])
    meridiem = start_time[1]
    
    # Split the duration into hour and minute
    duration = duration.split(":")
    duration_hour = int(duration[0])
    duration_minute = int(duration[1])

    # Convert start hour to 24-hour format if it's PM
    if meridiem == "PM" and start_hour != 12: 
        start_hour += 12
    if meridiem == "AM" and start_hour == 12:
        start_hour = 0

    # Add the duration hours to the start hours
    total_hour = start_hour + duration_hour

    # Add the duration minutes to the start minutes
    total_minute = start_minute + duration_minute
    if total_minute >= 60:
        total_hour += 1
        total_minute -= 60

    # Calculate the final hour in 12-hour format
    final_hour = (total_hour % 24) % 12
    
    # Special case: 12:00 PM is the same as 12:00 AM for the next cycle
    if final_hour == 0:
        final_hour = 12

    # Calculate total days
    total_days = (total_hour // 24)

    # Determine AM/PM for the final time
    if (total_hour % 24) <= 11:
        meridiem = "AM"
    else:
        meridiem = "PM"

    # Format minutes (leading zero if necessary)
    if total_minute < 10:
        final_minute = "0" + str(total_minute)
    else:
        final_minute = str(total_minute)

     # Format the new time
    new_time = f'{final_hour}:{final_minute} {meridiem}'
    
    # If no weekday is provided, calculate the days later and return the time
    if week_day is None:
        if total_days == 0:
            return new_time
        elif total_days == 1:
            return new_time + " (next day)"
        return new_time + f" ({total_days} days later)"

    # If weekday is provided, calculate the new weekday after adding the days
    if week_day:
        # Days of the week in order
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

        # Find the current day index
        current_day_index = days_of_week.index(week_day.lower().capitalize())
        
        # Adjust the day index based on the number of days later
        new_day_index = (current_day_index + total_days) % 7
        
        # If there are days later than 0, we need to add a day_name
        if total_days == 0:
            return new_time + ", " + f"{days_of_week[current_day_index]}"
        elif total_days == 1:
            return new_time + ", " + f"{days_of_week[new_day_index]}" + " (next day)"
        return new_time + ", " + f"{days_of_week[new_day_index]}" + f" ({total_days} days later)"
