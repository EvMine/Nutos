import pytest
import requests


def test_SWAPI():
    exp_res = 'Wilhuff Tarkin'
    r = requests.get(url="https://swapi.co/api/people/12/")
    assert r.json()["name"] == exp_res
