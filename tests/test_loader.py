# coding: utf-8
# Copyright 2014 Globo.com Player authors. All rights reserved.
# Use of this source code is governed by a MIT License
# license that can be found in the LICENSE file.

import os
try:
    import urlparse as url_parser
except ImportError:
    import urllib.parse as url_parser
import m3u8
import playlists


def test_loads_should_create_object_from_string():
    obj = m3u8.loads(playlists.SIMPLE_PLAYLIST)
    obj.should.be.a(m3u8.M3U8)
    (5220.0).should.equal(obj.target_duration)
    ('http://media.example.com/entire.ts').should.equal(obj.segments[0].uri)


def test_load_should_create_object_from_file():
    obj = m3u8.load(playlists.SIMPLE_PLAYLIST_FILENAME)
    obj.should.be.a(m3u8.M3U8)
    (5220.0).should.equal(obj.target_duration)
    ('http://media.example.com/entire.ts').should.equal(obj.segments[0].uri)


def test_load_should_create_object_from_uri():
    obj = m3u8.load(playlists.SIMPLE_PLAYLIST_URI)
    obj.should.be.a(m3u8.M3U8)
    (5220.0).should.equal(obj.target_duration)
    ('http://media.example.com/entire.ts').should.equal(obj.segments[0].uri)


def test_load_should_remember_redirect():
    obj = m3u8.load(playlists.REDIRECT_PLAYLIST_URI)
    urlparsed = url_parser.urlparse(playlists.SIMPLE_PLAYLIST_URI)
    (urlparsed.scheme + '://' + urlparsed.netloc + "/").should.equal(obj.base_uri)


def test_load_should_create_object_from_file_with_relative_segments():
    base_uri = os.path.dirname(playlists.RELATIVE_PLAYLIST_FILENAME)
    obj = m3u8.load(playlists.RELATIVE_PLAYLIST_FILENAME)
    expected_key_abspath = '%s/key.bin' % os.path.dirname(base_uri)
    expected_key_path = '../key.bin'
    expected_ts1_abspath = '%s/entire1.ts' % base_uri
    expected_ts1_path = '/entire1.ts'
    expected_ts2_abspath = '%s/entire2.ts' % os.path.dirname(base_uri)
    expected_ts2_path = '../entire2.ts'
    expected_ts3_abspath = '%s/entire3.ts' % os.path.dirname(os.path.dirname(base_uri))
    expected_ts3_path = '../../entire3.ts'
    expected_ts4_abspath = '%s/entire4.ts' % base_uri
    expected_ts4_path = 'entire4.ts'

    obj.should.be.a(m3u8.M3U8)
    (expected_key_path).should.equal(obj.key.uri)
    (expected_key_abspath).should.equal(obj.key.absolute_uri)
    (expected_ts1_path).should.equal(obj.segments[0].uri)
    (expected_ts1_abspath).should.equal(obj.segments[0].absolute_uri)
    (expected_ts2_path).should.equal(obj.segments[1].uri)
    (expected_ts2_abspath).should.equal(obj.segments[1].absolute_uri)
    (expected_ts3_path).should.equal(obj.segments[2].uri)
    (expected_ts3_abspath).should.equal(obj.segments[2].absolute_uri)
    (expected_ts4_path).should.equal(obj.segments[3].uri)
    (expected_ts4_abspath).should.equal(obj.segments[3].absolute_uri)


def test_load_should_create_object_from_uri_with_relative_segments():
    obj = m3u8.load(playlists.RELATIVE_PLAYLIST_URI)
    urlparsed = url_parser.urlparse(playlists.RELATIVE_PLAYLIST_URI)
    base_uri = os.path.normpath(urlparsed.path + '/..')
    prefix = urlparsed.scheme + '://' + urlparsed.netloc
    expected_key_abspath = '%s%s/key.bin' % (prefix, os.path.normpath(base_uri + '/..'))
    expected_key_path = '../key.bin'
    expected_ts1_abspath = '%s/entire1.ts' % (prefix)
    expected_ts1_path = '/entire1.ts'
    expected_ts2_abspath = '%s%sentire2.ts' % (prefix, os.path.normpath(base_uri + '/..') + '/')
    expected_ts2_path = '../entire2.ts'
    expected_ts3_abspath = '%s%sentire3.ts' % (prefix, os.path.normpath(base_uri + '/../..'))
    expected_ts3_path = '../../entire3.ts'
    expected_ts4_abspath = '%s%sentire4.ts' % (prefix, base_uri + '/')
    expected_ts4_path = 'entire4.ts'

    obj.should.be.a(m3u8.M3U8)
    (expected_key_path).should.equal(obj.key.uri)
    (expected_key_abspath).should.equal(obj.key.absolute_uri)
    (expected_ts1_path).should.equal(obj.segments[0].uri)
    (expected_ts1_abspath).should.equal(obj.segments[0].absolute_uri)
    (expected_ts2_path).should.equal(obj.segments[1].uri)
    (expected_ts2_abspath).should.equal(obj.segments[1].absolute_uri)
    (expected_ts3_path).should.equal(obj.segments[2].uri)
    (expected_ts3_abspath).should.equal(obj.segments[2].absolute_uri)
    (expected_ts4_path).should.equal(obj.segments[3].uri)
    (expected_ts4_abspath).should.equal(obj.segments[3].absolute_uri)


def test_there_should_not_be_absolute_uris_with_loads():
    with open(playlists.RELATIVE_PLAYLIST_FILENAME) as f:
        content = f.read()
    obj = m3u8.loads(content)
    obj.key.get_absolute_uri.when.called.should.have.raised(
        ValueError,
        'There can not be `absolute_uri` with no `base_uri` set'
    )


def test_absolute_uri_should_handle_empty_base_uri_path():
    key = m3u8.model.Key(method='AES', uri='/key.bin', base_uri='http://example.com')
    ('http://example.com/key.bin').should.equal(key.absolute_uri)
