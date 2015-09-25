from includes.ActiveCampaign import ActiveCampaign
from includes.Config import ACTIVECAMPAIGN_URL, ACTIVECAMPAIGN_API_KEY

if __name__ == '__main__':
    ac = ActiveCampaign(ACTIVECAMPAIGN_URL,  ACTIVECAMPAIGN_API_KEY)

    # add list
    list = {
        'name': 'A Subscripiton List',
        'get_unsubscribe_reason': 1,
        'sender_name': 'A Company',
        'sender_addr1': 'A Street There',
        'sender_zip': 'AA2 2AA',
        'sender_city': 'Manchester',
        'sender_country': 'United Kingdom',
        'sender_url': 'http://www.example.com/',
        'sender_reminder': 'You subscribed on our web site'
    }
    print ac.api('list/add', list)

    # add custom list field
    list_field = {
        'title': 'A Custom Field',
        'type': 1, # 1 = Text Field, 2 = Text Box, 3 = Checkbox, 4 = Radio, 5 = Dropdown, 6 = Hidden field, 7 = List Box, 9 = Date
        'req': 0,
        'perstag': 'CUSTOM_FIELD',
        'p[0]': 0
    }
    print ac.api('list/field_add', list_field)

    # add message
    message = {
        'id': 12,
        'format': 'html',
        'subject': 'Test Message',
        'fromemail': 'test@example.com',
        'fromname': 'John Doe',
        'priority': 1,
        'charset': 'utf-8',
        'htmlconstructor': 'external',
        'htmlfetch': 'http://notify.bartbania.co.uk/notification.php?segment=1&email=%EMAIL%',
        'htmlfetchwhen': 'send',
        'p[1]': 1,
    }
    print ac.api('message/add', message)

    # add campaign
    campaign = {
        'type': 'single',
        'segmentid': 0,
        'bounceid': 0,
        'name': 'ActiveCampaign TEST',
        'status': 1,
        'tracklinks': 'none',
        'trackreads': 1,
        'htmlunsub': 1,
        'p[1]': 1,
        'm[12]': 100
    }
    print ac.api('campaign/create', campaign)

    # add subscriber
    subscriber = {
        'email': 'person@example.com',
        'first_name': 'John',
        'last_name': 'Smith',
        'p[1]': 1,
        'status[1]': 1,
        'field[%CUSTOM_FIELD%,0]': 'This is a field'
    }
    print ac.api('contact/sync', subscriber)

    # add note
    note = {
        'email': 'person@example.com',
        'listid': 1,
        'note': 'here is my note'
    }
    print ac.api('contact/note_add', note)

    # add tag
    tag = {
        'email': 'person@example.com',
        'tags': 'Tag1, Tag2, Tag3'
    }
    print ac.api('contact/tag_add', tag)

    # campaign send
    send = {
        'email': 'person@example.com',
        'campaignid': 1,
        'messageid': 11,
        'action': 'send'
    }
    print ac.api('campaign/send', send)
