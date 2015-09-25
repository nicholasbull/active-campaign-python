
from Config import ACTIVECAMPAIGN_URL, ACTIVECAMPAIGN_API_KEY
from ActiveCampaign import ActiveCampaign
import json
import urllib2, urllib

class Contact(ActiveCampaign):

    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key
        ActiveCampaign.__init__(self, url, api_key)

    def add(self, params, post_data):
        request_url = '%s&api_action=contact_add&api_output=%s' % (self.url, self.output)
        if params:
            request_url = '%s&%s' % (request_url, params)
        post_data = urllib.urlencode(post_data)
        req = urllib2.Request(request_url, post_data)
        response = json.loads(urllib2.urlopen(req).read())
        return response

    def automation_list(self, params, post_data = {}):
        request_url = '%s&api_action=contact_automation_list&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def delete(self, params, post_data = {}):
        request_url = '%s&api_action=contact_delete&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def delete_list(self, params, post_data = {}):
        request_url = '%s&api_action=contact_delete_list&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def edit(self, params, post_data):
        request_url = '%s&api_action=contact_edit&api_output=%s&%s' % (self.url, self.output, params)
        post_data = urllib.urlencode(post_data)
        req = urllib2.Request(request_url, post_data)
        response = json.loads(urllib2.urlopen(req).read())
        return response

    def list(self, params, post_data = {}):
        request_url = '%s&api_action=contact_list&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def note_add(self, params, post_data = {}):
        request_url = '%s&api_action=contact_note_add&api_output=%s' % (self.url, self.output)
        if params:
            request_url = '%s&%s' % (request_url, params)
        post_data = urllib.urlencode(post_data)
        req = urllib2.Request(request_url, post_data)
        response = json.loads(urllib2.urlopen(req).read())
        return response

    def note_delete(self, params, post_data = {}):
        request_url = '%s&api_action=contact_note_delete&api_output=%s' % (self.url, self.output)
        if params:
            request_url = '%s&%s' % (request_url, params)
        post_data = urllib.urlencode(post_data)
        req = urllib2.Request(request_url, post_data)
        response = json.loads(urllib2.urlopen(req).read())
        return response

    def note_edit(self, params, post_data):
        request_url = '%s&api_action=contact_note_edit&api_output=%s&%s' % (self.url, self.output, params)
        post_data = urllib.urlencode(post_data)
        req = urllib2.Request(request_url, post_data)
        response = json.loads(urllib2.urlopen(req).read())
        return response

    def paginator(self, params, post_data = {}):
        request_url = '%s&api_action=contact_paginator&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def sync(self, params, post_data):
        request_url = '%s&api_action=contact_sync&api_output=%s' % (self.url, self.output)
        if params:
            request_url = '%s&%s' % (request_url, params)
        post_data = urllib.urlencode(post_data)
        req = urllib2.Request(request_url, post_data)
        response = json.loads(urllib2.urlopen(req).read())
        return response

    def tag_add(self, params, post_data = {}):
        request_url = '%s&api_action=contact_tag_add&api_output=%s' % (self.url, self.output)
        if params:
            request_url = '%s&%s' % (request_url, params)
        post_data = urllib.urlencode(post_data)
        req = urllib2.Request(request_url, post_data)
        response = json.loads(urllib2.urlopen(req).read())
        return response

    def tag_remove(self, params, post_data = {}):
        request_url = '%s&api_action=contact_tag_remove&api_output=%s' % (self.url, self.output)
        if params:
            request_url = '%s&%s' % (request_url, params)
        post_data = urllib.urlencode(post_data)
        req = urllib2.Request(request_url, post_data)
        response = json.loads(urllib2.urlopen(req).read())
        return response

    def view(self, params, post_data = {}):
        if params.startswith('email='):
            action = 'subscriber_view_email'
        elif params.startswith('hash='):
            action = 'subscriber_view_hash'
        elif params.startswith('id='):
            action = 'subscriber_view'
        else:
            action = 'subscriber_view'
        request_url = '%s&api_action=%s&api_output=%s&%s' % (self.url, action, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

if __name__ == '__main__':
    ac = ActiveCampaign(ACTIVECAMPAIGN_URL,  ACTIVECAMPAIGN_API_KEY)

    ## add
##    contact = {
##        'email': 'person@example.com',
##        'first_name': 'John',
##        'last_name': 'Smith',
##        'p[1]': 1,
##        'status[1]': 1,
##    }
##    print ac.api('contact/add', contact)

    ## delete
##    print ac.api('contact/delete?id=10')

    ## delete_list
##    print ac.api('contact/delete_list?ids=9,11')

    ## edit
##    contact = {
##        'id': 12,
##        'email': 'person@example.com',
##        'first_name': 'Johnny',
##        'last_name': 'Smith',
##        'p[1]': 1,
##        'status[1]': 1
##    }
##    print ac.api('contact/edit', contact)

    ## list
##    print ac.api('contact/list?ids=1,12')

    ## paginator
##    print ac.api('contact/paginator?sort=&offset=0&limit=20&filter=0')

    ## sync
##    contact = {
##        'email': 'person@example.com',
##        'first_name': 'John',
##        'last_name': 'Smith',
##        'p[1]': 1,
##        'status[1]': 1,
##    }
##    print ac.api('contact/sync', contact)

    ## view id
##    print ac.api('contact/view?id=12')

    ## view email
##    print ac.api('contact/view?email=person@example.com')

    ## view hash
##    print ac.api('contact/view?hash=3eeda4735e93f5407fced5ed45ddae82')

    ## tag_add
##    tags = {
##        'email': 'person@example.com',
##        'tag': 'atag',
##    }
##    print ac.api('contact/tag_add', tags)

    ## tag_remove
##    tags = {
##        'email': 'person@example.com',
##        'tag': 'atag',
##    }
##    print ac.api('contact/tag_remove', tags)
