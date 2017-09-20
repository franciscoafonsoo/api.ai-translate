# !/usr/bin/python3
# -*- coding: utf-8 -*-
from api_ai_translate.parser import load_jsons   as load
from api_ai_translate.parser import rebuild_jsons as dump
from api_ai_translate.build import output_file
from api_ai_translate.build import input_file

from pysettings import conf

if __name__ == '__main__':

    print('Welcome.\n\nPlease select the "intent" folder from the zip exported from API.AI.\r\n')

    # parse all the json's in given dir to a list of Intent objects (api_ai_graphs.intent)
    if not conf.DEFAULT_INTENTS_PATH:
        raise Exception("Please define an intents path in the user_settings.py file")

    choice = int(input('output(1) or input(2) \n'))

    if choice == 1:
        var = 'Choose to what language you want to translate the agent (en, pt, etc) '
        intents = load(conf.DEFAULT_INTENTS_PATH, str(input(var)))
        output_file(intents)
    elif choice == 2:
        intents = load(conf.DEFAULT_INTENTS_PATH, False)
        intents = input_file(intents)
        dump(conf.DEFAULT_INTENTS_PATH, intents)
