# !/usr/bin/python3
# -*- coding: utf-8 -*-
import json
from api_ai_translate.intent import replace_intents


def output_file(lintents):
    """
    Output two files with all User Says  and References based on a list of Intent Objects (from api_ai_translate.intent)

    :type lintents: list
    :param lintents: list of all intents
    """
    speech = dict()
    usersays = dict()
    reference = list()

    for i in lintents:
        if i.usersays:
            usersays.update(i.usersays)
        if i.reference:
            reference.append(i.reference)
        if i.speech:
            for s in i.speech:
                if s not in speech.keys():
                    speech.update(i.speech)

    # clear duplicate entries
    reference = [dict(t) for t in set([tuple(d.items()) for d in reference])]

    with open(file='usersays.txt', mode='w+', encoding='utf-8') as out:
        json.dump(usersays, out)

    with open(file='reference.txt', mode='w+', encoding='utf-8') as out:
        json.dump(reference, out)

    with open(file='speech.txt', mode='w+', encoding='utf-8') as out:
        json.dump(speech, out)


def input_file(lintents):
    """
    Load the translated file with all User Says (from api_ai_translate.build.output_file)

    :type lintents: list
    :param lintents: list of all intents
    """

    load = dict()
    with open(file='usersays.txt', mode='r+', encoding='utf-8') as f:
        load = json.load(f)

    return replace_intents(lintents, load)
