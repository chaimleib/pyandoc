#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
import subprocess
from os.path import exists
from tempfile import NamedTemporaryFile
import os

# Import find executable engine
try:
    from shutil import which
except ImportError:
    from distutils.spawn import find_executable

    which = find_executable

# Path to the executable
PANDOC_PATH = which('pandoc')


class Document(object):
    """
        A formatted document.
    """

    INPUT_FORMATS = {
        'native', 'markdown', 'markdown+lhs', 'rst',
        'rst+lhs', 'html', 'latex', 'latex+lhs',
        'json', 'markdown_github', 'markdown_mmd', 'markdown_phpextra',
        'mediawiki', 'textile'
    }

    OUTPUT_FORMATS = {
        'native', 'html', 'html+lhs', 's5', 'html5', 'html5+lhs', 'slidy',
        'docbook', 'opendocument', 'asciidoc',
        'latex', 'latex+lhs', 'context', 'texinfo', 'json',
        'man', 'markdown', 'markdown+lhs', 'markdown_github',
        'plain', 'rst', 'rst+lhs', 'mediawiki', 'rtf', 'texinfo',
        'textile', 'docx'
    }

    OUTPUT_WRITER = {
        'odt', 'epub', 'epub3', 'pdf'
    }

    def __init__(self):
        self._content = None
        self._format = None
        self._register_formats()
        self.arguments = []

        if not exists(PANDOC_PATH):
            raise OSError("Path to pandoc executable does not exists")

    def bib(self, bibfile):
        """
            Set Bibliography
            :param bibfile:
            :return:
        """
        if not exists(bibfile):
            raise IOError("Bib file not found: %s" % bibfile)
        self.add_argument("bibliography=%s" % bibfile)

    def csl(self, cslfile):
        if not exists(cslfile):
            raise IOError("CSL file not found: %s" % cslfile)
        self.add_argument("csl=%s" % cslfile)

    def abbr(self, abbrfile):
        if not exists(abbrfile):
            raise IOError("Abbreviations file not found: " + abbrfile)
        self.add_argument("citation-abbreviations=%s" % abbrfile)

    def add_argument(self, arg):
        self.arguments.append("--%s" % arg)
        return self.arguments

    @classmethod
    def _register_formats(cls):
        """Adds format properties."""
        for fmt in cls.OUTPUT_FORMATS | cls.OUTPUT_WRITER:
            clean_fmt = fmt.replace('+', '_')
            setattr(cls, clean_fmt, property(
                (lambda x, fmt=fmt: cls._output(x, fmt)),  # fget
                (lambda x, y, fmt=fmt: cls._input(x, y, fmt))))  # fset

    def _input(self, value, format=None):
        # format = format.replace('_', '+')
        self._content = value
        self._format = format

    def _output(self, format_):

        subprocess_arguments = [PANDOC_PATH, '--from=%s' % self._format]
        subprocess_arguments.extend(self.arguments)

        if format_ in self.OUTPUT_WRITER:
            tmp = NamedTemporaryFile(mode="w", suffix="." + format_, delete=False)
            tmp.close()

            subprocess_arguments.extend(['-o', tmp.name])
        else:
            subprocess_arguments.extend(['-w', format_])

        p = subprocess.Popen(
            subprocess_arguments,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            universal_newlines=True
        )
        rtn = p.communicate(self._content)[0]
        if format_ in self.OUTPUT_WRITER:
            with open(subprocess_arguments[-1], "rb") as f:
                rtn = f.read()
            os.unlink(subprocess_arguments[-1])

        return rtn


