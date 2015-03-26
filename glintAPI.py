# An API to commmunicate with jsonservices.py

#import logging

#logging.basicConfig(filename='glintAPI.log', level=logging.DEBUG)

class glint_api(object):
    
    def __init__(self, api_log, debug_level, api_yaml):
        self.log = api_log
        self.debug = debug_level
        self.yaml = api_yaml
        self.USER_TOKEN = 'userToken'
        self.USER_TENANT = 'userTenant'
        self.USER_ID = 'userId'
        
    def define(self):
        self.c =2

    def getImages(self):
        if self.USER_TOKEN and self.USER_TENANT and self.USER_ID:
            return 'Images'

    def save(self, JSON_MESSAGE):
        return JSON_MESSAGE

    def credentials(self):
        return 'Credentials'

    def listSites(self):
        return 'List of sites'

    def deleteSite(self, SITE_ID):
        return 'Deleted site %s.'%SITE_ID

    def createSite(self, SITEDATA):
        return 'Created site with %s.'%SITEDATA

    def deleteCredential(self, SITE_ID):
        return 'Deleted credential %s.'%SITE_ID

    def getCredential(self, SITE_ID):
        return 'Credential for site %s.'%SITE_ID

    def hasCredential(self, SITE_ID, CK_TYPE):
        return 'Has credential for %s of type %s.'%(SITE_ID, CK_TYPE)

    def addCredential(self,CREDDATA):
        return 'Added credential %s.'%CREDDATA
