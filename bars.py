import json
import math

def load_data(filepath):
    with open(filepath) as moscow_bars:
        return json.loads(moscow_bars.read())


def get_biggest_bar(data):
    return(max(data, key=lambda x: x['SeatsCount']))


def get_smallest_bar(data):
    return(min(data, key=lambda x: x['SeatsCount']))


def get_closest_bar(data, longitude, latitude):
    return(min(data, key=lambda x: math.hypot(float(x['Latitude_WGS84']) - latitude, float(float(x['Longitude_WGS84']) - longitude))))


if __name__ == '__main__':
    moscow_bars = load_data('data-2897-2016-11-23.json')
    print(get_biggest_bar(moscow_bars))
    print(get_smallest_bar(moscow_bars))
    print(get_closest_bar(moscow_bars), float(input()), float(input()))
