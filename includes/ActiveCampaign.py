
from Config import ACTIVECAMPAIGN_URL, ACTIVECAMPAIGN_API_KEY
from Connector import Connector

class ActiveCampaign(Connector):

    def __init__(self, url, api_key, api_user = '', api_pass = ''):
        self.url = url
        self.api_key = api_key
        Connector.__init__(self, url, api_key, api_user, api_pass)

    def api(self, path, post_data = {}):
        # IE: "contact/view"
        components = path.split('/')
        component = components[0]

        if '?' in components[1]:
            # query params appended to method
            # IE: contact/edit?overwrite=0
            method_arr = components[1].split('?')
            method = method_arr[0]
            params = method_arr[1]
        else:
            # just a method provided
            # IE: "contact/view
            if components[1]:
                method = components[1]
                params = ''
            else:
                return 'Invalid method.'

        # adjustments
        if component == 'branding':
            # reserved word
            component = 'design'
        elif component == 'sync':
            component = 'contact'
            method = 'sync'
        elif component == 'singlesignon':
            component = 'auth'

        class1 = '%s' % component.capitalize() # IE: "contact" becomes "contact"
        source_module = __import__(class1, globals(), locals(), [], -1) # import contact
        class1 = getattr(source_module, class1) # get contact
        class1 = class1(ACTIVECAMPAIGN_URL, ACTIVECAMPAIGN_API_KEY) # contact()
        # contact.view()

        if method == 'list':
            # reserved word
            method = 'list_'

        if method in dir(class1):
            return getattr(class1, method)(params, post_data)
        return None
