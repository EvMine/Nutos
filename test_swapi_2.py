import pytest
import requests
import logging


def test_luke():
    exp_res = 'Luke Skywalker'
    r = requests.get(url="https://swapi.co/api/people/12/")
    logger = logging.getLogger()
    logger.warning('There is name in JSON response: {}'.format(r.json()['name']))
    assert r.json()["name"] == exp_res, "there is no Luke Skywalker ".format(r.json())
