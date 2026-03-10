import requests
import random
from atproto import Client

API = "https://chaturbate.com/api/public/affiliates/onlinerooms/?wm=T2CSW&client_ip=request_ip&limit=20"

client = Client()

client.login("yourhandle.bsky.social","APP_PASSWORD")

data = requests.get(API).json()

rooms = data["results"]

room = random.choice(rooms)

post = f"""
🔥 {room['num_users']} people watching this stream right now

{room['username']} just went live

{room['room_subject']}

Watch live cams
"""

client.send_post(post)
