import argparse
import json
import math


def load_data(filepath):
    with open(filepath) as moscow_bars:
        return json.loads(moscow_bars.read())


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', help='path to json file')
    return parser.parse_args().f


def get_biggest_bar(data):
    return (max(data, key=lambda x: x['SeatsCount']))


def get_smallest_bar(data):
    return (min(data, key=lambda x: x['SeatsCount']))


def get_closest_bar(data, longitude, latitude):
    return (min(data, key=lambda x: math.hypot(float(x['Latitude_WGS84']) - latitude,
                                               float(float(x['Longitude_WGS84']) - longitude))))


if __name__ == '__main__':
    path = create_parser()
    moscow_bars = load_data(path)
    print('The most biggest bar: {}'.format(get_biggest_bar(moscow_bars)))
    print('The most smallest bar: {}'.format(get_smallest_bar(moscow_bars)))
    print('Nearest bar is: {}'.format(
        get_closest_bar(moscow_bars, float(input('Enter your longitude: ')), float(input('Enter your latitude: ')))))
