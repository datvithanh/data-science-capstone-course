# import requests
# from parsel import Selector
# from tqdm import tqdm
# url = 'https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-ha-noi/'

# with open('apartments.txt', 'w+') as f:
#     for i in range(1, 407):
#         u = url + 'p{}'.format(i)
#         response = requests.get(url)
#         sel = Selector(response.text)
#         pr = sel.xpath(
#             "//strong[contains(@class,'product-price')]/text()").extract()
#         ar = sel.xpath(
#             "//strong[contains(@class,'product-area')]/text()").extract()
#         di = sel.xpath(
#             "//strong[contains(@class, 'product-city-dist')]/text()").extract()
#         print('page: {}, price: {}, area: {}, dist: {}\n'.format(
#             i, len(pr), len(ar), len(di)))
#         pr = [x.replace('\n', '').replace('\r', '') for x in pr]
#         ar = [x.replace('\n', '').replace('\r', '') for x in ar]
#         di = [x.replace('\n', '').replace('\r', '') for x in di]
#         for j in range(len(pr)):
#             f.write('{}|{}|{}|{}\n'.format(pr[j], ar[j], di[j], i))
