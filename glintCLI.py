from glintAPI import glint_api
import argparse
import logging
import os
import sys
#import warnings


def env(*vars, **kwargs):
    """ Try to find the first environnental variable in vars,
        if successful return it.
        Otherwise return the default defined in kwargs.

    """
    for v in vars:
        value = os.environ.get(v)
        if value:
            return value
    return kwargs.get('default', '')


class glintCommands(object):

    def __init__(self, parser_class=argparse.ArgumentParser):
        self.parser_class = parser_class
        self.api = glint_api('api.log', 'logging.DEBUG', 'api.yaml')

    # create parser for arguments to be inherited by the subcommand subparsers
    def get_base_parser(self):
        self.parent = self.parser_class(
                prog='glint',
                epilog='See "glint help COMMAND" '
                        'for help on a specific command.',
                add_help=False
        )

        # Global arguments

        # used by save
        self.parent.add_argument('--json-message',
                             default=env('JSON_MESSAGE'),
                             help='Message used for authentication with the '
                                  'OpenStack Identity service. '
                                  'Defaults to env[JSON_MESSAGE].')

        # used by delete-site, delete-credential, get-credential, and has-credential
        self.parent.add_argument('--site-id',
                             default=env('SITE_ID'),
                             help='Site ID used for authentication with the '
                                  'OpenStack Identity service. '
                                  'Defaults to env[SITE_ID].')

        # used by create-site
        self.parent.add_argument('--site-data',
                             default=env('SITEDATA'),
                             help='Site data used for authentication with the '
                                  'OpenStack Identity service. '
                                  'Defaults to env[SITEDATA].')

        # used by has-credential
        self.parent.add_argument('--ck-type',
                             default=env('CK_TYPE'),
                             help='CK type used for authentication with the '
                                  'OpenStack Identity service. '
                                  'Defaults to env[CK_TYPE].')

        # used-by add-credential
        self.parent.add_argument('--cred-data',
                             default=env('CREDDATA'),
                             help='Credential data used for authentication with the '
                                  'OpenStack Identity service. '
                                  'Defaults to env[CREDDATA].')
         
    
    # default funtions for subcommand parsers to make calls to the glint API

    def getImages(self, args):
        return self.api.getImages()

    def save(self, args):
        return self.api.save(args.json_message)

    def credentials(self, args):
        return self.api.credentials()

    def listSites(self, args):
        return self.api.listSites()

    def deleteSite(self, args):
        return self.api.deleteSite(args.site_id)

    def createSite(self, args):
        return self.api.createSite(args.site_data)

    def deleteCredential(self, args):
        return self.api.deleteCredential(args.site_id)

    def getCredential(self, args):
        return self.api.getCredential(args.site_id)

    def hasCredential(self, args):
        return self.api.hasCredential( args.site_id, args.ck_type)

    def addCredential(self, args):
        return self.api.addCredential(args.cred_data)




    def get_sub_command_parser(self):
        # create a new parser
        parser = self.parser_class(
                prog='glint',
                epilog='See "glint help COMMAND" '
                        'for help on a specific command.',
                add_help=False
        )
        
        # create a subparser instance for the new parser
        subparser = parser.add_subparsers(prog='glint')
        

        # subparsers to handle subcommands and inherit argument parsing

        # get-images
        parser_getImages = subparser.add_parser('get-images',
                                                parents=[self.parent], 
                                                help='get images help')
        parser_getImages.set_defaults(func=self.getImages)

        
        # save
        parser_save = subparser.add_parser('save',
                                           parents=[self.parent],
                                           help='save help')
        parser_save.set_defaults(func=self.save)


        # credentials
        parser_credentials = subparser.add_parser('credentials',
                                                 parents=[self.parent],
                                                 help='credentials help')
        parser_credentials.set_defaults(func=self.credentials)



        # list-sites 
        parser_listSites = subparser.add_parser('list-sites',
                                                 parents=[self.parent],
                                                 help='list sites help')
        parser_listSites.set_defaults(func=self.listSites)


        # delete-site
        parser_deleteSite = subparser.add_parser('delete-site',
                                                 parents=[self.parent],
                                                 help='delete site help')
        parser_deleteSite.set_defaults(func=self.deleteSite)


        # create-site
        parser_createSite = subparser.add_parser('create-site',
                                                 parents=[self.parent],
                                                 help='create site help')
        parser_createSite.set_defaults(func=self.createSite)


        # delete-credential 
        parser_deleteCredential = subparser.add_parser('delete-credential',
                                                 parents=[self.parent],
                                                 help='delete credential help')
        parser_deleteCredential.set_defaults(func=self.deleteCredential)


        # get-credential 
        parser_getCredential = subparser.add_parser('get-credential',
                                                 parents=[self.parent],
                                                 help='get credential help')
        parser_getCredential.set_defaults(func=self.getCredential)


        # has-credential
        parser_hasCredential = subparser.add_parser('has-credential',
                                                 parents=[self.parent],
                                                 help='has credential help')
        parser_hasCredential.set_defaults(func=self.hasCredential)


        # add-credential
        parser_addCredential = subparser.add_parser('add-credential',
                                                 parents=[self.parent],
                                                 help='add credential help')
        parser_addCredential.set_defaults(func=self.addCredential)

        return parser
    

    def main(self, argv):
        # initialize the parser to be inherited
        self.get_base_parser()

        # setup subcommand parser and parse areguments
        subcommand_parser = self.get_sub_command_parser()
        command_args = subcommand_parser.parse_args(argv)

        # call the handler function specified by the subcommand
        print command_args.func(command_args)


def main():
    glintCommands().main(sys.argv[1:])

if __name__=="__main__":
    sys.exit(main())
