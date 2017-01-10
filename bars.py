import json
import math

def load_data(filepath):
    with open(filepath) as data:
        d = json.loads(data.read())
    return d


def get_biggest_bar(data):
    return(max(data, key=lambda x: x['SeatsCount']))


def get_smallest_bar(data):
    return(min(data, key=lambda x: x['SeatsCount']))


def get_closest_bar(data, longitude, latitude):
    return(min(data, key=lambda x: math.hypot(float(x['Latitude_WGS84']) - latitude, float(float(x['Longitude_WGS84']) - longitude))))


if __name__ == '__main__':
    data = load_data('data-2897-2016-11-23.json')
    print(get_biggest_bar(data))
    print(get_smallest_bar(data))
    print(get_closest_bar(data), float(input()), float(input()))
