from Config import ACTIVECAMPAIGN_URL, ACTIVECAMPAIGN_API_KEY
from ActiveCampaign import ActiveCampaign
import simplejson as json
import urllib2, urllib
import datetime, time

class Automation(ActiveCampaign):

    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key
        ActiveCampaign.__init__(self, url, api_key)

    def list(self, params, post_data = {}):
        request_url = '%s&api_action=automation_list&api_output=%s%s' % (self.url, self.output)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def contact_list(self, params, post_data = {}):
        request_url = '%s&api_action=automation_contact_list&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def contact_view(self, params, post_data = {}):
        request_url = '%s&api_action=automation_contact_view&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def contact_remove(self, params, post_data = {}):
        request_url = '%s&api_action=automation_contact_remove&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def contact_add(self, params, post_data = {}):
        request_url = '%s&api_action=automation_contact_add&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

if __name__ == '__main__':
    ac = ActiveCampaign(ACTIVECAMPAIGN_URL,  ACTIVECAMPAIGN_API_KEY)
