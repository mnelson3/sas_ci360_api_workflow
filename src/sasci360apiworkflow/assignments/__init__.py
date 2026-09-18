#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import requests
from sasci360apiworkflow.base import Base


class Assignments(Base):
	"""
	Assignments Module
	Contains operations for the workflow assignments
		1. get_assignee(self, task_assignee_id: any) -> response
	"""

	def __init__(self, algorithm, api, encoding, host, secret_key, tenant_id) -> None:
		super().__init__(algorithm, api, encoding, host, secret_key, tenant_id)

	def get_assignee(self, task_assignee_id: any) -> requests.Response:
		"""
		Get a workflow task assignee
		:param task_assignee_id: required - The unique identifier for the workflow task assignee
		:return: Returns the representation of the specified workflow task assignee.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if task_assignee_id is None:
			raise Exception("Task Assignee ID is missing.")
		try:
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/taskAssignees/{0}".format(task_assignee_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result


if __name__ == "__main__":
	Assignments()
