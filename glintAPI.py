# An API to commmunicate with jsonservices.py

#import logging

#logging.basicConfig(filename='glintAPI.log', level=logging.DEBUG)

def getImages(USER_TOKEN, USER_TENANT):
   return USER_TOKEN, USER_TENANT 

def save(jsonMsg, USER_TOKEN, USER_TENANT):
    return jsonMsg, USER_TOKEN, USER_TENANT

def credentials(USER_TOKEN, USER_TENANT, USER_ID):
    return USER_TOKEN, USER_TENANT, USER_ID

def listsiteS(USER_TOKEN, USER_TENANT):
    return USER_TOKEN, USER_TENANT

def deletesite(USER_TOKEN, USER_TENANT, USER_ID, SITE_ID):
    return USER_TOKEN, USER_TENANT, USER_ID, SITE_ID

def createsite(USER_TOKEN, USER_TENANT, USER_ID, SITEDATA):
    return USER_TOKEN, USER_TENANT, USER_ID, SITEDATA

def deletecredential(USER_TOKEN, USER_TENANT, SITE_ID, USER_ID):
    return USER_TOKEN, USER_TENANT, SITE_ID, USER_ID

def getcredential(USER_TOKEN, USER_TENANT,SITE_ID, USER_ID):
    return USER_TOKEN, USER_TENANT,SITE_ID, USER_ID

def hascredential(USER_TOKEN, USER_TENANT, SITE_ID, USER_ID, CK_TYPE):
    return USER_TOKEN, USER_TENANT, SITE_ID, USER_ID, CK_TYPE

def addcredential(USER_TOKEN, USER_TENANT, CREDDATA):
    return USER_TOKEN, USER_TENANT, CREDDATA