Pyandoc: a simple Pandoc wrapper for Python

.. image:: https://travis-ci.org/chaimleib/pyandoc.svg?branch=master
    :target: https://travis-ci.org/chaimleib/pyandoc

Requirements
++++++++++++

* Pandoc


Usage
+++++

Get setup. ::

	import pandoc

	# pandoc.PANDOC_PATH = '/usr/bin/pandoc'


Let's start with a Markdown document: ::


	doc = pandoc.Document()
	doc.markdown = '''
	# I am an H1 Tag

	* bullet point
	* more points
	* point with [link](http://kennethreitz.com)!
	'''

Now let's convert that into a ReST document: ::

	>>> print doc.rst

	I am an H1 Tag
	==============


	-  bullet point
	-  more points
	-  point with `link <http://kennethreitz.com>`_!

Input formats available:
	- html
	- json
	- latex
	- latex+lhs
	- markdown
	- markdown+lhs
	- markdown_github
	- markdown_mmd
	- markdown_phpextra
	- mediawiki
	- native
	- rst
	- rst+lhs
	- textile

Output formats available
	- asciidoc
	- context
	- docbook
	- docx
	- epub
	- epub3
	- html
	- html+lhs
	- html5
	- html5+lhs
	- json
	- latex
	- latex+lhs
	- man
	- markdown
	- markdown+lhs
	- markdown_github
	- mediawiki
	- native
	- opendocument
	- pdf
	- plain
	- rst
	- rst+lhs
	- rtf
	- s5
	- slidy
	- texinfo
	- texinfo
	- textile

Enjoy.


Roadmap
+++++++

* Cleanup
* Proper Exceptions
* Unit testing
* CI
