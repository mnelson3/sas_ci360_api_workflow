#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

"""
Definitions Module
Contains operations for the workflow definitions
	1. get_definitions(self, **kwargs) -> requests.Response
	2. get_definition(self, definition_id: str) -> requests.Response
"""

import os
import unittest
from sasci360apiworkflow import definitions


class TestDefinitions(unittest.TestCase):

	def setUp(self) -> None:
		algorithm = "HS256"
		api = "/marketingWorkflow"
		encoding = "UTF-8"
		host = os.environ.get("CI360_HOST", "")
		secret_key = os.environ.get("CI360_SECRET_KEY", "")
		tenant_id = os.environ.get("CI360_TENANT_ID", "")

		self.definitions = definitions.Definitions(
			algorithm=algorithm,
			api=api,
			encoding=encoding,
			host=host,
			secret_key=secret_key,
			tenant_id=tenant_id
		)

	def test_get_definitions(self):
		"""
		1. get_definitions(self, **kwargs) -> requests.Response
		"""
		result = self.definitions.get_definitions()
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_definition(self):
		"""
		2. get_definition(self, definition_id: str) -> requests.Response
		"""
		definition_id = "0"
		result = self.definitions.get_definition(definition_id=definition_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)


if __name__ == "__main__":
	unittest.main()
