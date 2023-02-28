import random
import re
from tkinter import  filedialog
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import nfc
import time
from PIL import Image
import os
import cv2
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
# Khởi tạo trình duyệt Chromium
# user_agent = UserAgent()
# random_user_agent = user_agent.random
# # print(random_user_agent)
# browser = webdriver.Chrome()
# chrome_options = Options()
# chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--disable-web-security")
# chrome_options.add_argument("--no-proxy-server")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--disable-notifications")
# chrome_options.add_argument("--disable-popup-blocking")
# chrome_options.add_argument("--disable-infobars")
# # chrome_options.add_argument(random_user_agent)
# chrome_options.add_argument('--disable-features=VizDisplayCompositor')
# # chrome_options.add_argument("--headless") # ẩn trình duyệt

# # browser.execute_script("Object.defineProperty(navigator, 'getDisplayMedia', {get: function() {return {};},});")
# browser.execute_script("Object.defineProperty(navigator, 'bluetooth', {get: function() {return {requestDevice: function() {return {};}};},});")
# browser.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5];},});")
# browser.execute_script("Object.defineProperty(navigator, 'languages', {get: function() {return ['en-US', 'en'];}})")
# browser = webdriver.Chrome(executable_path='chromedriver.exe', options=chrome_options)
    # Cài đặt các thiết lập cơ bản
# browser.set_window_size(500, 800)
# browser.set_window_position(200, 0)
    # Mở trang web
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
        'login': 'kt.dptech@gmail.com',
        'password': 'Chanh983845',
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
        'Authorization': 'MTA3OTk2Mjk3NTg4NjExODk4Mw.GFVphU.uVJo3ecunaq8jjCU8eF58WTftfDIUbEk5NFjjs'
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
    print("Wait for 30 giây...")
    for i in range(30, 0, -1):
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
    # Break the loop after 1 minute
 # def compare_images(image1_path, image2_path):
    #     image1 = Image.open(image1_path)
    #     image2 = Image.open(image2_path)
    #     if image1.mode != image2.mode or image1.size != image2.size:
    #         return False
    #     return ImageChops.difference(image1, image2).getbbox() is None

    # def delete_duplicate_images(directory):
    #     files = os.listdir(directory)
    #     print(files)
    #     for i in range(len(files)):
    #         image1_path = os.path.join(directory, files[i])
    #         print('i',i)
    #         for j in range(i+1, len(files)):
    #             image2_path = os.path.join(directory, files[j])
    #             print('J',j)
    #             if compare_images(image1_path, image2_path):
    #                 os.remove(image1_path)
    #                 print('a')
    #                 break

    # directory = 'images1/'
    # print('........')
    # delete_duplicate_images(directory)
       
    

# # Lặp qua từng đường dẫn để tải hình ảnh
# for idx, link in enumerate(image_links):
#     response = requests.get(link)
#     # Kiểm tra xem phản hồi có thành công không
#     if response.status_code == 200:
#         # Tạo tên tệp tin mới bằng cách thêm chỉ số vào đầu tên
#         filename = f'image_{idx}.jpg'
#         # Ghi nội dung hình ảnh vào tệp tin
#         with open(f'images1/{filename}', 'wb') as f:
#             f.write(response.content)
#         print(f'{filename} saved.')
#     else:
#         print(f'Error downloading image from {link}')