from mitmproxy import ctx
import json
from bs4 import BeautifulSoup

from mitmproxy.http import HTTPFlow


def response(flow):
    url1 = 'https://h5.waimai.meituan.com/waimai/mindex/home'
    url2 = 'https://i.waimai.meituan.com/openh5/homepage/poilist'
    info = ctx.log.info
    if flow.request.url.startswith(url1):
        soup = BeautifulSoup(flow.response.text, 'html5lib')
        with open('index.html', 'w') as f:
            f.write(soup.prettify())

    if flow.request.url.startswith(url2):
        if flow.request.urlencoded_form.get('sortId') == '5':
            text = flow.response.text
            data = json.loads(text)
            info(str(data))
