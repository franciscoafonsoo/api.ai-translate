# !/usr/bin/python3
# -*- coding: utf-8 -*-
from collections import defaultdict
from functools import reduce
from googletrans import Translator


class Intent:
    def __init__(self, a, trans):
        """ Atributs for the Intent Object. Note: only using relevant atributes to build the graph

        :param a: json.load() from a file containting an intent
        :type a: dict
        """

        self.name = a.get('name')

        self.usersays = dict()
        self.reference = dict()
        translator = Translator()

        for x in a.get('userSays'):
            for data in x.get('data'):
                if len(data) == 1:
                    if not data.get('text') == ' ':
                        if trans:
                            self.usersays[data.get('text')] = \
                                translator.translate(data.get('text'), src='en', dest='pt').text
                        else:
                            self.usersays[data.get('text')] = data.get('text')
                elif len(data) == 4:
                    self.reference.update(data)
        self.speech = a.get('responses')[0].get('messages')[0].get('speech')

        self.old = a

    def __str__(self):
        """
        String representation of the class (copy and adapt prints from cli.py)
        :rtype: str
        """
        return self.name

    def __eq__(self, b):
        """
        first: All output contexts from 'b' also appear in 'a'
        second: 'b' user says is not empty OR 'b' is a fallback intent

        first AND second must be true.

        :type   b:  object
        :rtype   :  bool
        :param  b:  Intent Object
        """

        first = self.contextin[:len(b.contextout)] == b.contextout
        second = b.usersays or b.fallback

        return first and second


def search_cases(lintents):
    """
    Find 'User Cases' in the given intents. Returns a dict
    with the following format : {'usercase': list of intents}.
    If the intent doesn't have a usercase, it should be grouped
    in with the 'empty' name

    :param lintents: a list of intents
    :type lintents: list
    :return: defaultdict {'usercase': list of intents}
    :rtype: defaultdict
    """

    group = defaultdict(list)

    for index, intent in enumerate(lintents):
        for context in intent.usercase:
            if intent.usercase is '':
                group['empty'].append(intent)
            else:
                group[context].append(intent)

    return group


def replace_intents(lintents, load):
    for key in load.keys():
        for intent in lintents:
            for usersays in intent.usersays:
                if usersays == key:
                    intent.usersays[usersays] = load[key]
    return lintents
