from __future__ import absolute_import
from subprocess import Popen, PIPE
from powerline.theme import requires_segment_info

import os
import sys
import subprocess
import commands
from xml.dom import minidom

@requires_segment_info
def version(pl, segment_info):
    try:
        check = False
        path = ""

        if os.path.isfile("lib/Cake/VERSION.txt") == True:
            path = "lib/Cake/VERSION.txt"
            check = True

        if os.path.isfile("app/vendor/cakephp/cakephp/VERSION.txt") == True:
            path = "app/vendor/cakephp/cakephp/VERSION.txt"
            check = True

        if check == False:
            return None

        status, cake_version = commands.getstatusoutput("awk '/./{line=$0} END{print line}' " + path)

        if cake_version != '':
            return [{
                'contents': str(cake_version),
                'highlight_groups': ['version']
            }]
        else:
            return None

    except OSError as e:
        if e.errno == 2:
            pass
        else:
            raise
