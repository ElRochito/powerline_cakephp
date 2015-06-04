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
        if os.path.isfile("lib/Cake/VERSION.txt") == False:
            return None

        status, alloy_version = commands.getstatusoutput("awk '/./{line=$0} END{print line}' lib/Cake/VERSION.txt")

        if alloy_version != '':
            return [{
                'contents': str(alloy_version),
                'highlight_groups': ['version']
            }]
        else:
            return None

    except OSError as e:
        if e.errno == 2:
            pass
        else:
            raise
