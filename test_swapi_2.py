import pytest
import requests


def test_luke():
    exp_res = 'Luke Skywalker'
    r = requests.get(url="https://swapi.co/api/people/12/")
    assert r.json()["name"] == exp_res, "there is no Luke Skywalker in: ".format(r.json())
