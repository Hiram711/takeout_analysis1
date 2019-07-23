from mitmproxy import ctx

from mitmproxy.http import HTTPFlow


def response(flow):
    url = 'https://restapi.ele.me/swarm/shops/recommend'
    info = ctx.log.info
    if flow.request.url.startswith(url):
        if flow.request.query.get('orderBy') == '5':
            text = flow.response.text
            with open('data.json', 'a', encoding='utf-8') as f:
                f.write(text)
                f.write('\n')
                info('数据获取获取成功')
