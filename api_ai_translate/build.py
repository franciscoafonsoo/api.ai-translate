# !/usr/bin/python3
# -*- coding: utf-8 -*-
from api_ai_translate.parser import translate_jsons
from api_ai_translate.intent import replace_intents


def output_file(lintents):
    """
    Build a file with all User Says and Speech based on a list of Intent Objects (from api_ai_translate.intent)

    :type lintents: list
    :param lintents: list of all intents
    """
    dump = set()
    for index, i in enumerate(lintents):
        for endex, e in enumerate(i.usersays):
            e = e.strip()
            dump.add(e)

    with open(file='output.txt', mode='w+', encoding='utf-8') as out:
        for index, i in enumerate(dump):
            out.write(str(i) + '=\r\n')


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
            before, after = before.strip(), after.strip()
            if line and after:
                load[before] = after

    return replace_intents(lintents, load)
