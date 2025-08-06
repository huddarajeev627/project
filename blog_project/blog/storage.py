import json
import os

POSTS_FILE = os.path.join(os.path.dirname(__file__), 'posts.json')

if not os.path.exists(POSTS_FILE):
    with open(POSTS_FILE, 'w') as f:
        json.dump([], f)

def read_posts():
    with open(POSTS_FILE, 'r') as f:
        return json.load(f)

def write_posts(posts):
    with open(POSTS_FILE, 'w') as f:
        json.dump(posts, f, indent=4)
