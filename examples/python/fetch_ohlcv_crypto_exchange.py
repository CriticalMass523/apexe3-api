'''
/**
 * fetch_aggregate_ohlcv.py
 * 
 * Retrieves OHLCV for traditional and digital assets
 * 
 * Disclaimer:
 * APEX:E3 is a financial technology company based in the United Kingdom https://www.apexe3.com
 *  
 * None of this code constitutes financial advice. APEX:E3 is not 
 * liable for any loss resulting from the use of this code or the API. 
 * 
 * This code is governed by The MIT License (MIT)
 * 
 * Copyright (c) 2020 APEX:E3 Team
 * 
 **/
'''

import sys
sys.path.append('..')
from apexe3.apexe3 import initialise
from apexe3.apexe3 import fetch_OHLCV_for_exchange

import pandas as pd

def init():
    clientId = "your-client-id-goes-here"
    clientSecret = "your-client-secret-goes-here"
    initialise(clientId, clientSecret)

if __name__ == "__main__":
    init()
    #Change parameters as desired -run supported-asset-markets-exchanges.js file for a list of supported markets / exchanges
    #This endpoint is currently limited to COINBASEPRO and FTX for the free tier
    table=pd.DataFrame(fetch_OHLCV_for_exchange('COINBASEPRO','BTC','USD','2018-01-01','2020-12-31','1d'))
    table.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
    print(table)