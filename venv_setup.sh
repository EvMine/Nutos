#!/bin/bash
python -m venv venv.
echo created venv
venv/scripts/pip install pytest
echo pytest installed
venv/scripts/pip install teamcity-messages
echo TC-messages installed
venv/scripts/pip install requests
venv/scripts/pip install allure-pytest
echo requests installed
