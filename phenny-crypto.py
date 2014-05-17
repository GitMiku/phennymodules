# -*- coding: utf-8 -*-
#Phenny module that outputs the current prices of various cryptocurrencies 
#Example output http://i.imgur.com/ruhI7Zb.png
import urllib2
import json
def crypto(phenny, input):
	dresponse = json.load(urllib2.urlopen('http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=132'))
	response = json.load(urllib2.urlopen("https://btc-e.com/api/3/ticker/btc_usd-btc_eur-btc_gbp-ltc_btc-nmc_btc-nvc_btc-trc_btc-ppc_btc-ftc_btc-xpm_btc"))
	return phenny.say("BTC/USD $" + str(response["btc_usd"]["last"]) + " | BTC/EUR €" + str(response["btc_eur"]["last"]) + " | BTC/GBP £" + str(response["btc_gbp"]["last"]) + " | LTC/BTC " + str(response["ltc_btc"]["last"]) + " | NMC/BTC " + str(response["nmc_btc"]["last"]) + " |  NVC/BTC " + str(response["nvc_btc"]["last"]) + " | TRC/BTC " + str(response["trc_btc"]["last"]) + " | PPC/BTC " + str(response["ppc_btc"]["last"]) + " | FTC/BTC " + str(response["ftc_btc"]["last"]) + " | XPM/BTC " + str(response["xpm_btc"]["last"]) + " | DOGE/BTC " + str(dresponse['return']['markets']['DOGE']['lasttradeprice']))
crypto.commands = ['btc', 'BTC', 'trc', 'ftc', 'crypto', 'btc-e', 'BTC-E', 'Btc', 'ltc', 'LTC', 'Crypto', 'Btc-e', 'doge', 'DOGE', 'Doge']

#dresponse is for DOGE/BTC since BTC-E does not have DOGE
