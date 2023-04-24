from requests import request
import json
import logging


class RequestApi:

    @classmethod
    def get(cls, url: str, headers, payload: json):
        """
        Get all from external api.
        :param url: service url.
        :param headers: headers to send.
        :param payload: data to send.
        :return: list of json.
        """
        try:
            if payload is None:
                return request('GET', url, headers=headers, json=payload).json()
            else:
                return request('GET', url, headers=headers).json()
        except Exception as e:
            logging.error(e)

    @classmethod
    def post(cls, url: str, payload: json):
        """
        Post all from external api.
        :param url: service url.
        :param payload: data to send.
        :return: list of json.
        """
        try:
            return request('POST', url, json=payload).json()
        except Exception as e:
            logging.error(e)
