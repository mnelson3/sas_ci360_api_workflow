#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

"""
Processes Module
Contains operations for the workflow processes
	1. get_processes(self, **kwargs) -> requests.Response
	2. create_process(self, payload: dict, **kwargs) -> requests.Response
	3. get_process(self, process_id: any) -> requests.Response
	4. cancel_process(self, process_id: any, payload: dict, **kwargs) -> requests.Response
	5. update_process(self, process_id: any, payload: dict, **kwargs) -> requests.Response
	6. delete_process(self, process_id: any) -> requests.Response
"""

import os
import unittest
from sasci360apiworkflow import processes


class TestProcesses(unittest.TestCase):

	def setUp(self) -> None:
		algorithm = "HS256"
		api = "/marketingWorkflow"
		encoding = "UTF-8"
		host = os.environ.get("CI360_HOST", "")
		secret_key = os.environ.get("CI360_SECRET_KEY", "")
		tenant_id = os.environ.get("CI360_TENANT_ID", "")

		self.processes = processes.Processes(
			algorithm=algorithm,
			api=api,
			encoding=encoding,
			host=host,
			secret_key=secret_key,
			tenant_id=tenant_id
		)

	def test_get_processes(self):
		"""
		1. get_processes(self, **kwargs) -> requests.Response
		"""
		result = self.processes.get_processes()
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_create_process(self):
		"""
		2. create_process(self, payload: dict, **kwargs) -> requests.Response
		"""
		payload = {
			"id": "22e935e2-460d-4527-987e-a9e6ee014c4a",
			"name": "New Product Launch Workflow",
			"version": 1,
			"code": "200420201208",
			"description": "Description for new product launch",
			"ownerName": "fSsXQ7DNCN15pKyW8FF7f4nMVqvsoyh2",
			"createdUserName": "fSsXQ7DNCN15pKyW8FF7f4nMVqvsoyh2",
			"createdBy": "demouser",
			"createdByName": "fSsXQ7DNCN15pKyW8FF7f4nMVqvsoyh2",
			"creationTimeStamp": "2020-12-01T08:44:24Z",
			"lastModifiedBy": "demouser",
			"lastModifiedByName": "fSsXQ7DNCN15pKyW8FF7f4nMVqvsoyh2",
			"lastModifiedTimeStamp": "2020-12-01T08:44:24Z",
			"processDefinitionId": "f4075806-eed6-45c9-a931-f7ce34fa0da6",
			"submittedTimeStamp": "2020-12-01T08:44:24Z",
			"state": "INPROGRESS",
			"localizedState": "Pending",
			"comment": "some comment",
			"businessInformation": {},
			"numberOfTasks": "4",
			"workflowType": "GENERIC",
			"category": "category",
			"plannedEndTimeStamp": "2020-12-01T08:44:24Z",
			"projectedEndTimeStamp": "2020-12-07T09:23:55Z",
			"startTimeStamp": "2020-12-01T08:44:24Z",
			"endTimeStamp": "2020-12-07T09:23:55Z",
			"timelineCalculationTimeStamp": "2020-12-07T09:23:55Z",
			"percentComplete": 70,
			"delayedBy": 0,
			"submittedBy": {},
			"mappedGroupMembers": [
				{
					"name": "demouser",
					"displayName": "fSsXQ7DNCN15pKyW8FF7f4nMVqvsoyh2",
					"type": "USER",
					"members": [{}]
				}
			],
			"tasks": [
				{
					"id": "ea0f7d8c-c925-4b0d-8078-1ed9b00f4064",
					"name": "Approve Artwork For Generated Artwork",
					"version": 1,
					"description": "Description for task",
					"initiatorUserName": "fSsXQ7DNCN15pKyW8FF7f4nMVqvsoyh2",
					"lastModifiedTimeStamp": "2020-12-01T08:44:24Z",
					"key": "idApproverTask",
					"processId": "45c3f71c-1580-4e4d-ac21-3accdc9abb6e",
					"processName": "Promotion Revision Workflow",
					"processCode": "200320200908",
					"workflowType": "GENERIC",
					"sequential": False,
					"businessInformation": {},
					"processDefinitionId": "72563198-889a-4e86-9a56-e8bca63f04a0",
					"taskTypeForLink": "MyTask",
					"taskType": "ITEMAPPROVAL",
					"internalTaskType": "USER_TASK",
					"versionNumber": 1,
					"isLatest": True,
					"locallyUpdated": True,
					"processSubmittedBy": {},
					"state": "NOT_INITIATED",
					"localizedState": "Not initiated",
					"multipleAssigneesSupported": False,
					"instruction": "some instruction",
					"projectedStartTimeStamp": "2020-12-01T08:44:24Z",
					"projectedEndTimeStamp": "2020-12-07T09:23:55Z",
					"startedTimeStamp": "2020-12-01T08:44:24Z",
					"endTimeStamp": "2020-12-07T09:23:55Z",
					"dueTimeStamp": "2020-12-01T08:44:24Z",
					"percentComplete": 0,
					"delayedBy": 0,
					"defaultDurationPerAssignee": "3",
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
			],
			"customAttributes": {},
			"links": [
				{
					"method": "GET",
					"rel": "self",
					"href": "https://extapigwservice-<server>/<endpoint>/",
					"uri": "/<endpoint>", "type": "application/vnd.sas.collection"
				}
			]
		}
		result = self.processes.create_process(payload=payload)
		print(result)
		self.assertIsNotNone(result)

	def test_get_process(self):
		"""
		3. get_process(self, process_id: any) -> requests.Response
		"""
		process_id = 0
		result = self.processes.get_process(process_id=process_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_cancel_process(self):
		"""
		4. cancel_process(self, process_id: any, payload: dict, **kwargs) -> requests.Response
		"""
		process_id = 0
		payload = {
			"id": "17e38990-3640-6008-1602-01ef1h7ef319",
			"name": "Workflow for New Product Launch",
			"version": 1,
			"code": "310320202359",
			"createdUserName": "fSsXQ7DNCN15pKyW8FF7f4nMVqvsoyh2",
			"createdBy": "demouser",
			"createdByName": "fSsXQ7DNCN15pKyW8FF7f4nMVqvsoyh2",
			"lastModifiedBy": "demouser",
			"lastModifiedByName": "fSsXQ7DNCN15pKyW8FF7f4nMVqvsoyh2",
			"lastModifiedTimeStamp": "2020-12-01T08:44:24Z",
			"submittedBy": {},
			"submittedTimeStamp": "2020-12-01T08:44:24Z",
			"state": "SAVEASDRAFT",
			"localizedState": "Pending",
			"percentComplete": 0,
			"delayedBy": 1,
			"businessInformation": {},
			"numberOfTasks": "4",
			"workflowType": "GENERIC",
			"plannedEndTimeStamp": "2020-12-01T08:44:24Z",
			"projectedEndTimeStamp": "2020-12-07T09:23:55Z",
			"startTimeStamp": "2020-12-01T08:44:24Z",
			"endTimeStamp": "2020-12-07T09:23:55Z",
			"timelineCalculationTimeStamp": "2020-12-07T09:23:55Z",
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
		result = self.processes.cancel_process(process_id=process_id, payload=payload)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)
		pass

	def test_update_process(self) -> None:
		"""
		5. update_process(self, process_id: any, payload: dict, **kwargs) -> requests.Response
		"""
		process_id = 0
		payload = {
			"id": "22e935e2-460d-4527-987e-a9e6ee014c4a",
			"name": "New Product Launch Workflow",
			"version": 1,
			"code": "200420201208",
			"description": "Description for new product launch",
			"ownerName": "fSsXQ7DNCN15pKyW8FF7f4nMVqvsoyh2",
			"createdUserName": "fSsXQ7DNCN15pKyW8FF7f4nMVqvsoyh2",
			"createdBy": "demouser",
			"createdByName": "fSsXQ7DNCN15pKyW8FF7f4nMVqvsoyh2",
			"creationTimeStamp": "2020-12-01T08:44:24Z",
			"lastModifiedBy": "demouser",
			"lastModifiedByName": "fSsXQ7DNCN15pKyW8FF7f4nMVqvsoyh2",
			"lastModifiedTimeStamp": "2020-12-01T08:44:24Z",
			"processDefinitionId": "f4075806-eed6-45c9-a931-f7ce34fa0da6",
			"submittedTimeStamp": "2020-12-01T08:44:24Z",
			"state": "INPROGRESS",
			"localizedState": "Pending",
			"comment": "some comment",
			"businessInformation": {},
			"numberOfTasks": "4",
			"workflowType": "GENERIC",
			"category": "category",
			"plannedEndTimeStamp": "2020-12-01T08:44:24Z",
			"projectedEndTimeStamp": "2020-12-07T09:23:55Z",
			"startTimeStamp": "2020-12-01T08:44:24Z",
			"endTimeStamp": "2020-12-07T09:23:55Z",
			"timelineCalculationTimeStamp": "2020-12-07T09:23:55Z",
			"percentComplete": 70,
			"delayedBy": 0,
			"submittedBy": {},
			"mappedGroupMembers": [
				{
					"name": "demouser",
					"displayName": "fSsXQ7DNCN15pKyW8FF7f4nMVqvsoyh2",
					"type": "USER",
					"members": [{}]
				}
			],
			"tasks": [
				{
					"id": "ea0f7d8c-c925-4b0d-8078-1ed9b00f4064",
					"name": "Approve Artwork For Generated Artwork",
					"version": 1, "description": "Description for task",
					"initiatorUserName": "fSsXQ7DNCN15pKyW8FF7f4nMVqvsoyh2",
					"lastModifiedTimeStamp": "2020-12-01T08:44:24Z",
					"key": "idApproverTask",
					"processId": "45c3f71c-1580-4e4d-ac21-3accdc9abb6e",
					"processName": "Promotion Revision Workflow",
					"processCode": "200320200908",
					"workflowType": "GENERIC",
					"sequential": False,
					"businessInformation": {},
					"processDefinitionId": "72563198-889a-4e86-9a56-e8bca63f04a0",
					"taskTypeForLink": "MyTask",
					"taskType": "ITEMAPPROVAL",
					"internalTaskType": "USER_TASK",
					"versionNumber": 1,
					"isLatest": True,
					"locallyUpdated": True, "processSubmittedBy": {},
					"state": "NOT_INITIATED",
					"localizedState": "Not initiated",
					"multipleAssigneesSupported": False,
					"instruction": "some instruction",
					"projectedStartTimeStamp": "2020-12-01T08:44:24Z",
					"projectedEndTimeStamp": "2020-12-07T09:23:55Z",
					"startedTimeStamp": "2020-12-01T08:44:24Z",
					"endTimeStamp": "2020-12-07T09:23:55Z",
					"dueTimeStamp": "2020-12-01T08:44:24Z",
					"percentComplete": 0, "delayedBy": 0,
					"defaultDurationPerAssignee": "3",
					"links": [
						{
							"method": "GET", "rel": "self", "href": "https://extapigwservice-<server>/<endpoint>/", "uri": "/<endpoint>", "type": "application/vnd.sas.collection"
						}
					]
				}
			],
			"customAttributes": {},
			"links": [{"method": "GET", "rel": "self", "href": "https://extapigwservice-<server>/<endpoint>/", "uri": "/<endpoint>", "type": "application/vnd.sas.collection"}]
		}
		launch_process = None
		result = self.processes.update_process(process_id=process_id, payload=payload, launch_process=launch_process)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_delete_process(self):
		"""
		6. delete_process(self, process_id: any) -> requests.Response
		"""
		process_id = 0
		result = self.processes.delete_process(process_id=process_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)


if __name__ == "__main__":
	unittest.main()
