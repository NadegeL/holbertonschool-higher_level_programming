#!/usr/bin/env python3
"""Consuming and processing data from an
API using Python mandatory
"""

import requests
import csv
import json


def fetch_and_print_posts():
    """Fetches data from an API and prints post titles"""
    url = 'https://jsonplaceholder.typicode.com/posts'
    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            posts = response.json()
            for post in posts:
                print(post.get('title'))
        else:
            print("No result")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


def fetch_and_save_posts():
    """Fetches data and saves it in a CSV file"""
    url = 'https://jsonplaceholder.typicode.com/posts'
    try:
        response = requests.get(url)

        if response.status_code == 200:
            posts = response.json()
            post_list = [{'id': post.get('id'), 'title': post.get('title'),
                          'userId': post.get('userId')} for post in posts]

            with open('posts.csv', 'w', newline='') as file:
                writer = csv.DictWriter(
                    file, fieldnames=['id', 'title', 'userId'])
                writer.writeheader()
                writer.writerows(post_list)

            print("Data saved in posts.csv")
        else:
            print("No result")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
