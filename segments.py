from __future__ import absolute_import
from subprocess import Popen, PIPE
from powerline.theme import requires_segment_info

from powerline.segments import Segment, with_docstring
from subprocess import PIPE, Popen
import os, re, string

import os
import sys
import subprocess
import commands
from xml.dom import minidom

@requires_segment_info
class CakePHPSegment(Segment):

    def version(self, cake_core_include_path):
        try:
            if os.path.isfile(cake_core_include_path + "/Cake/VERSION.txt") == False:
                return None

            status, cake_version = commands.getstatusoutput("awk '/./{line=$0} END{print line}' " + cake_core_include_path + "/Cake/VERSION.txt")

            if cake_version != '':
                return [{
                    'contents': str(cake_version),
                    'highlight_groups': ['cakephp_version']
                }]
            else:
                return None

        except OSError as e:
            if e.errno == 2:
                pass
            else:
                raise

    def __call__(self, pl, segment_info, cake_core_include_path='lib'):

        return self.version(cake_core_include_path)

cakephp = with_docstring(CakePHPSegment(),
'''Return the CakePHP version number.
''')
