# Best Buy Restock Alert

## About
This Python script looks at the Best Buy website for an item. If that item is in stock, it will send you a text message that includes link directly to the item. If the item is not in stock, the script will check again in 2 minutes. You must supply the Twilio credentials and phone number.

## Instructions
1. Fill in environment variables in `sample_env.txt` and rename that file to `.env`
2. Insert links of all the items from Best Buy that you want the script to look at in `main.py:32`
3. In project directory install required packages: `pip3 install -r requirements.txt`
4. Run general.py

## Inspiration
My GTX 1070 suddenly gave out in January 2021. It turned it out to be worst timing to enter the GPU market at the time due to a variety of factors (COVID, Cryptocurrency, etc.). Since GPU's were very hard to find manually, I wrote my own script to check multiple Best Buy products for an RTX 3070.

## Results
After 8 days of running the script, I was personally able to get an Gigabyte RTX 3070 Vision after having my script text me immediately after founding out that it was in stock. The text message included a link to the product on the Best Buy page. 

Results may vary, but this script personally notified me about 10 minutes before StockDrop did. StockDrop is a discord server with about 130000+ members that assists in alerting members of availability for CPUs, GPUs, and consoles. 
Although my script did beat StockDrop when it came to buying my GPU, I still recommend joining the server so that you can get alerts from other vendors (Newegg, B&H, Amazon, Walmart, etc.) when they drop.

12/27/2021 Update: I used this bot to also help my girlfriend purchase a Dyson Airwrap.