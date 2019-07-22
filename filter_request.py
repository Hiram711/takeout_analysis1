from mitmproxy import ctx
from bs4 import BeautifulSoup
import re
import requests
# from mitmproxy.http import HTTPFlow


def response(flow):
    url1 = 'https://h5.waimai.meituan.com/waimai/mindex/home'
    url2 = 'https://i.waimai.meituan.com/openh5/homepage/poilist'
    info = ctx.log.info
    if flow.request.url.startswith(url1):
        soup = BeautifulSoup(flow.response.text, 'html5lib')
        l = soup.find_all('style', {'type': 'text/css'})
        for i in l:
            if re.match(r'^@font-face{.+}$', i.text.strip()):
                current_font_url = 'https:' + re.findall(r',url.+\.woff', i.text.strip())[0][6:]
                ttf = requests.get(current_font_url, stream=True)
                with open("current_font.woff", "wb") as pdf:
                    for chunk in ttf.iter_content(chunk_size=1024):
                        if chunk:
                            pdf.write(chunk)  # http://fontstore.baidu.com/static/editor/index.html
                info('字体文件获取成功')
                break

    if flow.request.url.startswith(url2):
        if flow.request.urlencoded_form.get('sortId') == '5':
            text = flow.response.text
            with open('data.json', 'a', encoding='utf-8') as f:
                f.write(text)
                f.write('\n')
                info('数据获取获取成功')
