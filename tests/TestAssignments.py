#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

"""
Assignments Module
Contains operations for the workflow assignments
	1. get_assignee(self, task_assignee_id: any) -> response
"""

import os
import unittest
from sasci360apiworkflow import assignments


class TestAssignments(unittest.TestCase):

	def setUp(self) -> None:
		algorithm = "HS256"
		api = "/marketingWorkflow"
		encoding = "UTF-8"
		host = os.environ.get("CI360_HOST", "")
		secret_key = os.environ.get("CI360_SECRET_KEY", "")
		tenant_id = os.environ.get("CI360_TENANT_ID", "")

		self.assignments = assignments.Assignments(
			algorithm=algorithm,
			api=api,
			encoding=encoding,
			host=host,
			secret_key=secret_key,
			tenant_id=tenant_id
		)

	def test_get_assignee(self):
		"""
		1. get_assignee(self, task_assignee_id: any) -> response
		"""
		task_assignee_id = 0
		result = self.assignments.get_assignee(task_assignee_id=task_assignee_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)


if __name__ == "__main__":
	unittest.main()
