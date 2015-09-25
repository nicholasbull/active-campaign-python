
from Config import ACTIVECAMPAIGN_URL, ACTIVECAMPAIGN_API_KEY
from ActiveCampaign import ActiveCampaign
import json
import urllib2, urllib

class Automation(ActiveCampaign):

    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key
        ActiveCampaign.__init__(self, url, api_key)

    def contact_add(self, params, post_data):
        request_url = '%s&api_action=automation_contact_add&api_output=%s' % (self.url, self.output)
        if params:
            request_url = '%s&%s' % (request_url, params)
        post_data = urllib.urlencode(post_data)
        req = urllib2.Request(request_url, post_data)
        response = json.loads(urllib2.urlopen(req).read())
        return response

    def contact_remove(self, params, post_data = {}):
        request_url = '%s&api_action=automation_contact_remove&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def contact_list(self, params, post_data = {}):
        request_url = '%s&api_action=automation_contact_list&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def list(self, params, post_data = {}):
        request_url = '%s&api_action=automation_list&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def view(self, params, post_data = {}):
        if params.startswith('contact_id='):
            action = 'subscriber_view'
        else:
            action = 'subscriber_view'
        request_url = '%s&api_action=%s&api_output=%s&%s' % (self.url, action, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

if __name__ == '__main__':
    ac = ActiveCampaign(ACTIVECAMPAIGN_URL,  ACTIVECAMPAIGN_API_KEY)
