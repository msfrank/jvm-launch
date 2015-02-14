# Copyright 2015 Michael Frank <msfrank@syntaxjockey.com>
#
# This file is part of jvmlaunch.  jvmlaunch is BSD-licensed software;
# for copyright information see the LICENSE file.

import os, logging

class JVM(object):
    """
    """
    def __init__(self, name):
        self.name = name
        self.java_home = None
        self.java_path = None
        self.version = None
        self.use_client_jvm = False

    def configure(self, settings):
        logging.debug("configuring jvm %s", self.name)

    def run(self, target):
        logging.debug("running target %s using jvm %s", target.name, self.name)
