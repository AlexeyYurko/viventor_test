# Junior Django Developer Test - Medium

## Background

A client has requested that you create a contact list application for them in Django. The client wants to store the following information about each contact: first name, last name, phone number, email, birth date.

They want to populate the database from another piece of software they have. So they ask you to include a webhook that they will hit to add a customer to the database.

### Stack

- Django
- Django Rest Framework (Optional, but preferred)

### Test

- Create a model for the above contact list
- Create the webhook that will be used to populate this database

### Extra Credit

- If the client wants to update information about a contact, how will they achieve that?



## API
/api/contacts

returns list of contacts in JSON 

## Webhook
/webhook

request POST with JSON body

    {"event": type_of_event,
       "data": {"id": id, 
                 "first_name": first_name,
                 "last_name": last_name,
                 "email": email,
                 "phone_number": phone_number,
                 "birth_date": birth_date}}
    
type_of_event: 'contact.add', 'contact.update', 'contact.delete'
 

contact.add requires only person data
 
contact.update also needs record id
 
contact.delete needs only record id