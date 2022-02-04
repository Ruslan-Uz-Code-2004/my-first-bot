import requests
from fake_useragent import UserAgent
import json

ua = UserAgent()


def collect_data(cat_type=2):

   # response = requests.get(
    # url='https://inventories.cs.money/5.0/load_bots_inventory/730?buyBonus=40&isStore=true&limit=60&maxPrice=200&minPrice=100&offset=60',
    # headers={'user-agent': f'{ua.random}'}
    # )
    # json.dump(response.json(), file, indent=4, ensure_ascii=False)

    offset = 0
    batch_size = 60
    result = []
    while True:
        for item in range(offset, offset+batch_size, 60):
            url = f'https://inventories.cs.money/5.0/load_bots_inventory/730?buyBonus=40&isStore=true&limit=60&maxPrice=200&minPrice=100&offset={item}&type={cat_type}&withStack=true'.encode(
                'utf-8')
            response = requests.get(
                url=url,
                headers={'user-agent': f'{ua.random}'}
            )
            offset += batch_size
            data = response.json()
            items = data.get('items')
            for i in items:
                if i.get('overprice') is not None and i.get('overprice') < -10:
                    item_full_name = i.get('fullName')
                    item_3d = i.get('3d')
                    item_price = i.get('price')
                    item_over_prays = i.get('overprice')
                    result.append(
                        {
                            'full_name': item_full_name,
                            '3d': item_3d,
                            'price': item_price,
                            'overprice': item_over_prays
                        }
                    )
        if len(items) < 60:
            break
    with open('../result_cs.json', 'w', encoding="utf-8") as file:
        json.dump(result, file, indent=4, ensure_ascii=False)


def main():
    collect_data()


if __name__ == '__main__':
    main()
