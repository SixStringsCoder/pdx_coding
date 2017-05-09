import os
import requests
import chalk



class RainyDays:
    def __init__(self, date, total_rain, hours):
        pass


    def __repr__(self):
        print('Date of most rain')


    def find_file(self, path: str) -> str:
        """
        open file of rain data

        :return:
        """

        with open(path, 'r') as file:
            text = file.read()  # .read is a method on a file object that returns the file as a single string
            return text


    def cleaner(self, raw_raindata: str) -> dict:
        """

        :return: 
        """

        clean_me = raw_raindata.split('\n')
        no_header = clean_me[11:]
        single_lines = [line.split() for line in no_header if line != '']
        cleanest = [line for line in single_lines if '-' not in line]
        date_to_dict = {data[0]: (int(data[1]), list(map(int, data[2:]))) for data in cleanest}

        return date_to_dict


    def rain_data(self) -> None:
        """
        locate file of rain date

        return: None
        """

        requests.get('http://or.water.usgs.gov/non-usgs/bes/')

        raw_raindata = find_file(os.path.join(FILE_PATH, 'sample.rain'))  # Open and display file
        cleaned = cleaner(raw_raindata)  # Remove upper lines and rogue data lines with dashes
        this_day_rain = stat_finder(cleaned)  # Loop through cleaned dict to find stats
        stat_printer(this_day_rain)  # Display stats