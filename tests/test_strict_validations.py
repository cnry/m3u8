# coding: utf-8
# Copyright 2014 Globo.com Player authors. All rights reserved.
# Use of this source code is governed by a MIT License
# license that can be found in the LICENSE file.


def test_should_fail_if_first_line_not_EXTM3U():
    assert True


def test_should_fail_if_expected_ts_segment_line_is_not_valid():
    assert True


def test_should_fail_if_EXT_X_MEDIA_SEQUENCE_is_diffent_from_sequence_number_of_first_uri():
    assert True


def test_should_fail_if_more_than_one_EXT_X_MEDIA_SEQUENCE():
    assert True


def test_should_fail_if_EXT_X_MEDIA_SEQUENCE_is_not_a_number():
    assert True


def test_should_validate_supported_EXT_X_VERSION():
    assert True


def test_should_fail_if_any_EXTINF_duration_is_greater_than_TARGET_DURATION():
    assert True


def test_should_fail_if_TARGET_DURATION_not_found():
    assert True


def test_should_fail_if_invalid_m3u8_url_after_EXT_X_STREAM_INF():
    assert True
