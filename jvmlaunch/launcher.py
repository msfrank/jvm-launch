# Copyright 2015 Michael Frank <msfrank@syntaxjockey.com>
#
# This file is part of jvmlaunch.  jvmlaunch is BSD-licensed software;
# for copyright information see the LICENSE file.

import os, logging
from pesky.settings import ConfigureError
from jvmlaunch.jvm import JVM
from jvmlaunch.target import TargetJar, TargetClass

class Launcher(object):
    """
    The Launcher is responsible for configuring the separate aspects of the
    JVM, determining which target to launch, then running the JVM.
    """
    def __init__(self):
        self.target = None
        self.jvm = None
        self.native_agents = None
        self.java_agents = None
        self.show_version = True

    def configure(self, ns):
        """
        Configure the JVM application launcher.
        """
        # jvmlaunch_settings contains the command line arguments
        jvmlaunch_settings = ns.get_section('jvmlaunch')

        # configure logging early
        if jvmlaunch_settings.get_bool('debug', False) == True:
            logging.getLogger().setLevel(logging.DEBUG)

        # configure the target
        (target_section,) = ns.get_args(str, names=['TARGET'], minimum=1, maximum=1)
        try:
            target_settings = ns.get_section(target_section)
        except:
            raise ConfigureError("unknown target '%s'" % target_section)
        if target_section.startswith('targetclass:'):
            self.target = TargetClass(target_section.split(':', 1)[1])
        elif target_section.startswith('targetjar:'):
            self.target = TargetJar(target_section.split(':', 1)[1])
        self.target.configure(target_settings)

        # configure the JVM
        jvm_section = jvmlaunch_settings.get_str('jvm')
        try:
            jvm_settings = ns.get_section("jvm:" + jvm_section)
        except:
            raise ConfigureError("unknown jvm 'jvm:%s'" % jvm_section)
        self.jvm = JVM(jvm_section)
        self.jvm.configure(jvm_settings)

    def run(self):
        """
        Run the specified target using the configured JVM.
        """
        return self.jvm.run(self.target) 
