# !/usr/bin/python3
# -*- coding: utf-8 -*-
from pprint import pprint
from api_ai_translate.parser import load_jsons   as load
from api_ai_translate.build import build_file  as build
from api_ai_translate.intent import search_cases as search

from pysettings import conf

if __name__ == '__main__':

    print('Welcome.\n\nPlease select the "intent" folder from the zip exported from API.AI.\r\n')

    # parse all the json's in given dir to a list of Intent objects (api_ai_graphs.intent)
    if not conf.DEFAULT_INTENTS_PATH:
        raise Exception("Please define an intents path in the user_settings.py file")

    intents = load(conf.DEFAULT_INTENTS_PATH)

    build(intents)
