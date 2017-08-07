

from requests import Session, request
from ConfigParser import SafeConfigParser, NoSectionError 

class Connection(Session):
    """
        Connection object is a Session object, give a name and authentication endpoint.
        If you don't need to authenticate it should work without. An .ini file is required.
    """
    def __init__(self, name, authEndpoint):
        self.name = name
        super(Connection, self).__init__()
        self.stream = False
        self.parser = SafeConfigParser()
        self.parser.read('../gateConfigs.ini') 

        self.authEndpoint = authEndpoint
        self.authResponse = None 
        self.__auth_setup__()
        
        
    def __auth_setup__(self):
        """
            Runs one time at object instantiation, needs to be mutatable.
        """
        try: 
            credentials = {'email':self.parser.get('SiteCredentials', 'email'), 
                           'password':self.parser.get('SiteCredentials', 'password')}
        except NoSectionError, e:
            print "[-] gateConfigs.ini file missing or incomplete" 
            credentials = {}
 
        self.authResponse = self.connect(self.authEndpoint, credentials=credentials)
        return None


    def connect(self, endpoint, credentials={}):
        """
            Connect should check for an auth response and do some exception handling.
        """ 
        # TODO: Something smart here. 
        response = self.post(endpoint, credentials)
        print "[*] Connection response: " .format(response.status_code)
        return response


    def send_form_post(self, endpoint, dPostPayload):
        """ For sending to forms, like babalooey.com"""
        self.headers.update({"Content-Type":"application/x-www-form-urlencoded"})
        return self.post(endpoint, dPostPayload)


    def send_json_post(self, endpoint, dPostPayload):
        """ For sending to json endpoints, like GSlvts server."""
        self.headers.update({"Content-Type":"application/json"})
        return self.post(endpoint, dPostPayload)
    
   
    def send_get(self, endpoint):
        return self.get(endpoint)



