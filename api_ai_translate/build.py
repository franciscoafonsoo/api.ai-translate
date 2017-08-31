# !/usr/bin/python3
# -*- coding: utf-8 -*-
import json
from api_ai_translate.parser import translate_jsons
from api_ai_translate.intent import replace_intents


def output_file(lintents):
    """
    Build a file with all User Says and Speech based on a list of Intent Objects (from api_ai_translate.intent)

    :type lintents: list
    :param lintents: list of all intents
    """
    usersays = dict()
    reference = list()

    for i in lintents:
        usersays.update(i.usersays)
        if i.reference:
            reference.append(i.reference)

    reference = [dict(t) for t in set([tuple(d.items()) for d in reference])]

    with open(file='usersays.txt', mode='w+', encoding='utf-8') as out:
        json.dump(usersays, out)
        # for index, i in enumerate(usersays):
        #    out.write("'" + str(i) + "'=\r\n")
    with open(file='reference.txt', mode='w+', encoding='utf-8') as out:
        json.dump(reference, out)
        # for endex, e in enumerate(reference):
        # out.write(str(e) + '\r\n')


def input_file(lintents):
    """
    Load a file with all User Says and Speech based on the file created by api_ai_translate.build.output_file

    :type lintents: list
    :param lintents: list of all intents
    """

    load = dict()
    with open(file='output.txt', mode='r+', encoding='utf-8') as f:
        for line in f:
            before, after = line.split('=')
            if line and after:
                load[before] = after

    return replace_intents(lintents, load)
