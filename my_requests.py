#!/usr/bin/env python3

import requests
import csv

def fetch_and_print_posts():
    ''' Fetches data from an API and prints post titles '''
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    print(f'Status Code: {response.status_code}')
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get('title'))

if __name__ == '__main__':
    fetch_and_print_posts()