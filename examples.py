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
        'title': 'Custom Field',
        'type': 1, # 1 = Text Field, 2 = Text Box, 3 = Checkbox, 4 = Radio, 5 = Dropdown, 6 = Hidden field, 7 = List Box, 9 = Date
        'req': 0,
        'perstag': 'CUSTOM_F',
        'p[0]': 0
    }
    print ac.api('list/field_add', list_field)

    # add subscriber
    subscriber = {
        'email': 'person@example.com',
        'first_name': 'John',
        'last_name': 'Smith',
        'p[1]': 1,
        'status[1]': 1,
        'field[%CUSTOM_F%,0]': 'This is a field'
    }
    print ac.api('contact/sync', subscriber)

    # add note
    note = {
        'id': 1,
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
