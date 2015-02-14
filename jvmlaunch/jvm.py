# Copyright 2015 Michael Frank <msfrank@syntaxjockey.com>
#
# This file is part of jvmlaunch.  jvmlaunch is BSD-licensed software;
# for copyright information see the LICENSE file.

import os, subprocess, logging
from pesky.settings import ConfigureError

class JVM(object):
    """
    """
    def __init__(self, name):
        self.name = name
        self.java_home = None
        self.java_path = None
        self.version = None
        self.use_client_vm = False

    def configure(self, settings):
        logging.debug("configuring jvm %s", self.name)
        # determine where java home is
        self.java_home = settings.get_path("java home", None)
        if self.java_home is None and 'JAVA_HOME' in os.environ:
            self.java_home = os.environ['JAVA_HOME']
        if self.java_home is None:
            raise ConfigureError("no java home directory specified" % self.java_home)
        if not os.path.isdir(self.java_home):
            raise ConfigureError("java home directory %s doesn't exist" % self.java_home)

        # find the path to java binary
        self.java_path = settings.get_path("java path", None)
        if self.java_path is None:
            self.java_path = os.path.join(self.java_home, "bin/java")
        if not os.path.isfile(self.java_path):
            raise ConfigureError("java program %s doesn't exist" % self.java_path)
        if not os.access(self.java_path, os.X_OK):
            raise ConfigureError("java program %s isn't executable" % self.java_path)

        self.use_client_jvm = settings.get_bool("use client vm", False)

    def run(self, target, app_args):
        logging.debug("running target %s using jvm %s", target.name, self.name)
        # build JVM command arguments
        cmd_args = [self.java_path]
        if self.use_client_vm is True:
            cmd_args += ['-client']
        else:
            cmd_args += ['-server']
        # build target command arguments
        cmd_args += target.get_args()
        # build application arguments
        cmd_args += app_args
        # construct the environment
        env = os.environ.copy()
        env['JAVA_HOME'] = self.java_home
        # set our initial file descriptors
        fd_in = None
        fd_out = None
        fd_err = None
        logging.debug("invoking command %s", " ".join(cmd_args))
        #exit_status = subprocess.call(cmd_args, env=env, shell=False, stdin=fd_in, stdout=fd_out, stderr=fd_err)
        #return exit_status
        return 0
