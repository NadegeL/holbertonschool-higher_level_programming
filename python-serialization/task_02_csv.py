#!/usr/bin/python3
"""Converting CSV Data to JSON Format"""

import csv
import json


def convert_csv_to_json(csv_file):
    """convert csv data to json format"""
    try:
        with open(csv_file, 'r') as file:
            data_csv = csv.DictReader(file)

        with open('data.json', 'w') as file:
            json.dump(data_csv, file)

        return True

    except FileNotFoundError:
        return False
