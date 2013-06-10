#!/usr/bin/env python
import requests
from requests.exceptions import RequestException, Timeout, ConnectionError


class BadStatus(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)


class ClientTweet(object):

    @staticmethod
    def get_tweets():
        """Function get tweets with api"""
        url = 'http://search.twitter.com/search.json'
        headers = {
            'content-type': 'application/x-www-form-urlencoded'}
        data_send = {
            'q': 'tonsquemisa',
            'count': 5}
        try:
            response = requests.get(url, data_send, headers, headers)
        except RequestException:
            raise
        except Timeout:
            raise
        except ConnectionError:
            raise
        if response.status_code is 200:
            return response
        else:
            raise BadStatus('Service returned %d' % (response.status_code))
