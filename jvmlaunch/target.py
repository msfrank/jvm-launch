# Copyright 2015 Michael Frank <msfrank@syntaxjockey.com>
#
# This file is part of jvmlaunch.  jvmlaunch is BSD-licensed software;
# for copyright information see the LICENSE file.

import os, logging
from pesky.settings import ConfigureError

class Target(object):
    """
    """
    def __init__(self, name):
        self.name = name
        self.class_path = None

    def configure(self, settings):
        self.class_path = settings.get_str("class path", None)

    def get_args(self):
        if self.class_path is None:
            return []
        return ['-cp', self.class_path]

class TargetClass(Target):
    """
    """
    def __init__(self, name):
        Target.__init__(self, name)
        self.main_class = None

    def configure(self, settings):
        Target.configure(self, settings)
        logging.debug("configuring targetclass %s", self.name)
        self.main_class = settings.get_str("main class", None)
        if self.main_class is None:
            raise ConfigureError("no main class specified")

    def get_args(self):
        return Target.get_args(self) + self.main_class

class TargetJar(Target):
    """
    """
    def __init__(self, name):
        Target.__init__(self, name)
        self.jar_file = None

    def configure(self, settings):
        Target.configure(self, settings)
        logging.debug("configuring targetjar %s", self.name)
        self.jar_file = settings.get_path("jar file", None)
        if self.jar_file is None:
            raise ConfigureError("no jar file specified")
        if not os.path.isfile(self.jar_file):
            raise ConfigureError("jar file %s doesn't exist" % self.jar_file)

    def get_args(self):
        return Target.get_args(self) + ['-jar', self.jar_file]
