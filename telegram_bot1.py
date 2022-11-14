import telegram
from telegram.ext import*
import pandas_datareader as web
from nsetools import Nse
import json
import logging
from commands import *

nse = Nse()

TOKEN = '***********************'


if __name__ == "__main__":
    logging.basicConfig(
        format='%(levelname)s-%(message)s', level=logging.INFO)

    updater = Updater(TOKEN, use_context=True)
    disp = updater.dispatcher
    disp.add_handler(CommandHandler("start", start))
    # when start is i/p it runsstart func
    disp.add_handler(CommandHandler("stock", stock))
    disp.add_handler(CommandHandler("index", index))
    disp.add_handler(CommandHandler("top_gainers", top_gainers))
    disp.add_handler(CommandHandler("top_losers", top_losers))
    disp.add_handler(CommandHandler("fno_lot", fno_lot))

    updater.start_polling()
    updater.idle()
