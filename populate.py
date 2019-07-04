"""
Mock data generator and web hook methods tester
"""

import json
from random import choice

import requests
from mimesis import Generic

WEBHOOK_URL = 'http://127.0.0.1:8000/webhook/'
API_URL = 'http://127.0.0.1:8000/api/contacts/'


def get_persons():
    """
    Get list of contacts via API
    :return: list of records with persons data in JSON format
    """
    resp = requests.get(API_URL).content
    persons = json.loads(resp)
    return persons


def request(parameters):
    """
    Send POST to webhook
    :param parameters: event type, person data
    :return: none
    """
    resp = requests.post(WEBHOOK_URL, json.dumps(parameters),
                         headers={"Content-Type": "application/json", "Accept": "application/json"})
    print(parameters, resp)


def make_random(language):
    """
    Generate mock data
    :param language: language to use
    :return: dict
    """
    generic = Generic(language)
    first_name = generic.person.name()
    last_name = generic.person.surname()
    email = generic.person.email()
    phone_number = generic.person.telephone(mask="+#############")
    birth_date = str(generic.datetime.date())
    mock = {"first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone_number": phone_number,
            "birth_date": birth_date}
    return mock


def populate(iterations):
    """
    Create n == iterations records in database
    :param iterations: num of records
    :return: none
    """
    for _ in range(iterations):
        person = make_random('en')
        params = {"event": "contact.add",
                  "data": person}
        request(params)


def update(max_iterations):
    """
    Update records in database
    :param max_iterations: MAXIMUM (look at random choice) number of updated records
    :return: none
    """
    persons = get_persons()
    count = 0
    for person in persons:
        if count > max_iterations:
            return
        count += 1
        if choice([0, 1]):
            new_person = make_random('en')
            new_person['id'] = person['id']
            params = {"event": "contact.update",
                      "data": new_person}
            request(params)


def delete(max_iterations):
    """
    Delete records in database
    :param max_iterations: max_iterations: MAXIMUM (look at random choice) number of deleted records
    :return: none
    """
    persons = get_persons()
    count = 0
    for person in persons:
        if count > max_iterations:
            return
        count += 1
        if choice([0, 1]):
            params = {"event": "contact.delete",
                      "data": {"id": person['id']}}
            request(params)


if __name__ == '__main__':
    populate(0)
    update(10)
    delete(0)
