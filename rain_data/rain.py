"""
Print out a summary of the data:

* The specific date with the most rain.

"""


import os
import chalk


FILE_PATH = '/Users/mbp/Git/labpractice/rain_data/'


def stat_printer(rain_stat: tuple) -> None:
    """display results"""

    date, rain_amount = rain_stat[0], int(rain_stat[1][0] / 24)
    year, month, day = date[-4:], date[3:6].capitalize(), date[1:2]

    chalk.red(f"{month}. {day}, {year} had the most rain with {rain_amount} hunderedths of an inch on an hourly average.")
    chalk.green(f"The year with the most rain was {year} with {rain_amount} inches of rain.")


def stat_finder(cleaned_data: dict) -> tuple :
    """sort and funnel the results to return"""
    most_rain = max(cleaned_data.items(), key=lambda t: t[1][0])
    # least_rain = min(cleaned_data.items(), key=lambda t: t[1][0])

    return most_rain


def find_file(path: str) -> str:
    """open file of rain data"""

    with open(path, 'r') as file:
        text = file.read()  # .read is a method on a file object that returns the file as a single string
        return text


def cleaner(raw_raindata: str) -> dict:
    """clean the data"""

    clean_me = raw_raindata.split('\n')
    no_header = clean_me[11:]
    single_lines = [line.split() for line in no_header if line != '']
    cleanest = [line for line in single_lines if '-' not in line]
    date_to_dict = {data[0]: (int(data[1]), list(map(int, data[2:]))) for data in cleanest}

    return date_to_dict


def rain_data() -> None:
    """
    - locate file of rain date
    - call cleaner
    - call stat_finder
    - then display it
    """

    raw_raindata = find_file(os.path.join(FILE_PATH, 'sample.rain'))    # Open and display file
    cleaned = cleaner(raw_raindata)         # Remove upper lines and rogue data lines with dashes
    this_day_rain = stat_finder(cleaned)    # Loop through cleaned dict to find stats
    stat_printer(this_day_rain)             # Display stats

rain_data()

