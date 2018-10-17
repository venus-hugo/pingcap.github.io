# convert html links of a tags and src of img tags

from bs4 import BeautifulSoup

import os
import re
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

abs_hyper_link_pattern = re.compile(r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}')

with open(sys.argv[1], 'r') as f:
    soup = BeautifulSoup(f.read())

for link in soup.find_all('a'):
    href = link.get('href')
    if href:
        if (not abs_hyper_link_pattern.match(href)) and href.rfind('.md') > 0:
            href = href.replace('.md', '')
            href = os.path.normpath(re.sub(r'^[\.\/]*', href, '/'))
            href = os.path.normpath(os.path.join('/', sys.argv[2], href))
        print (href)
        link['href'] = href

# print (soup.prettify())
# write html
with open(sys.argv[1], 'w') as f:
    f.write(soup.prettify())
