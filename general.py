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

# Enter urls of product you would like

stores = {
  "www.bestbuy.com" : [
    'https://www.bestbuy.com/site/sandisk-128gb-microsdxc-uhs-i-memory-card-for-nintendo-switch/6103002.p?skuId=6103002',
    'https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149'
  ],
  # "www.dyson.com" : [
  #   'https://www.dyson.com/hair-care/hair-stylers/airwrap#airwrap-choose-your-color'
  # ]
}

minutes = 0
while True:
  for store in stores:
    urls = stores[store]
    for url in urls:
      store = requests.get(url, headers = headers)
      storeHtml = store.content

      soup = BeautifulSoup(storeHtml, 'html.parser')
      parsed_url = urlparse(url)
      netloc = parsed_url.netloc

      # Grab text base on website
      if netloc == "www.bestbuy.com":
        title = soup.select('.sku-title .heading-5.v-fw-regular')[0].text
        button = soup.select('.c-button.add-to-cart-button')
        availableText = "Add to Cart"
      elif netloc == "www.dyson.com":
        title = soup.select('.trade-up-item__name.js-trade-up-item-name')[0].text
        button = soup.select('.trade-up-item__add-to-basket')
        availableText = "Add to Basket"
      else:
        title = "Store not supported yet"
        button = []
        availableText = ""

      if len(button) > 0 and button[0].text == availableText:
        print(f"BUY NOW: {url}")
        message = twilioClient.messages.create(
          messaging_service_sid = twilioMessagingServiceSid,
          to = myPhoneNumber,
          body = f"Text:  Buy Now: {url} "
        )
      else:
        print(f"Sold out. Checking again in 2 minute. It has been {minutes} minutes to far. ({title})")
      time.sleep(2)

  minutes += 2
  time.sleep(120)