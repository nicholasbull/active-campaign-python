
from Config import ACTIVECAMPAIGN_URL, ACTIVECAMPAIGN_API_KEY
from ActiveCampaign import ActiveCampaign
import json
import urllib2, urllib

class Deal(ActiveCampaign):

    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key
        ActiveCampaign.__init__(self, url, api_key)

    def add(self, params, post_data):
        request_url = '%s&api_action=deal_add&api_output=%s' % (self.url, self.output)
        if params:
            request_url = '%s&%s' % (request_url, params)
        post_data = urllib.urlencode(post_data)
        req = urllib2.Request(request_url, post_data)
        response = json.loads(urllib2.urlopen(req).read())
        return response

    def delete(self, params, post_data = {}):
        request_url = '%s&api_action=deal_delete&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def list(self, params, post_data = {}):
        request_url = '%s&api_action=deal_list&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def get(self, params, post_data = {}):
        request_url = '%s&api_action=deal_get&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def edit(self, params, post_data):
        request_url = '%s&api_action=deal_edit&api_output=%s&%s' % (self.url, self.output, params)
        post_data = urllib.urlencode(post_data)
        req = urllib2.Request(request_url, post_data)
        response = json.loads(urllib2.urlopen(req).read())
        return response

    def note_edit(self, params, post_data):
        request_url = '%s&api_action=deal_note_edit&api_output=%s' % (self.url, self.output)
        if params:
            request_url = '%s&%s' % (request_url, params)
        post_data = urllib.urlencode(post_data)
        req = urllib2.Request(request_url, post_data)
        response = json.loads(urllib2.urlopen(req).read())
        return response

    def note_add(self, params, post_data = {}):
        request_url = '%s&api_action=deal_note_add&api_output=%s' % (self.url, self.output)
        if params:
            request_url = '%s&%s' % (request_url, params)
        post_data = urllib.urlencode(post_data)
        req = urllib2.Request(request_url, post_data)
        response = json.loads(urllib2.urlopen(req).read())
        return response

if __name__ == '__main__':
    ac = ActiveCampaign(ACTIVECAMPAIGN_URL,  ACTIVECAMPAIGN_API_KEY)
