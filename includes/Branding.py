
from Config import ACTIVECAMPAIGN_URL, ACTIVECAMPAIGN_API_KEY
from ActiveCampaign import ActiveCampaign
import json
import urllib2, urllib

class Branding(ActiveCampaign):

    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key
        ActiveCampaign.__init__(self, url, api_key)

    def edit(self, params, post_data):
        request_url = '%s&api_action=branding_edit&api_output=%s' % (self.url, self.output)
        if params:
            request_url = '%s&%s' % (request_url, params)
        post_data = urllib.urlencode(post_data)
        req = urllib2.Request(request_url, post_data)
        response = json.loads(urllib2.urlopen(req).read())
        return response

    def view(self, params, post_data = {}):
        request_url = '%s&api_action=%s&api_output=%s&%s' % (self.url, action, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response


if __name__ == '__main__':
    ac = ActiveCampaign(ACTIVECAMPAIGN_URL,  ACTIVECAMPAIGN_API_KEY)

# Variables
# site_name                     Title of software. Example: 'ActiveCampaign Email Marketing'
# site_logo                     URL of logo. Large logos appear on the login page.
# sit e_logo_small              URL of small logo. Small logos appear in the header of the admin panel.
# branding_header_html_val      Content of non-removable header. Example: <p>header content here</p>
# branding_footer_html_val      Content of non-removeable footer. Example: <p>footer content here</p>
# header_text_value             Content of non-removable header. Example: text header content
# footer_text_value             Content of non-removeable footer. Example: text footer cntent
# links                         External links. To enable (which is the default) exclude this parameter entirely.
#                               To disable (remove our branding), just pass this parameter with any value.
# admin_template                The actual HTML template (ONLY AVAILABLE FOR CERTAIN PLANS)
# admin_style                   The actual CSS. Example: test color: green; (ONLY AVAILABLE FOR CERTAIN PLANS)
# public_template               The actual HTML templat  e (ONLY AVAILABLE FOR CERTAIN PLANS)
# public_style                  The actual CSS. Example: test color: green; (ONLY AVAILABLE FOR CERTAIN PLANS)
# result_code                   Whether or not the request was successful. Examples: 1 = yes, 0 = no
# result_message                A custom message that appears explaining what happened. Example: Design Settings updated
# result_output                 The result output used. Example: serialize
