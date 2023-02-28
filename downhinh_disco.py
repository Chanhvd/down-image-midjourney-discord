import random
import re
import os
import discord
import requests
from PIL import Image
from PIL import Image, ImageChops
import imagehash
url = 'https://discord.com/api/v9/auth/login'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
payload = {
        'login': 'email',
        'password': 'pass',
        'undelete': False,
        'captcha_key': None,
        'gift_code_sku_id': None,
        'login_source': None
    }

response = requests.post(url, json=payload, headers=headers)
    # print(response.status_code)
print(response.text)
match = re.search(r'"token":\s*"([^"]+)"', response.text)
if match:
    token = match.group(1)
    print(token)    
while True:
    
    headers = {
        'Authorization': token
    }

    channel_id = '997268018855940147'

    url = f'https://discord.com/api/v9/channels/{channel_id}/messages'

    response = requests.get(url, headers=headers)
    messages = response.json()
    image_links = []

    for message in messages:
        if 'attachments' in message and message['attachments']:
            for attachment in message['attachments']:
                if attachment.get('width') and attachment.get('height'):
                    image_links.append(attachment['url'])
        if 'embeds' in message and message['embeds']:
            for embed in message['embeds']:
                if embed.get('type') == 'image':
                    image_links.append(embed['url'])
    # print(image_links)
    # Tạo thư mục để lưu trữ các hình ảnh
    if not os.path.exists('images1'):
        os.makedirs('images1')

    if not os.path.exists('images1'):
        os.mkdir('images1')

    for idx, link in enumerate(image_links):
        while True:
            filename = f'image_{idx}.jpg'
            if os.path.exists(f'images1/{filename}'):
                # print(f'{filename} đã tồn tại.')
                idx += 1
                
            else:
                # print(f'{filename} chưa tồn tại.')
                break
        
        response = requests.get(link)
        # Kiểm tra xem phản hồi có thành công không
        if response.status_code == 200:
            # Ghi nội dung hình ảnh vào tệp tin
            with open(f'images1/{filename}', 'wb') as f:
                f.write(response.content)
            print(f'{filename} saved.')
        else:
            print(f'Error downloading image from {link}')
            
    print("Done")
    print("Wait for 80 giây...")
    for i in range(80, 0, -1):
        print(f"\r{i} seconds left...", end="")
        time.sleep(1)
    if idx > 1000:
        print(f"Reached the limit. File {filename} will not be saved.")
        break      
    print("\n kiểm tra hình trùng lặp...")   
    def delete_duplicate_images(directory):
        image_paths = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.jpg')]
        hashes = {}
        duplicates = []

        for path in image_paths:
            with open(path, 'rb') as f:
                image_hash = imagehash.average_hash(Image.open(f))
            if image_hash in hashes:
                duplicates.append(path)
                print(path)
            else:
                hashes[image_hash] = path

        for path in duplicates:
            os.remove(path)
            print(f'Deleted duplicate image: {path}')

        print('Done.')    
    directory = 'images1/'
    delete_duplicate_images(directory)
