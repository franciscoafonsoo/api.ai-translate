# !/usr/bin/python3
# -*- coding: utf-8 -*-

from pysettings import conf

import api_ai_translate # load this app settings in first place

from pyforms import BaseWidget
from pyforms.Controls import ControlDir
from pyforms.Controls import ControlCombo
from pyforms.Controls import ControlButton
# from pyforms.Controls import ControlText

import pyforms

from api_ai_translate.parser import load_jsons   as load
from api_ai_translate.build import build_file  as build
from api_ai_translate.intent import search_cases as search


class ApiAI(BaseWidget):
	def __init__(self):
		super(ApiAI, self).__init__('API.AI Translate')

		# Definition of the forms fields
		self._intent_dir = ControlDir('Open Intents Folder', 'path')

		if conf.DEFAULT_INTENTS_PATH:
			self._intent_dir.value = conf.DEFAULT_INTENTS_PATH

		self._load_intents = ControlButton('Load Intents')
		self._user_cases = ControlCombo('User Cases')
		self._build_file = ControlButton('Show File')

		# Define the button action
		self._load_intents.value = self.__button_load
		self._build_file.value = self.__button_build

		# Define the organization of the forms
		self.formset = [('_intent_dir', '_load_intents', ' '),
		                ('_user_cases', '_build_file', ' '),
		                ' '
		                ]
		# The ' ' is used to indicate that a empty space should be placed at the bottom of the window
		# If you remove the ' ' the forms will occupy the entire window

	def __button_load(self):
		"""_load_intent button action event"""
		allintents = search(load(self._intent_dir.value))

		for index, elements in enumerate(allintents):
			self._user_cases.add_item(elements, allintents[elements])

	def __button_build(self):
		"""_build_graph button action event"""
		build(self._user_cases.value)


# Execute the application
if __name__ == "__main__":
	pyforms.start_app(ApiAI, [100, 100, 500, 450])
