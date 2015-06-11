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

    def test(self, cake_core_include_path):
        try:
            if os.path.isfile(cake_core_include_path + "/Cake/VERSION.txt") == False:
                return None

            status, cake_version = commands.getstatusoutput("awk '/./{line=$0} END{print line}' " + cake_core_include_path + "/Cake/VERSION.txt")

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

    def __call__(self, pl, segment_info, cake_core_include_path='lib'):

        return self.version(cake_core_include_path)

cakephp = with_docstring(CakePHPSegment(),
'''Return the status of a Git working copy.

It will show the branch-name, or the commit hash if in detached head state.

It will also show the number of commits behind, commits ahead, staged files,
unmerged files (conflicts), changed files, untracked files and stashed files
if that number is greater than zero.

:param bool use_dash_c:
    Call git with ``-C``, which is more performant and accurate, but requires git 1.8.5 or higher.
    Otherwise it will traverse the current working directory up towards the root until it finds a ``.git`` directory, then use ``--git-dir`` and ``--work-tree``.
    True by default.

Divider highlight group used: ``gitstatus:divider``.

Highlight groups used: ``gitstatus_branch_detached``, ``gitstatus_branch_dirty``, ``gitstatus_branch_clean``, ``gitstatus_branch``, ``gitstatus_behind``, ``gitstatus_ahead``, ``gitstatus_staged``, ``gitstatus_unmerged``, ``gitstatus_changed``, ``gitstatus_untracked``, ``gitstatus_stashed``, ``gitstatus``.
''')
