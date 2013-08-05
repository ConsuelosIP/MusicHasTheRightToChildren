#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#
# https://github.com/michielkauwatjoe/MusicHasTheRightToChildren

from mutagen.mp3 import MP3

class EmPeeThree:
    key_musicbrainz = 'TXXX:MusicBrainz'
    key_musicbrainz_album_id = key_musicbrainz + ' ' + 'Album Id'
    key_date = 'TDRC'

    def __init__(self, path):
        self.audio = MP3(path)
        self.metadata = {'format': 'mp3'}
        self.addMetadata()

    def addMetadata(self):
        self.metadata['date'] = str(self.audio[self.key_date])
        if self.key_musicbrainz_album_id in self.audio:
            self.metadata['musicbrainz_id'] = str(self.audio[self.key_musicbrainz_album_id])