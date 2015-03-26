# An API to commmunicate with jsonservices.py

#import logging

#logging.basicConfig(filename='glintAPI.log', level=logging.DEBUG)

def getImages(USER_TOKEN, USER_TENANT):
   return USER_TOKEN, USER_TENANT 

def save(jsonMsg, USER_TOKEN, USER_TENANT):
    return jsonMsg, USER_TOKEN, USER_TENANT

def credentials(USER_TOKEN, USER_TENANT, USER_ID):
    return USER_TOKEN, USER_TENANT, USER_ID

def listSites(USER_TOKEN, USER_TENANT):
    return USER_TOKEN, USER_TENANT

def deleteSite(USER_TOKEN, USER_TENANT, USER_ID, SITE_ID):
    return USER_TOKEN, USER_TENANT, USER_ID, SITE_ID

def createSite(USER_TOKEN, USER_TENANT, USER_ID, SITEDATA):
    return USER_TOKEN, USER_TENANT, USER_ID, SITEDATA

def deleteCredential(USER_TOKEN, USER_TENANT, USER_ID, SITE_ID):
    return USER_TOKEN, USER_TENANT, USER_ID, SITE_ID

def getCredential(USER_TOKEN, USER_TENANT, USER_ID, SITE_ID):
    return USER_TOKEN, USER_TENANT, USER_ID, SITE_ID

def hasCredential(USER_TOKEN, USER_TENANT, USER_ID, SITE_ID, CK_TYPE):
    return USER_TOKEN, USER_TENANT, USER_ID, SITE_ID, CK_TYPE

def addCredential(USER_TOKEN, USER_TENANT, CREDDATA):
    return USER_TOKEN, USER_TENANT, CREDDATA
