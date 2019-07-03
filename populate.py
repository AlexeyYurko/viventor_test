import json

import requests
from mimesis import Generic

url = 'http://127.0.0.1:8000/api/webhooks/'
generic = Generic('en')
for _ in range(2):
    first_name = generic.person.name()
    last_name = generic.person.surname()
    email = generic.person.email()
    phone_number = generic.person.telephone(mask="+#############")
    birth_date = str(generic.datetime.date())
    params = {"hook": {"event": "contact.added", "target": 'http://127.0.0.1:8000/api/contacts/'},
              "data": {"first_name": first_name,
                       "last_name": last_name,
                       "email": email,
                       "phone_number": phone_number,
                       "birth_date": birth_date}}
    nparams = json.dumps(params)
    resp = requests.post(url, nparams, headers={"Content-Type": "application/json", "Accept": "application/json"})
