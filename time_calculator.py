# Time Calculator: Adds a duration to a start time, handles day rollovers, 
# and optionally tracks the day of the week. Built for the freeCodeCamp certification.

def add_time(start, duration, day=None):
    weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    # 1. Split the inputs into parts
    start_time = start.split()
    start_hour_min = start_time[0].split(":")
    duration_time = duration.split(":")

    # 2. Add minutes and hours together
    added_min = int(start_hour_min[1]) + int(duration_time[1])
    added_hour = int(start_hour_min[0]) + int(duration_time[0])

    # 3. Handle minutes rollover
    if added_min >= 60:
        added_hour += int(added_min / 60)
        added_min = added_min % 60
    
    # 4. Convert to "24-hour style" to calculate days easily
    if start_time[1] == "PM":
        added_hour += 12

    added_day = int(added_hour / 24)
    final_hour = added_hour % 24

    # 5. Convert back to 12-hour format for the display
    if final_hour >= 12:
        start_time[1] = "PM"
    else:
        start_time[1] = "AM"
    
    # Logic to handle 12:00 AM and 12:00 PM
    display_hour = final_hour % 12
    if display_hour == 0:
        display_hour = 12
    
    # Manual minute formatting (adding the 0 if needed)
    if added_min < 10:
        display_min = "0" + str(added_min)
    else:
        display_min = str(added_min)

    # 6. Build the result string
    new_time = str(display_hour) + ":" + display_min + " " + start_time[1]

    # Handle the optional day of the week
    if day != None:
        for i in range(len(weekdays)):
            if day.lower() == weekdays[i]:
                new_day = weekdays[(i + added_day) % 7].capitalize()
        new_time = new_time + ', ' + new_day

    # Handle "next day" and "n days later"
    if added_day == 1:
        new_time = new_time + ' (next day)'
    elif added_day > 1:
        new_time = new_time + ' (' + str(added_day) + ' days later)'

    return new_time

# --- TEST CASES ---
if __name__ == "__main__":
    
    print(add_time('3:30 PM', '2:12')) # 5:42 PM
    print(add_time('11:55 AM', '3:12')) # 3:07 PM
    print(add_time('11:59 PM', '24:05')) # 12:04 AM (2 days later)
    print(add_time('8:16 PM', '466:02')) # 6:18 AM (20 days later)
    print(add_time('8:16 PM', '466:02', 'tuesday')) # 6:18 AM, Monday (20 days later)