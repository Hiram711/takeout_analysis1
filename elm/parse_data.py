import json

with open('data.json', 'r', encoding='utf-8') as f:
    for line in f:
        item_list = json.loads(line).get('items')
        for item in item_list:
            shop = item.get('restaurant')
            shop_id = shop.get('id')
            name = shop.get('name')
            rating = shop.get('rating')
            recentOrderNum = shop.get('recentOrderNum')
            distance = shop.get('distance')
            orderLeadTime = shop.get('orderLeadTime')
            output = 'ID:%s,店名:%s,评分:%s,距离:%s,当月售卖数:%s,配送时间:%s'
            print(output % (shop_id, name, rating, distance, recentOrderNum, orderLeadTime))
