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
            return {u'rows': [{u'container_format': u'bare', u'image': u'cirros-0.3.3-x86_64', u'disk_format': u'qcow2', u'sites': [{u'is_public': u'True', u'tenent': u'glinttenant', u'is_owner': u'False', u'name': u'TestSite'}, {u'is_public': u'True', u'tenent': u'glinttenant', u'is_owner': u'False', u'name': u'DevSite'}]}, {u'container_format': u'bare', u'image': u'Ubuntu-14.04-x86_64', u'disk_format': u'qcow2', u'sites': [{u'is_public': u'True', u'tenent': u'glinttenant', u'is_owner': u'False', u'name': u'ProdSite'}, {u'is_public': u'True', u'tenent': u'glinttenant', u'is_owner': u'False', u'name': u'DevSite'}]} ], u'sites': [{u'tenent': u'glinttenant', u'name': u'TestSite'}, {u'tenent': u'glinttenant', u'name': u'DevSite'}, {u'tenent': u'glinttenant', u'name': u'ProdSite'}]}



    def save(self, JSON_MESSAGE):
        return JSON_MESSAGE

    def credentials(self):
        return 'Credentials'

    def listSites(self):
        return [u'{"name":"Mouse","url":"http://mouse01.heprc.uvic.ca:5000/v2.0","authport":"5000","version":"v2.0","type":"Openstack","pk":"1"}']

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
