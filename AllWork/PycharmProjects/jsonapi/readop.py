import json

import requests
from cerberus import Validator

from config import BASE_URI
from assertpy import soft_assertions, assert_that

schema = {
    "fname": {'type': 'string'},
    "lname": {'type': 'string'},
    "person_id": {'type': 'integer'},
    "timestamp": {'type': 'string'}
}


def test_read_one_operation_has_expected_schema():
    response = requests.get(f'{BASE_URI}/1')
    person = json.loads(response.text)

    validator = Validator(schema)
    is_valid = validator.validate(person)

    assert_that(is_valid, description=validator.errors).is_true()


def test_read_all_operation_has_expected_schema():
    response = requests.get(BASE_URI)
    persons = json.loads(response.text)

    validator = Validator(schema, require_all=True)

    with soft_assertions():
        for person in persons:
            is_valid = validator.validate(person)
            assert_that(is_valid, description=validator.errors).is_true()