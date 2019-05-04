import pytest
import requests
import logging


def test_x_wing():
    exp_res = 'X-wing'
    r = requests.get(url="https://swapi.co/api/starships/12/")
    assert r.json()["name"] == exp_res, "there is no X-wing ".format(r.json())
