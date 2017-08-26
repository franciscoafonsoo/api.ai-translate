# !/usr/bin/python3
# -*- coding: utf-8 -*-


def build_file(lintents):
	"""
	Build a file with all User Says and Speech based on a list of Intent Objects (from api_ai_translate.intent)

	:type lintents: list
	:param lintents: list of all intents
	"""
	with open('output.txt', 'a+') as out:
		for index, i in enumerate(lintents):
			for dont, e in enumerate(i.usersays):
				out.write(str(i) + '.' + str(e) + '\r\n')