import chalk
import os
import requests
from bs4 import BeautifulSoup


class RainStation:
    def __init__(self, url: str):
        self.url = url
        self.raw_text = self.scrape_station()
        name, address = self.parse_header()

        self.name = name
        self.address = address

        self.rain_data = list()


    def scrape_station(self):
        response = requests.get(self.url)  # Sends an HTTP request over the internet
        raw_text = response.text
        return raw_text


    def parse_header(self):

        name, address = self.raw_text.splitlines()[0].split(' - ')
        return name, address

    def __repr__(self):
        message = f'RainStation({self.name}, {self.address}'
        return message


    def __str__(self):
        message = f'Station: {self.name}'
        return message


    def stat_finder(self, cleaned_data: dict) -> tuple:
        """sort and funnel the results to return"""
        most_rain = max(cleaned_data.items(), key=lambda t: t[1][0])

        return most_rain


    def cleaner(self, raw_raindata: str) -> dict:
        """clean the data"""

        clean_me = raw_raindata.split('\n')
        no_header = clean_me[11:]
        single_lines = [line.split() for line in no_header if line != '']
        cleanest = [line for line in single_lines if '-' not in line]
        date_to_dict = {data[0]: (int(data[1]), list(map(int, data[2:]))) for data in cleanest}
        # year_to_dict = {data[-4:]: (int(data[1]), list(map(int, data[2:]))) for data in cleanest}

        return date_to_dict


    def stat_printer(self, rain_stat: tuple) -> None:
        """display results"""

        date, rain_amount = rain_stat[0], int(rain_stat[1][0] / 24)
        year, month, day = date[-4:], date[3:6].capitalize(), date[1:2]

        chalk.red(
            f"{month}. {day}, {year} had the most rain with {rain_amount} hunderedths of an inch on an hourly average.")


    def max_day(self):
        text = self.raw_text
        dict_data = self.cleaner(text)
        max_rain = self.stat_finder(dict_data)
        print(max_rain)
        return max_rain


def compile_links():
    base_url = "http://or.water.usgs.gov/precip"

    response = requests.get(base_url)  # Send an HTTP request over the interwebs
    raw = response.text  # Getting the raw HTML as a string
    soup = BeautifulSoup(raw, 'html.parser')  # MAking a BS4 soup object

    rengas = [os.path.join(base_url, link['href']) for link in soup.find_all('a') if '.rain' in link['href']]

    return rengas


def run_links():
    links = compile_links()

    rain_stations = list()
    failed_links = list()
    counter = 0
    for link in links:
        try:
            rs = RainStation(url=link)
        except ValueError:
            failed_links.append(link)
            chalk.red(f"Failed station # {counter}")
        else:
            rain_stations.append(rs)
            chalk.green(f"built station # {counter}")
        finally:
            counter += 1
    pass

if __name__ == '__main__':
    run_links()