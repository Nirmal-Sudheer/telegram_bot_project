from nsetools import Nse
import json
import logging
import pandas_datareader as web


nse = Nse()


def fno_lot(updater, conext):
    q = nse.get_fno_lot_sizes()
    k = json.dumps(q, indent=4)
    updater.message.reply_text(k)
    logging.info("Function called.")


def top_losers(updater, conext):
    try:
        q = nse.get_top_losers()
        k = json.dumps(q, indent=4)
        updater.message.reply_text(k)
    except:
        updater.message.reply_text("No data available now")
    logging.info("Function called.")


def top_gainers(updater, conext):
    try:
        q = nse.get_top_gainers()
        k = json.dumps(q, indent=4)
        updater.message.reply_text(k)
    except:
        updater.message.reply_text("No data available now")

    logging.info("Function called.")


def index(updater, context):
    q = nse.get_index_list()
    k = json.dumps(q, indent=4)
    updater.message.reply_text(k)
    logging.info("Function called.")


def stock(updater, context):
    ticker = context.args[0]
    q = nse.get_quote(ticker)
    if q is None:
        updater.message.reply_text("Please enter a valid stock name")
    else:
        k = json.dumps(q, indent=4)
        updater.message.reply_text(k)

    logging.info("Function called.")


def start(updater, context):
    updater.message.reply_text("""
    Following commands available are:
    /stock <stock name>:Presents all stock details

    /index:Presents all index Status

    /top_gainers:Presents top gainers for given day

    /top_losers:Presents top losers for given day

    /fno_lot:Presents F&O lot sizes of all the stocks and indices

    """)
    logging.info("Function called.")
