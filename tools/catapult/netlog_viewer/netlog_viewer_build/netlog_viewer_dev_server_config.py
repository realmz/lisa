# Copyright (c) 2016 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import json
import os

import netlog_viewer_project

import webapp2
from webapp2 import Route


def _RelPathToUnixPath(p):
  return p.replace(os.sep, '/')


class TestListHandler(webapp2.RequestHandler):

  def get(self, *args, **kwargs):  # pylint: disable=unused-argument
    project = netlog_viewer_project.NetlogViewerProject()
    test_relpaths = ['/' + _RelPathToUnixPath(x)
                     for x in project.FindAllTestModuleRelPaths()]

    tests = {'test_relpaths': test_relpaths}
    tests_as_json = json.dumps(tests)
    self.response.content_type = 'application/json'
    return self.response.write(tests_as_json)


class NetlogViewerDevServerConfig(object):

  def __init__(self):
    self.project = netlog_viewer_project.NetlogViewerProject()

  def GetName(self):
    return 'netlog_viewer'

  def GetRunUnitTestsUrl(self):
    return '/netlog_viewer/tests.html'

  def AddOptionstToArgParseGroup(self, g):
    pass

  def GetRoutes(self, args):  # pylint: disable=unused-argument
    return [
        Route('/netlog_viewer/tests', TestListHandler),
    ]

  def GetSourcePaths(self, args):  # pylint: disable=unused-argument
    return list(self.project.source_paths)

  def GetTestDataPaths(self, args):  # pylint: disable=unused-argument
    return []
