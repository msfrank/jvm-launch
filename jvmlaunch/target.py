# Copyright 2015 Michael Frank <msfrank@syntaxjockey.com>
#
# This file is part of jvmlaunch.  jvmlaunch is BSD-licensed software;
# for copyright information see the LICENSE file.

import os, logging

class Target(object):
    """
    """
    def __init__(self, name):
        self.name = name
        self.class_path = None

    def configure(self, settings):
        pass

class TargetClass(Target):
    """
    """
    def __init__(self, name):
        Target.__init__(self, name)
        self.main_class = None

    def configure(self, settings):
        logging.debug("configuring targetclass %s", self.name)

class TargetJar(Target):
    """
    """
    def __init__(self, name):
        Target.__init__(self, name)
        self.jar_file = None

    def configure(self, settings):
        logging.debug("configuring targetjar %s", self.name)
