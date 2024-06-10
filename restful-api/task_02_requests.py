#!/usr/bin/python3


import requests
import csv


def fetch_and_print_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    posts = response.json()

    with open('posts.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for post in posts:
            writer.writerow([post.get('userId'), post.get(
                'id'), post.get('title'), post.get('body')])
