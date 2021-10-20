def time_conversion(s: str) -> str:
    """
    Time Conversion problem: https://www.hackerrank.com/challenges/one-month-preparation-kit-time-conversion/problem

    :param s: A time in 12-hour format.
    :return: The time in 24-hour format.
    """
    time_sep = ":"
    am_pm = s[len(s) - 2:]
    time = s[:len(s) - 2]
    hour_min_sec = time.split(time_sep)
    if int(hour_min_sec[0]) == 12:
        if am_pm == "PM":
            return time
        elif am_pm == "AM":
            hour_min_sec[0] = "00"
    elif am_pm == "PM" and 1 <= int(hour_min_sec[0]) <= 11:
        hour_min_sec[0] = str(int(hour_min_sec[0]) + 12)
    else:
        return time
    return time_sep.join(hour_min_sec)
