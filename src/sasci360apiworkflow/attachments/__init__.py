#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import requests
from sasci360apiworkflow.base import Base


class Attachments(Base):
	"""
	Attachments Module
	Contains operations for the workflow attachments
		1. get_attachments(self, process_id: any, task_id: any, **kwargs) -> requests.Response
		2. create_attachment(self, process_id: any, task_id: any, payload: dict, **kwargs) -> requests.Response
		3. create_attachment_with_file(self, process_id: any, task_id: any, file: object) -> requests.Response
		4. delete_attachment(self, process_id: any, task_id: any, attachment_id: any) -> requests.Response
		5. download_attachment(self, process_id: any, task_id: any, attachment_id: any) -> requests.Response
	"""

	def __init__(self, algorithm, api, encoding, host, secret_key, tenant_id) -> None:
		super().__init__(algorithm, api, encoding, host, secret_key, tenant_id)

	def get_attachments(self, process_id: any, task_id: any, **kwargs) -> requests.Response:
		"""
		Get a collection of attachments for a workflow task
		:param process_id: required - The unique identifier for the workflow process
		:param task_id: required - The unique identifier for the workflow task
		:keyword username: any, optional - The query parameter that specifies the filter on the user ID of the assignee. The workflow task attachments for the specified assignee are returned to the response
		:keyword type: any, required - The query parameter that specifies the filter on the type of attachments; the possible values are "response", "contributor attachment", or "initiator attachment"
		:keyword start: any, optional - The index of the first attachment that is returned
		:keyword limit: any, optional - The maximum number of attachments that can be returned
		:return: Returns a collection of attachments for the specified workflow task based on the options for pagination, filtering, and sorting. The items in the collection use the application/vnd.sas.marketing.workflow.task.summary media type.
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
		if kwargs["type"] is None:
			raise Exception("Type is missing.")
		try:
			query_string = "?"
			if "username" in kwargs:
				query_string.join("userName={0}&".format(kwargs["username"]))
			if "type" in kwargs:
				query_string.join("type={0}&".format(kwargs["type"]))
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
			api_path = "/processes/{0}/tasks/{1}/attachments{2}".format(process_id, task_id, res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def create_attachment(self, process_id: any, task_id: any, payload: dict, **kwargs) -> requests.Response:
		"""
		Create an attachment for the specified workflow task
		:param process_id: required - The unique identifier for the workflow process
		:param task_id: required - The unique identifier for the workflow task
		:param payload: required - The representation of a workflow task attachment
		:keyword type: The query parameter that specifies the type of the workflow task attachment; the possible values are "response", "contributor attachment", or "initiator attachment"
		:return: Creates a workflow task attachment based on the representation in the request body.
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
		if kwargs["type"] is None:
			raise Exception("Type is missing.")
		try:
			query_string = "?"
			if "type" in kwargs:
				query_string.join("type={0}&".format(kwargs["type"]))
			action = "POST"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			res_query_string = lambda x: x if len(x) > 1 else x[:-1]
			api_path = "/processes/{0}/tasks/{1}/attachments#withoutFile{2}".format(process_id, task_id, res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def create_attachment_with_file(self, process_id: any, task_id: any, file: object) -> requests.Response:
		"""
		Create an attachment by using the given file for the specified workflow task
		:param process_id: required - The unique identifier for the workflow process
		:param task_id: required - The unique identifier for the workflow task
		:param file: required -
		:return: Creates a new workflow task attachment based on the specified file data.
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
		try:
			action = "POST"
			data = file
			headers = {
				"Content-Type": "multipart/form-data; boundary={boundaryString}",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/processes/{0}/tasks/{1}/attachments#withFile".format(process_id, task_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def delete_attachment(self, process_id: any, task_id: any, attachment_id: any) -> requests.Response:
		"""
		Delete an attachment
		:param process_id: required - The unique identifier for the workflow process
		:param task_id: required - The unique identifier for the workflow task
		:param attachment_id: required - The unique identifier for the workflow task attachment
		:return: Deletes the specified attachment for the specified workflow task.
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
		if attachment_id is None:
			raise Exception("Attachment ID is missing.")
		try:
			action = "DELETE"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/processes/{0}/tasks/{1}/attachments/{2}".format(process_id, task_id, attachment_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def download_attachment(self, process_id: any, task_id: any, attachment_id: any) -> requests.Response:
		"""
		Download the workflow attachment
		:param process_id: required - The unique identifier for the workflow process
		:param task_id: required - The unique identifier for the workflow task
		:param attachment_id: required - The unique identifier for the workflow attachment
		:return: Downloads the specified attachment for the specified workflow task.
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
		if attachment_id is None:
			raise Exception("Attachment ID is missing.")
		try:
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/processes/{0}/tasks/{1}/attachments/{2}/download".format(process_id, task_id, attachment_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result


if __name__ == "__main__":
	Attachments()
