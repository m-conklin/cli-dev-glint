# An API to commmunicate with jsonservices.py

#import logging

#logging.basicConfig(filename='glintAPI.log', level=logging.DEBUG)

class glint_api(object):
    
    def __init__(self, api_log, debug_level, api_yaml):
        self.log = api_log
        self.debug = debug_level
        self.yaml = api_yaml

    def define(self):
        self.c =2

    def getImages(self, USER_TOKEN, USER_TENANT, USER_ID):
        if USER_TOKEN !=  "" and USER_TENANT != "" and USER_ID != "":
            return USER_TOKEN, USER_TENANT, USER_ID

    def save(self, jsonMsg, USER_TOKEN, USER_TENANT):
        return jsonMsg, USER_TOKEN, USER_TENANT

    def credentials(self, USER_TOKEN, USER_TENANT, USER_ID):
        return USER_TOKEN, USER_TENANT, USER_ID

    def listSites(self, USER_TOKEN, USER_TENANT):
        return USER_TOKEN, USER_TENANT

    def deleteSite(self, USER_TOKEN, USER_TENANT, USER_ID, SITE_ID):
        return USER_TOKEN, USER_TENANT, USER_ID, SITE_ID

    def createSite(self, USER_TOKEN, USER_TENANT, USER_ID, SITEDATA):
        return USER_TOKEN, USER_TENANT, USER_ID, SITEDATA

    def deleteCredential(self, USER_TOKEN, USER_TENANT, USER_ID, SITE_ID):
        return USER_TOKEN, USER_TENANT, USER_ID, SITE_ID

    def getCredential(self, USER_TOKEN, USER_TENANT, USER_ID, SITE_ID):
        return USER_TOKEN, USER_TENANT, USER_ID, SITE_ID

    def hasCredential(self, USER_TOKEN, USER_TENANT, USER_ID, SITE_ID, CK_TYPE):
        return USER_TOKEN, USER_TENANT, USER_ID, SITE_ID, CK_TYPE

    def addCredential(self, USER_TOKEN, USER_TENANT, CREDDATA):
        return USER_TOKEN, USER_TENANT, CREDDATA
