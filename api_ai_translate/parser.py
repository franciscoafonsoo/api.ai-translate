# !/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import json
from api_ai_translate.intent import Intent


def load_jsons(path, translate):
    """ Converts all JSON's given in path (inside 'intents) to a list of Intent Objects.

    :param translate:
    :param path: intent directory extrated from API.AI
    :type path: str
    :return: list of Intent objects.
    :rtype: list
    """

    data = dict()
    for i, filename in enumerate(os.listdir(path)):
        with open(path + '/' + filename, encoding="utf-8") as data_file:
            data[filename] = json.load(data_file)

    return [Intent(value, translate) for keys, value in data.items()]


def rebuild_jsons(path, lintents):
    """ Replace and output a list on Intents to valid API.AI JSON Files

    :param path: path to output files
    :param lintents: list of Intent objects
    """

    for intent in lintents:
        for x in intent.old.get('userSays'):
            for data in x.get('data'):
                for key in intent.usersays:
                    if len(data) == 1:
                        if not data.get('text') == ' ' and data.get('text') == key:
                            data['text'] = intent.usersays[key]
                    elif len(data) == 4:
                        pass

        speech = intent.old.get('responses')[0].get('messages')[0].get('speech')

        print("original: ")
        print(speech)
        print("new: ")
        print(intent.speech)

        for i in intent.speech:
            if type(speech) is list:
                for y in speech:
                    if y == i:
                        y = i
            else:
                if speech == i:
                    y = i

        with open(path + '/' + 'trans_' + intent.name + ".json", encoding="utf-8", mode='w+') as outfile:
            json.dump(intent.old, outfile)
