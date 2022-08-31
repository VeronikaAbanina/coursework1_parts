import requests
from pprint import pprint

vk_id = ''
vk_token = ''


class VK:
    def get_photos(self, owner_id):
        '''Получаем фото из альбома вк'''
        URL = 'https://api.vk.com/method/photos.get'
        params = {
            'access_token': vk_token,
            'owner_id': vk_id,
            'album_id': '286078325',
            'extended': 1,
            'v': 5.131
        }
        res = requests.get(URL, params=params).json()
        return res
        pprint(res)



# URL = 'https://api.vk.com/method/photos.get'
# params = {
#     'access_token': vk_token,
#     'owner_id': vk_id,
#     'album_id': 286078325,
#     'extended': 1,
#     'v': 5.131
# }
# res = requests.get(URL, params=params).json()
# pprint(res)