import json

with open('data_night.json', 'r', encoding='utf-8') as f:
    for line in f:
        shop_list = json.loads(line).get('data').get('shopList')
        for shop in shop_list:
            output = 'ID:%s,店名:%s,评分:%s'
            print(output % (shop.get('mtWmPoiId'), shop.get('shopName'), shop.get('wmPoiScore')))
