#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

"""
Tasks Module
Contains operations for the workflow tasks
	1. get_workflow_tasks(self, process_id: any, **kwargs) -> requests.Response
	2. mark_workflow_task_complete(self, process_id: any, task_id: any, payload: dict, **kwargs) -> requests.Response
	3. get_workflow_tasks_contributor(self, **kwargs) -> requests.Response
	4. get_workflow_task_contributor(self, task_id: any, **kwargs) -> requests.Response
	5. get_workflow_task(self, task_id: any, **kwargs) -> requests.Response
	6. update_workflow_task(self, task_id: any, payload: dict) -> requests.Response
"""

import os
import unittest
from sasci360apiworkflow import tasks


class TestTasks(unittest.TestCase):

	def setUp(self) -> None:
		algorithm = "HS256"
		api = "/marketingWorkflow"
		encoding = "UTF-8"
		host = os.environ.get("CI360_HOST", "")
		secret_key = os.environ.get("CI360_SECRET_KEY", "")
		tenant_id = os.environ.get("CI360_TENANT_ID", "")

		self.tasks = tasks.Tasks(
			algorithm=algorithm,
			api=api,
			encoding=encoding,
			host=host,
			secret_key=secret_key,
			tenant_id=tenant_id
		)

	def test_get_workflow_tasks(self):
		"""
		1. get_workflow_tasks(self, process_id: any, **kwargs) -> requests.Response
		"""
		process_id = 0
		result = self.tasks.get_workflow_tasks(process_id=process_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_mark_workflow_task_complete(self):
		"""
		2. mark_workflow_task_complete(self, process_id: any, task_id: any, payload: dict, **kwargs) -> requests.Response
		"""
		process_id = 0
		task_id = 0
		payload = {
			"id": "3a50d7d9-d9ea-4e78-994a-95896debd1ce",
			"name": "Review information and Generated content",
			"version": 1,
			"description": "Description for task",
			"createdUserName": "fSsXQ7DNCN15pKyW8FF7f4nMVqvsoyh2",
			"createdBy": "demouser",
			"creationTimeStamp": "2020-12-01T08:44:24Z",
			"lastModifiedBy": "demouser",
			"lastModifiedByName": "fSsXQ7DNCN15pKyW8FF7f4nMVqvsoyh2",
			"lastModifiedTimeStamp": "2020-12-01T08:44:24Z",
			"ownerName": "fSsXQ7DNCN15pKyW8FF7f4nMVqvsoyh2",
			"owner": "demouser",
			"key": "idMultipleContributer",
			"taskType": "GENERIC",
			"internalTaskType": "USER_TASK",
			"category": "category",
			"sourceItemFieldValues": [
				{
					"items": [
						{
							"id": "8343fba0-6288-4305-8725-7b6dc03b8d7d",
							"refObjectId": "ee3ccc80-31ce-4d93-bde1-ce04738b8e16",
							"objectType": "cirest.SVC.PLANNER.PlanningObjects",
							"relatedObjects": [{}],
							"referenceAttachment": {},
							"objectApprovalRequired": True,
							"approvalInfo": {},
							"customAttributeInfo": {}
						}
					]
				}
			],
			"businessInformation": {},
			"versionNumber": 1,
			"isLatest": True,
			"locallyUpdated": True,
			"sequential": False,
			"processDefinitionId": "f4075806-eed6-45c9-a931-f7ce34fa0da6",
			"processId": "6061d6e0-a39e-4068-8147-c3d3c66e3644",
			"processName": "Content Production Workflow",
			"processCode": "310320202359",
			"processState": "PENDING",
			"approvalState": "APPROVED",
			"processSubmittedBy": {},
			"workflowType": "GENERIC",
			"state": "PENDING",
			"localizedState": "Pending",
			"multipleAssigneesSupported": False,
			"instruction": "some instruction",
			"comment": "some comment",
			"projectedStartTimeStamp": "2020-12-01T08:44:24Z",
			"projectedEndTimeStamp": "2020-12-07T09:23:55Z",
			"startedTimeStamp": "2020-12-01T08:44:24Z",
			"endTimeStamp": "2020-12-07T09:23:55Z",
			"dueTimeStamp": "2020-12-07T09:23:55Z",
			"percentComplete": 0,
			"delayedBy": 7,
			"defaultDurationPerAssignee": "2",
			"assignees": [
				{
					"id": "caf94645-7725-4728-bd70-36c4e291be22",
					"name": "Assignee1",
					"version": 1,
					"description": "Description for task assignee",
					"createdUserName": "fSsXQ7DNCN15pKyW8FF7f4nMVqvsoyh2",
					"createdBy": "demouser",
					"creationTimeStamp": "2020-12-01T08:44:24Z",
					"lastModifiedBy": "demouser",
					"lastModifiedTimeStamp": "2020-12-01T08:44:24Z",
					"ownerName": "fSsXQ7DNCN15pKyW8FF7f4nMVqvsoyh2",
					"category": "category",
					"state": "PENDING",
					"localizedState": "Pending",
					"approvalState": "APPROVED",
					"assignedToUser": True,
					"projectedStartTimeStamp": "2020-12-01T08:44:24Z",
					"projectedEndTimeStamp": "2020-12-07T09:23:55Z",
					"instruction": "some instruction",
					"comment": "some comment",
					"initiatorComment": "initiator added comment",
					"replaced": False,
					"assignee": {},
					"groups": ["group1", "group2"],
					"candidateGroups": ["candidategroup1", "candidategroup2"],
					"duration": "6",
					"startTimeStamp": "2020-12-01T08:44:24Z",
					"endTimeStamp": "2020-12-07T09:23:55Z",
					"dueTimeStamp": "2020-12-07T09:23:55Z",
					"delayedBy": 2,
					"attachmentFileCount": 0,
					"responseAttachmentCount": 0,
					"replacementDetails": {},
					"customAttributes": {},
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
					"uri": "/<endpoint>",
					"type": "application/vnd.sas.collection"
				}
			]
		}
		result = self.tasks.mark_workflow_task_complete(process_id=process_id, task_id=task_id, payload=payload)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_workflow_tasks_contributor(self):
		"""
		3. get_workflow_tasks_contributor(self, **kwargs) -> requests.Response
		"""
		result = self.tasks.get_workflow_tasks_contributor()
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_workflow_task_contributor(self):
		"""
		4. get_workflow_task_contributor(self, task_id: any, **kwargs) -> requests.Response
		"""
		task_id = 0
		result = self.tasks.get_workflow_task_contributor(task_id=task_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_workflow_task(self):
		"""
		5. get_workflow_task(self, task_id: any, **kwargs) -> requests.Response
		"""
		task_id = 0
		result = self.tasks.get_workflow_task(task_id=task_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_update_workflow_task(self):
		"""
		6. update_workflow_task(self, task_id: any, payload: dict) -> requests.Response
		"""
		task_id = 0
		payload = {
			"id": "3a50d7d9-d9ea-4e78-994a-95896debd1ce",
			"name": "Review information and Generated content",
			"version": 1,
			"description": "Description for task",
			"createdUserName": "fSsXQ7DNCN15pKyW8FF7f4nMVqvsoyh2",
			"createdBy": "demouser",
			"creationTimeStamp": "2020-12-01T08:44:24Z",
			"lastModifiedBy": "demouser",
			"lastModifiedByName": "fSsXQ7DNCN15pKyW8FF7f4nMVqvsoyh2",
			"lastModifiedTimeStamp": "2020-12-01T08:44:24Z",
			"ownerName": "fSsXQ7DNCN15pKyW8FF7f4nMVqvsoyh2",
			"owner": "demouser",
			"key": "idMultipleContributer",
			"taskType": "GENERIC",
			"internalTaskType": "USER_TASK",
			"category": "category",
			"sourceItemFieldValues": [
				{
					"items": [
						{
							"id": "8343fba0-6288-4305-8725-7b6dc03b8d7d",
							"refObjectId": "ee3ccc80-31ce-4d93-bde1-ce04738b8e16",
							"objectType": "cirest.SVC.PLANNER.PlanningObjects",
							"relatedObjects": [{}],
							"referenceAttachment": {},
							"objectApprovalRequired": True,
							"approvalInfo": {},
							"customAttributeInfo": {}
						}
					]
				}
			],
			"businessInformation": {},
			"versionNumber": 1,
			"isLatest": True,
			"locallyUpdated": True,
			"sequential": False,
			"processDefinitionId": "f4075806-eed6-45c9-a931-f7ce34fa0da6",
			"processId": "6061d6e0-a39e-4068-8147-c3d3c66e3644",
			"processName": "Content Production Workflow",
			"processCode": "310320202359",
			"processState": "PENDING",
			"approvalState": "APPROVED",
			"processSubmittedBy": {},
			"workflowType": "GENERIC",
			"state": "PENDING",
			"localizedState": "Pending",
			"multipleAssigneesSupported": False,
			"instruction": "some instruction",
			"comment": "some comment",
			"projectedStartTimeStamp": "2020-12-01T08:44:24Z",
			"projectedEndTimeStamp": "2020-12-07T09:23:55Z",
			"startedTimeStamp": "2020-12-01T08:44:24Z",
			"endTimeStamp": "2020-12-07T09:23:55Z",
			"dueTimeStamp": "2020-12-07T09:23:55Z",
			"percentComplete": 0,
			"delayedBy": 7,
			"defaultDurationPerAssignee": "2",
			"assignees": [
				{
					"id": "caf94645-7725-4728-bd70-36c4e291be22",
					"name": "Assignee1",
					"version": 1,
					"description": "Description for task assignee",
					"createdUserName": "fSsXQ7DNCN15pKyW8FF7f4nMVqvsoyh2",
					"createdBy": "demouser",
					"creationTimeStamp": "2020-12-01T08:44:24Z",
					"lastModifiedBy": "demouser",
					"lastModifiedTimeStamp": "2020-12-01T08:44:24Z",
					"ownerName": "fSsXQ7DNCN15pKyW8FF7f4nMVqvsoyh2",
					"category": "category",
					"state": "PENDING",
					"localizedState": "Pending",
					"approvalState": "APPROVED",
					"assignedToUser": True,
					"projectedStartTimeStamp": "2020-12-01T08:44:24Z",
					"projectedEndTimeStamp": "2020-12-07T09:23:55Z",
					"instruction": "some instruction",
					"comment": "some comment",
					"initiatorComment": "initiator added comment",
					"replaced": False, "assignee": {},
					"groups": ["group1", "group2"],
					"candidateGroups": ["candidategroup1", "candidategroup2"],
					"duration": "6",
					"startTimeStamp": "2020-12-01T08:44:24Z",
					"endTimeStamp": "2020-12-07T09:23:55Z",
					"dueTimeStamp": "2020-12-07T09:23:55Z",
					"delayedBy": 2,
					"attachmentFileCount": 0,
					"responseAttachmentCount": 0,
					"replacementDetails": {},
					"customAttributes": {},
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
					"uri": "/<endpoint>",
					"type": "application/vnd.sas.collection"
				}
			]
		}
		result = self.tasks.update_workflow_task(task_id=task_id, payload=payload)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)


if __name__ == "__main__":
	unittest.main()
