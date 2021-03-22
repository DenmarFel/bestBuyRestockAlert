import requests
from bs4 import BeautifulSoup

from twilio.rest import Client
from urllib.parse import urlparse

import time

import os
from os.path import join, dirname
from dotenv import load_dotenv

# Create .env file path.
dotenv_path = join(dirname(__file__), '.env')

# Load file from the path.
load_dotenv(dotenv_path)


# Enter navigator.userAgent in a brower console to get headers
headers = {'User-Agent': os.getenv('USER_AGENT')}

twilioSid = os.getenv('TWILIO_SID')
twilioAuthCode = os.getenv('TWILIO_AUTHCODE')
twilioClient = Client(twilioSid, twilioAuthCode)
twilioMessagingServiceSid = os.getenv('TWILIO_MESSAGING_SERVICES_SID')

# Make sure phone number is verified in Twilio
myPhoneNumber = os.getenv('PHONE_NUMBER')

# Enter urls of Best Buy product you would like
urls = [
  'https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442',
  'https://www.bestbuy.com/site/gigabyte-geforce-rtx-3070-eagle-8g-gddr6-pci-express-4-0-graphics-card-black/6437912.p?skuId=6437912',
  'https://www.bestbuy.com/site/gigabyte-geforce-rtx-3070-vision-oc-8g-gddr6-pci-express-4-0-graphics-card-white/6439385.p?skuId=6439385',
  'https://www.bestbuy.com/site/evga-geforce-rtx-3070-xc3-black-gaming-8gb-gddr6-pci-express-4-0-graphics-card/6439300.p?skuId=6439300',
  'https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3060-ti-eagle-oc-8g-gddr6-pci-express-4-0-graphics-card-black/6442485.p?skuId=6442485'
]

i = 0
while True:
  for url in urls:
    bestBuy = requests.get(url, headers = headers)
    bestBuyHtml = bestBuy.content

    soup = BeautifulSoup(bestBuyHtml, 'html.parser')

    parsed_url = urlparse(url)
    netloc = parsed_url.netloc

    # Grab text base on website
    if netloc == "www.bestbuy.com":
      rtx3070Title = soup.select('.sku-title .heading-5.v-fw-regular')[0].text
      rtx3070Btn = soup.select('button.btn-primary.add-to-cart-button')
    else:
      rtx3070Btn = []
      rtx3070Title = "Store not supported yet"

    if len(rtx3070Btn) > 0 and rtx3070Btn[0].text == "Add to Cart":
      print(f"BUY NOW: {url}")
      message = twilioClient.messages.create(
        messaging_service_sid = twilioMessagingServiceSid,
        to = myPhoneNumber,
        body = f"Text:  Buy Now: {url} "
      )
    else:
      print(f"Sold out. Checking again in 2 minute. It has been {i} minutes to far. ({rtx3070Title})")

    time.sleep(2)
  i += 1
  time.sleep(120)