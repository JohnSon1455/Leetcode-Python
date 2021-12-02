import time
import json
import random
import requests
from pprint import pprint


class PchomeSpider():
    """PChome線上購物 爬蟲"""
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
        }

    def request_get(self, url, params=None, to_json=True):
        """送出 GET 請求

        :param url: 請求網址
        :param params: 傳遞參數資料
        :param to_json: 是否要轉為 JSON 格式
        :return data: requests 回應資料
        """
        r = requests.get(url, params)
        print(r.url)
        if r.status_code != requests.codes.ok:
            print(f'網頁載入發生問題：{url}')
        try:
            if to_json:
                data = r.json()
            else:
                data = r.text
        except Exception as e:
            print(e)
            return None
        return data

    def get_product_info(self, product_id, fields=None):
        """取得商品基本資訊

        :param product_id: 商品 ID
        :param fields: 指定欄位
        :return data: 商品基本資訊
        """
        # fields=Seq,Id,Name,Nick,Store,PreOrdDate,SpeOrdDate,Price,Discount,Pic,Weight,ISBN,Qty,Bonus,isBig,isSpec,isCombine,isDiy,isRecyclable,isCarrier,isMedical,isBigCart,isSnapUp,isDescAndIntroSync,isFoodContents,isHuge,isEnergySubsidy,isPrimeOnly,isPreOrder24h,isWarranty,isLegalStore,isFresh,isBidding,isSet,Volume,isArrival24h,isETicket,ShipType,isO2O
        url = f'https://ecapi.pchome.com.tw/ecshop/prodapi/v2/prod/{product_id}'
        if fields is not None:
            url += f'&fields={fields}'
        url += '&_callback=jsonp_prod'
        data = self.request_get(url, to_json=False)
        # 去除前後 JS 語法字串
        data = json.loads(data[15:-48])
        return data

    def get_product_description(self, product_id, fields=None):
        """取得商品描述(標語、規格、備註)

        :param product_id: 商品 ID
        :param fields: 指定欄位
        :return data: 商品描述資料
        """
        # &fields=Id,Stmt,Equip,Remark,Liability,Kword,Slogan,Author,Brand,Meta,Transman,Pubunit,Pubdate,Approve
        url = f'https://ecapi-pchome.cdn.hinet.net/cdn/ecshop/prodapi/v2/prod/{product_id}/desc'
        if fields is not None:
            url += f'&fields={fields}'
        url += '&_callback=jsonp_prod'
        data = self.request_get(url, to_json=False)
        # 去除前後 JS 語法字串
        data = json.loads(data[15:-48])
        return data

    def get_product_introduction(self, product_id, fields=None):
        """取得商品詳細介紹(包含圖片、影片)

        :param product_id: 商品 ID
        :param fields: 指定欄位
        :return introduction: 商品詳細介紹字串
        """
        # &fields=Id,Pic,Pstn,Intro,Sort
        url = f'https://ecapi-pchome.cdn.hinet.net/cdn/ecshop/prodapi/v2/prod/{product_id}/intro'
        if fields is not None:
            url += f'&fields={fields}'
        url += '&_callback=jsonp_intro'
        data = self.request_get(url, to_json=False)
        # 去除前後 JS 語法字串
        data = json.loads(data[16:-48])

        introduction = ''
        # 依照 Sort 欄位數字由小到大排順序
        data = sorted(data[product_id], key=lambda k: k['Sort']) 
        for intro in data:
            if intro['Pic']:
                introduction = introduction + '\n' + 'https://e.ecimg.tw' + intro['Pic']
            else:
                introduction = introduction + '\n' + intro['Intro']
        return introduction

    def get_add_buy_product(self, product_id, fields=None):
        """取得加購商品

        :param product_id: 商品 ID
        :param fields: 指定欄位
        :return data: 加購商品
        """
        # &fields=Seq,Id,Name,Spec,Group,Price,Pic,Qty,isWarranty
        url = f'https://ecapi-pchome.cdn.hinet.net/cdn/ecshop/prodapi/v2/prod/{product_id}/add'
        if fields is not None:
            url += f'&fields={fields}'
        url += '&_callback=jsonp_add'
        data = self.request_get(url, to_json=False)
        # 去除前後 JS 語法字串
        data = json.loads(data[14:-48])
        return data


if __name__ == '__main__':
    pchome_spider = PchomeSpider()

    # product_info = pchome_spider.get_product_info('DHAFI0-A900BAPXK')
    # pprint(product_info)

    # product_description = pchome_spider.get_product_description('DHAFI0-A900BAPXK', 'Id,Stmt,Equip,Remark')
    # print(product_description)

    # product_intro = pchome_spider.get_product_introduction('DHAFI0-A900BAPXK')
    # product_intro = pchome_spider.get_product_introduction('DEBB55-A900AUAHM')
    # print(product_intro)

    # add_buy_product = pchome_spider.get_add_buy_product('DHAFI0-A900BAPXK', 'Seq,Id,Name,Spec,Group,Price,Pic,Qty,isWarranty')
    # print(add_buy_product)