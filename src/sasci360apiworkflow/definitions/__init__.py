#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import requests
from sasci360apiworkflow.base import Base


class Definitions(Base):
	"""
	Definitions Module
	Contains operations for the workflow definitions
		1. get_definitions(self, **kwargs) -> requests.Response
		2. get_definition(self, definition_id: str) -> requests.Response
	"""

	def __init__(self, algorithm, api, encoding, host, secret_key, tenant_id) -> None:
		super().__init__(algorithm, api, encoding, host, secret_key, tenant_id)

	def get_definitions(self, **kwargs) -> requests.Response:
		"""
		Get a collection of workflow definitions
		:keyword start: int, optional - The index of the first definition that is returned
		:keyword limit: int, optional - The maximum number of definitions that are returned
		:return: Returns a collection of workflow definitions based on the options for pagination, filtering, and sorting. The items in the collection use the application/vnd.sas.marketing.workflow.definition.summary media type.
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
			api_path = "/definitions{0}".format(res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_definition(self, definition_id: str) -> requests.Response:
		"""
		Get a workflow definition
		:param definition_id: required - The unique identifier for the workflow definition
		:return: Returns the representation of the specified workflow definition.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if definition_id is None:
			raise Exception("Definition ID is missing.")
		try:
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/definitions/{0}".format(definition_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result


if __name__ == "__main__":
	Definitions()
