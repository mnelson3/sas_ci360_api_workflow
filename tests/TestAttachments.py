#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

"""
Attachments Module
Contains operations for the workflow attachments
	1. get_attachments(self, process_id: any, task_id: any, **kwargs) -> requests.Response
	2. create_attachment(self, process_id: any, task_id: any, payload: dict, **kwargs) -> requests.Response
	3. create_attachment_with_file(self, process_id: any, task_id: any, file: object) -> requests.Response
	4. delete_attachment(self, process_id: any, task_id: any, attachment_id: any) -> requests.Response
	5. download_attachment(self, process_id: any, task_id: any, attachment_id: any) -> requests.Response
"""

import os
import unittest
from sasci360apiworkflow import attachments


class TestAttachments(unittest.TestCase):

	def setUp(self) -> None:
		algorithm = "HS256"
		api = "/marketingWorkflow"
		encoding = "UTF-8"
		host = os.environ.get("CI360_HOST", "")
		secret_key = os.environ.get("CI360_SECRET_KEY", "")
		tenant_id = os.environ.get("CI360_TENANT_ID", "")

		self.attachments = attachments.Attachments(
			algorithm=algorithm,
			api=api,
			encoding=encoding,
			host=host,
			secret_key=secret_key,
			tenant_id=tenant_id
		)

	def test_get_attachments(self):
		"""
		1. get_attachments(self, process_id: any, task_id: any, **kwargs) -> requests.Response
		"""
		process_id = 0
		task_id = 0
		result = self.attachments.get_attachments(process_id=process_id, task_id=task_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_create_attachment(self):
		"""
		2. create_attachment(self, process_id: any, task_id: any, payload: dict, **kwargs) -> requests.Response
		"""
		process_id = 0
		task_id = 0
		payload = {
			"id": "9cef745c-1f81-48de-b97d-722b130e6d51",
			"name": "ProductLaunchPromo.jpg",
			"version": 1,
			"creationTimeStamp": "2020-12-01T08:44:24Z",
			"referenceId": "9cef745c-1f81-48de-b97d-722b130e6d51",
			"type": "CONTRIBUTOR_ATTACHMENT",
			"contentType": "FILE",
			"additionalInformation": {},
			"file": {},
			"mediaType": "application/vnd.sas.marketing.workflow.attachment",
			"links": [
				{
					"method": "GET",
					"rel": "self",
					"href": "https://extapigwservice-<server>/<endpoint>/",
					"uri": "/<endpoint>",
					"type": "application/vnd.sas.collection"
				}
			]
		}
		attachment_type = "response"
		# attachment_type = "contributor attachment"
		# attachment_type = "initiator attachment"
		result = self.attachments.create_attachment(process_id=process_id, task_id=task_id, payload=payload, type=attachment_type)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_create_attachment_with_file(self):
		"""
		3. create_attachment_with_file(self, process_id: any, task_id: any, file: object) -> requests.Response
		"""
		process_id = 0
		task_id = 0
		file = "<PATH-TO_FILE>"
		result = self.attachments.create_attachment_with_file(process_id=process_id, task_id=task_id, file=file)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_delete_attachment(self):
		"""
		4. delete_attachment(self, process_id: any, task_id: any, attachment_id: any) -> requests.Response
		"""
		process_id = 0
		task_id = 0
		attachment_id = 0
		result = self.attachments.delete_attachment(process_id=process_id, task_id=task_id, attachment_id=attachment_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_download_attachment(self):
		"""
		5. download_attachment(self, process_id: any, task_id: any, attachment_id: any) -> requests.Response
		"""
		process_id = 0
		task_id = 0
		attachment_id = 0
		result = self.attachments.download_attachment(process_id=process_id, task_id=task_id, attachment_id=attachment_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)


if __name__ == "__main__":
	unittest.main()
