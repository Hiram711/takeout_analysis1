import json

font_dict = {'f8cd': '3', 'ed35': '4', 'e2d1': '9', 'edb1': '2', 'ed25': '6', 'e716': '1', 'e239': '7', 'e634': '0',
             'e423': '8', 'e01c': '5', '78': '.'}


def decrypt_fonts(encrypt_string):
    global font_dict
    decrypt_string_list = [font_dict.get(j, j) for i in encrypt_string.split('&#x') for j in i.split(';')]
    return ''.join(decrypt_string_list)


with open('data.json', 'r', encoding='utf-8') as f:
    for line in f:
        shop_list = json.loads(line).get('data').get('shopList')
        for shop in shop_list:
            output = 'ID:%s,店名:%s,评分:%s,距离:%s,当月售卖数:%s,配送时间:%s'
            print(output % (shop.get('mtWmPoiId'), shop.get('shopName'), shop.get('wmPoiScore'),
                            decrypt_fonts(shop.get('distance')), decrypt_fonts(shop.get('monthSalesTip')),
                            decrypt_fonts(shop.get('deliveryTimeTip'))
                            )
                  )
