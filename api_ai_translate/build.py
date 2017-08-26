# !/usr/bin/python3
# -*- coding: utf-8 -*-
output = set()
cenas = dict()


def output_file(lintents):
    """
    Build a file with all User Says and Speech based on a list of Intent Objects (from api_ai_translate.intent)

    :type lintents: list
    :param lintents: list of all intents
    """

    for index, i in enumerate(lintents):
        for endex, e in enumerate(i.usersays):
            e = e.strip()
            output.add(e)

    with open(file='output.txt', mode='w+', encoding='utf-8') as out:
        for index, i in enumerate(output):
            out.write(str(i) + '=\r\n')


def input_file():

    with open(file='output.txt', mode='r+', encoding='utf-8') as file:
        for line in file:
            before = line.split('=')[0]
            after = line.split('=')[1]
            before = before.strip()
            after = after.strip()
            if line and after:
                cenas[before] = after
                output.add(before)

    print (cenas)