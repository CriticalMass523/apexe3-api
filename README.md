# APEXE3-API - Providing Digital Asset Analytics for algorithmic trading & analysis

[![Discord](https://img.shields.io/discord/631158541486653466?logo=discord&logoColor=white)](https://discord.gg/cMdMBem)  [![Twitter Follow](https://img.shields.io/twitter/follow/apexe3hq?style=social&label=APEXE3HQ)](https://twitter.com/APEXE3HQ)

The APEX:E3 API gives you access to powerful analytics and market data generated by APEX:E3's Big Data Analytics Architecture. You can view this data on our [web based application](https://app.ae3platform.com).

### [Install & Quick Start](#install) 
### [Low Code Examples of How To Use the API](https://github.com/apexe3/apexe3-api/tree/main/examples) 
### [Example Low Code Dashboard Built Using the API](https://docs.google.com/spreadsheets/d/e/2PACX-1vQ8777n4TIZvcWjD48WrKxPiJcaTOZwBg2WWNyHgR8NnDgLMtCT1E2EPqb2d_otdLUw3YzBQgB6_bLv/pubhtml)
### [API Docs](https://api.ae3platform.com/docs) 
### [APEX:E3](https://www.apexe3.com)
### [Web Application](https://app.ae3platform.com/)

In addition to enriched exchange data from all major cryptocurrency exchanges, the **APEX:E3 API** includes real-time analytics and market intelligence. This means you can access live orderbook analytics, arbitrage opportunities and identify large blocks of liquidity with ease. The low code examples have been designed with simplicity in mind so that you can easily start to manipulate the data to enhance or create new trading bots, conduct real-time analysis or create powerful algorithms. The data structures can be easily stored in your database of choice for historical analysis, backtesting or general querying.

This API has been created for quants, algorithmic traders, data scientists, financial analysts and anybody who has a casual or formal interest in creating real-time trading algorithms or analysing cryptocurrency markets. 

Current real-time and on-demand features:

- structured data from all the major cryptocurrency exchanges covering thousands of pairs
- sorted aggregated global orderbook data structure (bids/asks for individual pairs across multiple exchanges in one place)  
- bid/ask imbalance ratios (quantification of buy / sell market intent)
- orderbook whale detection (identification of abnormally large bids across thousands of markets)
- arbitrage opportunities (between multiple exchanges and thousands of markets in one place) 
- spreads (delta between top bid and ask prices across thousands of markets)

## Cryptocurrency exchange data feeds

|      |Exchange|
|------|--------|
|[![binance](https://user-images.githubusercontent.com/1294454/29604020-d5483cdc-87ee-11e7-94c7-d1a8d9169293.jpg)](https://www.binance.com)|Binance|
|[![binance](https://user-images.githubusercontent.com/1294454/29604020-d5483cdc-87ee-11e7-94c7-d1a8d9169293.jpg)](https://www.binance.com)|Binance Futures |
|[![bitfinex](https://user-images.githubusercontent.com/1294454/27766244-e328a50c-5ed2-11e7-947b-041416579bb3.jpg)](https://www.bitfinex.com)|Bitfinex|  
|[![bitmex](https://user-images.githubusercontent.com/1294454/27766319-f653c6e6-5ed4-11e7-933d-f0bc3699ae8f.jpg)](https://www.bitmex.com)|Bitmex| 
|[![bitstamp](https://user-images.githubusercontent.com/1294454/27786377-8c8ab57e-5fe9-11e7-8ea4-2b05b6bcceec.jpg)](https://www.bitstamp.net)|Bitstamp|
|[![bittrex](https://user-images.githubusercontent.com/51840849/87153921-edf53180-c2c0-11ea-96b9-f2a9a95a455b.jpg)](https://bittrex.com)|Bittrex|  
|[![coinbasepro](https://user-images.githubusercontent.com/1294454/41764625-63b7ffde-760a-11e8-996d-a6328fa9347a.jpg)](https://pro.coinbase.com/)|Coinbase Pro|  
|[![ftx](https://user-images.githubusercontent.com/1294454/67149189-df896480-f2b0-11e9-8816-41593e17f9ec.jpg)](https://ftx.com)|FTX|
|[![ftx](https://user-images.githubusercontent.com/1294454/67149189-df896480-f2b0-11e9-8816-41593e17f9ec.jpg)](https://ftx.com)|FTX Derivatives|
|[![gateio](https://user-images.githubusercontent.com/1294454/31784029-0313c702-b509-11e7-9ccc-bc0da6a0e435.jpg)](https://www.gate.io)|Gateio|
|[![hitbtc](https://user-images.githubusercontent.com/1294454/27766555-8eaec20e-5edc-11e7-9c5b-6dc69fc42f5e.jpg)](https://hitbtc.com)|HitBTC|
|[![huobipro](https://user-images.githubusercontent.com/1294454/76137448-22748a80-604e-11ea-8069-6e389271911d.jpg)](https://www.huobi.com/en-us)|HuobiPRO|
|[![kraken](https://user-images.githubusercontent.com/51840849/76173629-fc67fb00-61b1-11ea-84fe-f2de582f58a3.jpg)](https://www.kraken.com)|Kraken|
|[![kraken](https://user-images.githubusercontent.com/51840849/76173629-fc67fb00-61b1-11ea-84fe-f2de582f58a3.jpg)](https://www.kraken.com)|Kraken Futures|
|[![okex](https://user-images.githubusercontent.com/1294454/32552768-0d6dd3c6-c4a6-11e7-90f8-c043b64756a7.jpg)](https://www.okex.com)|OKEX|
|[![okex](https://user-images.githubusercontent.com/1294454/32552768-0d6dd3c6-c4a6-11e7-90f8-c043b64756a7.jpg)](https://www.okex.com)|OKEX Derivatives|
|[![poloniex](https://user-images.githubusercontent.com/1294454/27766817-e9456312-5ee6-11e7-9b3c-b628ca5626a5.jpg)](https://poloniex.com)|Poloniex| 
|[![zb](https://user-images.githubusercontent.com/1294454/32859187-cd5214f0-ca5e-11e7-967d-96568e2e2bd1.jpg)](https://www.zb.com)|ZB|

# Install

1. Clone this repository into your project directory from [APEX:E3 GitHub repository](https://github.com/apexe3/apexe3-api):
```shell
git clone git@github.com:apexe3/apexe3-api.git
```

**Python**

***Python 3.8.x required***. Version 3.8.6 can be downloaded for the MAC [here](https://www.python.org/ftp/python/3.8.6/python-3.8.6-macosx10.9.pkg) and for Windows [here]( https://www.python.org/downloads/release/python-386/). 

You can check your current version of Python by typing

```shell
python --version
```
or if you are on Python 3.x.x

```shell
python3 --version
```

1. cd into the apexe3-api directory
```shell
cd apexe3-api
```

2. run setup.py to install dependencies
```shell
python3 examples/python/setup.py install 
```
3. If you see errors about directory permissions then use the sudo command
```shell
sudo python3 examples/python/setup.py install 
```

See [Quick start](https://github.com/apexe3/apexe3-api/blob/main/README.md#quick-start---global-aggregated-orderbook-streamed-in-the-command-line) below for an example of what you can do once the Python dependencies have been installed. 

**Nodejs**

**Successfully tested on Node 11.x - 14.x**. Nodejs can be downloaded for Mac and Windows from [here](https://nodejs.org/en/download/)

1. cd into the directory
```shell
cd apexe3-api/examples/nodejs
```
2. run npm install to install dependencies
```shell
npm install
```
 
## See Low Code examples for what you can do once you have installed dependencies (https://github.com/apexe3/apexe3-api/tree/main/examples)

