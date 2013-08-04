# -*- coding: UTF-8 -*-

import boto
from boto.exception import SDBResponseError


class SimpleDB:
    u"""
    Connection to NoSQL.
    """
    CONNECTION = None
    DOMAIN = None

    def __init__(self, awsaccesskey, awssecretkey, domainname):
        u"""
        Opens the connection or initializes a new domain on SimpleDB if it doesn't exist.
        """
        self.CONNECTION = boto.connect_sdb(awsaccesskey, awssecretkey)

        try:
            self.DOMAIN = self.CONNECTION.get_domain(domainname)
            print 'Established connection to SimpleDB domain %s' % domainname
        except SDBResponseError, e:
            print u'SimpleDB domain doesn’t exist yet, creating domain with name %s' % domainname
            self.DOMAIN = self.CONNECTION.create_domain(domainname)

    def listItems(self):
        pass

    def numberOfItems(self):
        meta = self.getMetadata()
        return meta.item_count

    def dumpCollection(self):
        f = open("dump.xml", 'w')
        fd = self.DOMAIN.to_xml(f=f)

    def getMetadata(self):
        return self.DOMAIN.get_metadata()

    def addID(self, album, id):
        u"""
        """
        self.writeItem(album=album, musicbrainzid=id)

    def writeItem(self, *args, **kwargs):
        u"""
        Writes key-value pairs to database.
        """
        item_name = kwargs['album']
        musicbrainzid = kwargs['musicbrainzid']
        item_attrs = {'musicbrainzid': musicbrainzid}
        self.DOMAIN.put_attributes(item_name, item_attrs)

        #for key, value in kwargs.items():
        #    item[key] = value

        #print item
