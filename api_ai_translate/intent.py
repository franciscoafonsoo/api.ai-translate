# !/usr/bin/python3
# -*- coding: utf-8 -*-
import re
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
        self.speech = dict()
        translator = Translator()

        for x in a.get('userSays'):
            for data in x.get('data'):
                if len(data) == 1:
                    if not data.get('text') == ' ':
                        if trans:
                            self.usersays[data.get('text')] = \
                                translator.translate(data.get('text'), src='en', dest=trans).text
                        else:
                            self.usersays[data.get('text')] = data.get('text')
                elif len(data) == 4:
                    self.reference.update(data)

        speech = a.get('responses')[0].get('messages')[0].get('speech')

        if trans:
            if type(speech) is list:
                for i in speech:
                    if not re.match(r'.*[\%\$\^\*\@\_\-\(\)\:\;\'\"\{\}\[\]].*', i):
                        self.speech[i] = translator.translate(i, src='en', dest=trans).text
                    else:
                        self.speech[i] = ''
            else:
                if not re.match(r'.*[\%\$\^\*\@\_\-\(\)\:\;\'\"\{\}\[\]].*', speech):
                    self.speech[speech] = translator.translate(speech, src='en', dest=trans).text
                else:
                    self.speech[speech] = ''

        self.old = a

    def __str__(self):
        """
        String representation of the class (copy and adapt prints from cli.py)
        :rtype: str
        """
        return self.name


def replace(lintents, usersays, speech, reference):

    for intent in lintents:
        # first iteration (usersays)
        for key in usersays.keys():
            for us in intent.usersays:
                if us == key:
                    intent.usersays[us] = usersays[key]
        # second iteration (speech)
        for key in speech.keys():
            for sp in intent.speech:
                if sp == key:
                    intent.speech[sp] = speech[key]
        # third iteration (reference)
        # for key in reference.keys():
        #     for rf in intent.reference:
        #         if rf == key:
        #             intent.reference = reference[key]

    # old code, trying to improve to cycle less
    # for key in usersays.keys():
    #     for intent in lintents:
    #         for usersays in intent.usersays:
    #             if usersays == key:
    #                 intent.usersays[usersays] = usersays[key]

    return lintents
