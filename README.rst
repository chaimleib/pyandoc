Pyandoc: a simple Pandoc wrapper for Python


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

Formats available:
	- context
	- docbook
	- epub
	- html
	- html_lhs
	- html5
	- html5_lhs
	- json
	- latex
	- latex_lhs
	- man
	- markdow
	- markdown_lhs
	- markdown_github
	- mediawiki
	- native
	- odt
	- opendocument
	- pdf
	- plain
	- rst
	- rst_lhs
	- rtf
	- s5
	- slidy
	- texinfo'

Enjoy.


Roadmap
+++++++

* Cleanup
* Proper Exceptions
* Unit testing
* CI
