#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import requests
from sasci360apiworkflow.base import Base


class Processes(Base):
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

	def __init__(self, algorithm, api, encoding, host, secret_key, tenant_id) -> None:
		super().__init__(algorithm, api, encoding, host, secret_key, tenant_id)

	def get_processes(self, **kwargs) -> requests.Response:
		"""
		Get a collection of workflow processes
		:keyword start: any, optional - The index of the first workflow process that is returned
		:keyword limit: any, optional - The maximum number of workflow processes that can be returned
		:keyword workflowType: any, optional - The query parameter that is used to specify a filter on the workflow process type. The value of the workflowType parameter is not case-sensitive
		:keyword state: any, optional - The query parameter that is used to specify a filter on the workflow process state. The value of the state parameter is not case-sensitive
		:keyword businessKey: any, optional - The query parameter that is used to specify a filter on the business key. The value of the businessKey parameter is not case-sensitive
		:return: Returns a collection of workflow processes based on the options for pagination, filtering, and sorting. The items in the collection use the application/vnd.sas.marketing.workflow.process.summary media type.
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
			if "workflow_type" in kwargs:
				query_string.join("workflowType={0}&".format(kwargs["workflow_type"]))
			if "state" in kwargs:
				query_string.join("state={0}&".format(kwargs["state"]))
			if "business_key" in kwargs:
				query_string.join("businessKey={0}&".format(kwargs["business_key"]))
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			res_query_string = lambda x: x if len(x) > 1 else x[:-1]
			api_path = "/processes{0}".format(res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def create_process(self, payload: dict, **kwargs) -> requests.Response:
		"""
		Create a new workflow process and initiate the workflow process
		:param payload: required - The representation of a workflow process
		:keyword launch_process: any, optional - The query parameter that specifies whether to create and initiate the new process, or only to create the new process. If the value for this parameter is set to "true", the new workflow process is created and initiated. In this case the return type is "vnd.sas.marketing.workflow.process.summary". If the value is set to "false" the new workflow process is created but not initiated. In this case the return type is "vnd.sas.marketing.workflow.process"
		:return: Creates a new workflow process based on the representation in the request body. The same API is also used to initiate the newly created workflow process if the query parameter, "launchProcess" is set to "true".
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		try:
			query_string = "?"
			if "launch_process" in kwargs:
				query_string.join("launchProcess={0}&".format(kwargs["launch_process"]))
			action = "POST"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			res_query_string = lambda x: x if len(x) > 1 else x[:-1]
			api_path = "/processes{0}".format(res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_process(self, process_id: any) -> requests.Response:
		"""
		Get a workflow process
		:param process_id: required - The unique identifier for the workflow process
		:return: Returns the representation of the specified workflow process.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if process_id is None:
			raise Exception("Process ID is missing.")
		try:
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/processes/{0}".format(process_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def cancel_process(self, process_id: any, payload: dict, **kwargs) -> requests.Response:
		"""
		Cancel a workflow process
		:param process_id: required - The unique identifier for the workflow process
		:param payload: required - The representation of a workflow process
		:keyword action: any, required - The query parameter that specifies the action to be taken for the workflow process. The value for the "action" parameter for this API is "cancel"
		:return: Cancels the specified workflow process by updating the comment passed in the request body.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if process_id is None:
			raise Exception("Process ID is missing.")
		if kwargs["action"] is None:
			raise Exception("Action is missing.")
		if kwargs["action"] != "cancel":
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
			api_path = "/processes/{0}{1}".format(process_id, res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.conn(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def update_process(self, process_id: any, payload: dict, **kwargs) -> requests.Response:
		"""
		Update a workflow process and initiate the workflow process
		:param process_id: required - The unique identifier for the workflow process
		:param payload: required - The representation of a workflow process
		:keyword launch_process: any, required - The query parameter that specifies whether to initiate the workflow process
		:return: Updates the specified workflow process based on the representation in the request body. The same API is also used to initiate the workflow process if the query parameter "launchProcess" is set to "true".
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if process_id is None:
			raise Exception("Process ID is missing.")
		if kwargs["launch_process"] is None:
			raise Exception("Launch Process is missing.")
		try:
			query_string = "?"
			if "launch_process" in kwargs:
				query_string.join("launchProcess={0}&".format(kwargs["launch_process"]))
			action = "PUT"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			res_query_string = lambda x: x if len(x) > 1 else x[:-1]
			api_path = "/processes/{0}{1}".format(process_id, res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def delete_process(self, process_id: any) -> requests.Response:
		"""
		Delete a workflow process
		:param process_id: required - The unique identifier for the workflow process
		:return: Deletes the specified workflow process.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if process_id is None:
			raise Exception("Process ID is missing.")
		try:
			action = "DELETE"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/processes/{0}".format(process_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result


if __name__ == "__main__":
	Processes()
