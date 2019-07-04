from contacts.models import Contact


def contact_add(event):
    first_name = event['data']['first_name']
    last_name = event['data']['last_name']
    phone_number = event['data']['phone_number']
    email = event['data']['email']
    birth_date = event['data']['birth_date']
    contact = Contact(first_name=first_name, last_name=last_name, phone_number=phone_number, email=email,
                      birth_date=birth_date)
    contact.save()
    return


def contact_update(event):
    try:
        contact_id = event['data']['id']
    except KeyError:
        print('No id for update record')
        return
    try:
        contact = Contact.objects.get(id=contact_id)
    except:
        print(f'No such record {contact_id}')
        return
    setattr(contact, 'first_name', event['data']['first_name'])
    setattr(contact, 'last_name', event['data']['last_name'])
    setattr(contact, 'phone_number', event['data']['phone_number'])
    setattr(contact, 'email', event['data']['email'])
    setattr(contact, 'birth_date', event['data']['birth_date'])
    contact.save()
    return


def contact_delete(event):
    try:
        contact_id = event['data']['id']
    except KeyError:
        print('No id for delete record')
        return
    try:
        contact_to_delete = Contact.objects.get(id=contact_id)
    except:
        print(f'No such record {contact_id}')
        return
    contact_to_delete.delete()
    return
