'''
Created on Mar 26, 2015
ok
@author: ronaldjosephdesmarais
'''
#import logging,yaml,json,requests
#import keystoneclient.v2_0.client as ksclient

class glint_api(object):
    def __init__(self,log_name,log_lvl,glint_cfg):
        #setup logging for glint api
        print "init glint_api"
        
    def getImages(self):
        data_obj = {}
        return data_obj

    def imageDelete(self,image_name,img_src_site,image_src_tenent):
        data_obj = {}
        return data_obj
        
    def imageCopy(self,image_name,src_site,dest_sites):
        data_obj = {}
        return data_obj

    def listSites(self):
        data_obj = {}
        return data_obj

    def deleteSite(self, SITE_ID):
        data_obj = {}
        return data_obj

    def createSite(self,name,url,formatt):
        data_obj = {}
        return data_obj

    def deleteCredential(self, site_id):
        data_obj = {}
        return data_obj

    def getCredential(self,site_id):
        data_obj = {}
        return data_obj

    def hasCredential(self, site_id, ck_type):
        data_obj = {}
        return data_obj

    def addCredential(self, remote_tenant,remote_un,remote_pw,remote_site_id):
        data_obj = {}
        return data_obj
    
    
    
    
    
    
    