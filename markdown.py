import mistune
import markdownify
import urllib
import os
from urllib.error import HTTPError
from urllib.parse import urlparse
import urllib.request
import random
from slugify import slugify

current_dir=os.getcwd()
path=os.path.join(current_dir, 'files')
if not os.path.exists(path):
    os.makedirs(path)
path=os.path.join(current_dir, 'files','img')
if not os.path.exists(path):
    os.makedirs(path)
    
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)

with open('data.txt', 'r', encoding="utf8") as file:
    md_str = file.read()
    
class MyCustomRenderer(mistune.Renderer):
    def image(self, src, title, alt_text):
        print("downloading...", src)
        file=None
        try:
            file=slugify(os.path.basename(urlparse(src).path))
            urllib.request.urlretrieve(src, os.path.join(current_dir, 'files', 'img', str(file)))
        except HTTPError:
            pass
        except OSError:
            file=random.randint(1, 9999999999)
            urllib.request.urlretrieve(src, os.path.join(current_dir, 'files', 'img', str(file)))
        return "<img src='%s' alt='%s'>" % ('img/' + str(file), alt_text)
# extension of file: os.path.splitext(os.path.basename(urlparse(src).path))[1]

renderer = MyCustomRenderer()
markdown = mistune.Markdown(renderer=renderer)
html_str = markdown(md_str)
h = markdownify.markdownify(html_str, heading_style="ATX")

with open(os.path.join(current_dir, 'files', 'README.md'), 'w', encoding="utf8") as file:
    file.write(h)