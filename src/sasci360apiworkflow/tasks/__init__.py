#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import requests
from sasci360apiworkflow.base import Base


class Tasks(Base):
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

	def __init__(self, algorithm, api, encoding, host, secret_key, tenant_id) -> None:
		super().__init__(algorithm, api, encoding, host, secret_key, tenant_id)

	def get_workflow_tasks(self, process_id: any, **kwargs) -> requests.Response:
		"""
		Get a collection of workflow tasks
		:param process_id: required - The unique identifier for the workflow process
		:keyword start: int, optional - The index of the first task that is returned
		:keyword limit: int, optional - The maximum number of tasks that can be returned
		:keyword task_definition_key: int, optional - The query parameter that specifies a filter on the workflow task definition key (task definition key in the workflow engine). The value provided for the taskDefinitionKey parameter is not case-sensitive
		:return: Returns a collection of workflow tasks for the specified workflow process based on the options for pagination, filtering, and sorting. The items in the collection use the application/vnd.sas.marketing.workflow.task.summary media type.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if process_id is None:
			raise Exception("Process ID is missing.")
		try:
			query_string = "?"
			if "start" in kwargs:
				query_string.join("start={0}&".format(kwargs["start"]))
			if "limit" in kwargs:
				query_string.join("limit={0}&".format(kwargs["limit"]))
			if "task_definition_key" in kwargs:
				query_string.join("taskDefinitionKey={0}&".format(kwargs["task_definition_key"]))
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			res_query_string = lambda x: x if len(x) > 1 else x[:-1]
			api_path = "/processes/{0}/tasks{1}".format(process_id, res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def mark_workflow_task_complete(self, process_id: any, task_id: any, payload: dict, **kwargs) -> requests.Response:
		"""
		Mark a workflow task as complete
		:param process_id: required - The unique identifier for the workflow process
		:param task_id: required - The unique identifier for the workflow task
		:param payload: required - The representation of a workflow task that contains only one assignee. The assignee resource contains the comment attribute
		:keyword action: any, required - The query parameter that specifies the action to be taken for the workflow task. The value of the "action" parameter for the current API is "markAsComplete"
		:return: Marks the completion of the specified assignment in the workflow task by updating the comment that is passed with the assignee information in the request body.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if process_id is None:
			raise Exception("Process ID is missing.")
		if task_id is None:
			raise Exception("Task ID is missing.")
		if kwargs["action"] is None:
			raise Exception("Action is missing.")
		if kwargs["action"] != "markAsComplete":
			raise Exception("Action must equal cancel.")
		try:
			query_string = "?"
			if "action" in kwargs:
				query_string.join("action={0}&".format(kwargs["action"]))
			action = "POST"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			res_query_string = lambda x: x if len(x) > 1 else x[:-1]
			api_path = "/processes/{0}/tasks/{1}{2}".format(process_id, task_id, res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_workflow_tasks_contributor(self, **kwargs) -> requests.Response:
		"""
		Get a collection of workflow tasks for which the logged-in user is assigned as the contributor
		:keyword start: int, optional - The index of the first task to be returned
		:keyword limit: int, optional - The maximum number of tasks that can be returned
		:return: Returns a collection of workflow tasks based on the options for pagination, filtering, and sorting. The items in the collection use the application/vnd.sas.marketing.workflow.task.summary media type.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		try:
			query_string = "?"
			if "start" in kwargs:
				query_string.join("start={0}&".format(kwargs["start"]))
			if "limit" in kwargs:
				query_string.join("limit={0}&".format(kwargs["limit"]))
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			res_query_string = lambda x: x if len(x) > 1 else x[:-1]
			api_path = "/tasks/myTasks{0}".format(res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_workflow_task_contributor(self, task_id: any, **kwargs) -> requests.Response:
		"""
		Get a workflow task for which the logged-in user is assigned as the contributor
		:param task_id: required - The unique identifier for the workflow task
		:keyword assignment_id: any, optional - The query parameter that specifies a filter on the assignmentId. The filter is applied on the list of workflow task assignees to get the specified task assignment and the task response. An error is displayed if the assignmentId does not match any task assignments
		:return: Returns the representation of the specified workflow task.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if task_id is None:
			raise Exception("Task ID is missing.")
		if kwargs["assignment_id"] is None:
			raise Exception("Assignment ID is missing.")
		try:
			query_string = "?"
			if "assignment_id" in kwargs:
				query_string.join("assignmentId={0}&".format(kwargs["assignment_id"]))
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			res_query_string = lambda x: x if len(x) > 1 else x[:-1]
			api_path = "/tasks/myTasks/{0}{1}".format(task_id, res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_workflow_task(self, task_id: any, **kwargs) -> requests.Response:
		"""
		Get Workflow Task
		:param task_id: required - The unique identifier for the workflow task
		:keyword username: any, optional - The query parameter that specifies a filter on the user ID. The filter is applied on the assignee from the list of task assignees to retrieve the specified task assignment and the task response. An error is thrown if the userName does not match any assignee
		:return: Returns the representation of the specified workflow task.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if task_id is None:
			raise Exception("Task ID is missing.")
		if kwargs["username"] is None:
			raise Exception("User Name is missing.")
		try:
			query_string = "?"
			if "username" in kwargs:
				query_string.join("userName={0}&".format(kwargs["username"]))
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			res_query_string = lambda x: x if len(x) > 1 else x[:-1]
			api_path = "/tasks/{0}{1}".format(task_id, res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def update_workflow_task(self, task_id: any, payload: dict) -> requests.Response:
		"""
		Update a workflow task
		:param task_id: required - The unique identifier for the workflow task
		:param payload: required - The representation of a workflow task that contains only one assignee. The assignee resource contains the comment attribute
		:return: Updates the specified workflow task based on the representation in the request body.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if task_id is None:
			raise Exception("Task ID is missing.")
		try:
			action = "PUT"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/tasks/{0}".format(task_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result


if __name__ == "__main__":
	Tasks()
