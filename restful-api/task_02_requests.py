#!/usr/bin/python3
"""
API
"""
import requests
import csv


def fetch_and_print_posts():
    """
    Fetch all posts from JSONPlaceholder and print the status code and titles of each post.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get('title'))
    else:
        print(f"Failed to fetch posts: HTTP {response.status_code}")

def fetch_and_save_posts():
    """
    Fetch all posts from JSONPlaceholder and save id, title, and body into posts.csv.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        data = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print("Posts saved to posts.csv")
    else:
        print(f"Failed to fetch posts: HTTP {response.status_code}")
