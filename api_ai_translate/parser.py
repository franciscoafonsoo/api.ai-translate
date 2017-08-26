# !/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import json
from api_ai_translate.intent import Intent


def load_jsons(path):
    """ Converts all JSON's given in path (inside 'intents) to a list of Intent Objects.

    :param path: intent directory extrated from API.AI
    :type path: str
    :return: list of Intent objects.
    :rtype: list
    """

    data = dict()

    for i, filename in enumerate(os.listdir(path)):
        with open(path + '/' + filename, encoding="utf-8") as data_file:
            data[filename] = json.load(data_file)

    return [Intent(value) for keys, value in data.items()]


def translate_jsons(path, lintents):
    data = dict()

    for i, filename in enumerate(os.listdir(path)):
        with open(path + '/' + filename, encoding="utf-8") as data_file:
            data[filename] = json.load(data_file)

    for f in data:
        for intent in lintents:
            if intent.name in f:
                for index, i in enumerate(data[f]['userSays']):
                    for dex, e in enumerate(intent.old):
                        if i['data'][0]['text'] == e:
                            i['data'][0]['text'] = intent.old[e]
        with open(path + '/' + 'trans_' + f, encoding="utf-8", mode='w+') as outfile:
            json.dump(data[f], outfile)
