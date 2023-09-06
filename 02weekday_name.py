def weekday_name(day_of_week):

    days = [
        'Sunday', 
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
    ]

    if day_of_week < 1 or day_of_week > 7:
        return None
    return days[day_of_week - 1]