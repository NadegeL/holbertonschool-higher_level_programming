#!/usr/bin/env python3
"""Converting CSV Data to JSON Format"""

import csv
import json


def convert_csv_to_json(CSV_filename):
    """takes the CSV filename as its parameter"""

    try:
        with open(CSV_filename, 'r') as csv_file:
            """open csv_filename in reader mode"""
            csv_reader = csv.DictReader(csv_file)
            """read data of csv_filename"""
            data = [row for row in csv_reader]
            """convert data csv in dict"""

        with open('data.json', 'w', encoding='utf-8') as json_file:
            """open json.file in writer mode"""
            json.dump(data, json_file)
            """write data in json format in json_file"""
            return True
    except FileNotFoundError:
        print(f"File {CSV_filename} not found.")
        return False
