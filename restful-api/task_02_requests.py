#!/usr/bin/env python3

import requests
import csv


def fetch_and_print_posts():
    """ fetches data from an API and prints post titles """
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])

    else:
        print("No result")


def fetch_and_print_users():
    """fetches data and save on csv file"""
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        post_list = [{'id': post['id'], 'title': post['title'],
                      'userId': post['userId']} for post in posts]

        with open('posts.csv', 'w') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'userId'])
            writer.writeheader()
            writer.writerows(post_list)
        print("data saved on posts.csv")
    else:
        print("No result")


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_print_users()
