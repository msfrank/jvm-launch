# Copyright 2015 Michael Frank <msfrank@syntaxjockey.com>
#
# This file is part of jvmlaunch.  jvmlaunch is BSD-licensed software;
# for copyright information see the LICENSE file.

import os, sys, traceback, logging
from pesky.settings import Settings, ConfigureError
from jvmlaunch.launcher import Launcher
from jvmlaunch.version import versionstring

logging.basicConfig(format="%(message)s")

def main():
    """
    Run the JVM application launcher.
    """
    settings = Settings(
        usage="[OPTIONS...] TARGET [TARGET-OPTIONS...]",
        version=versionstring(),
        description="JVM application launcher",
        appname="jvmlaunch",
        confbase=os.getcwd(),
        section="jvmlaunch")
    try:
        settings.add_option("j", "jvm",
            override="jvm", help="invoke the specified JVM when launching", metavar="JVM"
            )
        settings.add_switch("f", "foreground",
            override="foreground", help="Do not fork into the background"
            )
        settings.add_option("p", "pidfile",
            override="pid file", help="Store process identifier in FILE", metavar="FILE"
            )
        settings.add_switch("d", "debug",
            override="debug", help="Emit lots of debugging information"
            )
        # load configuration
        ns = settings.parse()
        # create the Agent and run it
        launcher = Launcher()
        launcher.configure(ns)
        return launcher.run()
    except ConfigureError, e:
        print >> sys.stderr, "%s: %s" % (settings.appname, e)
    except Exception, e:
        print >> sys.stderr, "\nUnhandled Exception:\n%s\n---\n%s" % (e,traceback.format_exc())
    sys.exit(1)
