import pandoc

def test_conversion():
    with open('README.rst', 'r') as readme:
        rst = readme.read()
    doc = pandoc.Document()
    doc.rst = rst
    
    markdown = doc.markdown
    assert isinstance(markdown, str)
    assert len(markdown)
    assert rst != markdown
