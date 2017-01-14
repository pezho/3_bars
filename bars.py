import argparse
import json
import math


def load_data(filepath):
    with open(filepath) as moscow_bars:
        return json.loads(moscow_bars.read())


def get_file_path():
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


def show_results(smallest_bar, biggest_bar, closest_bar):
    print("Самый маленький бар {} расположен по адресу {}.".format(smallest_bar["Name"], smallest_bar["Address"]))
    print("Самый большой бар {} расположен по адресу {}.".format(biggest_bar["Name"], biggest_bar["Address"]))
    print("Ближайший бар {} расположен по адресу {}.".format(closest_bar["Name"], closest_bar["Address"]))


if __name__ == '__main__':
    path = get_file_path()
    moscow_bars = load_data(path)

    smallest_bar = get_smallest_bar(moscow_bars)
    biggest_bar = get_biggest_bar(moscow_bars)
    closest_bar = get_closest_bar(moscow_bars,
                                  float(input('Введите широту: ')), float(input('Введите долготу: ')))

    show_results(smallest_bar, biggest_bar, closest_bar)
