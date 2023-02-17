import vk_api
# импорт библиотеки вк

vk_session = vk_api.VkApi(
    token='токен')
vk = vk_session.get_api()

class Wall:
    def __init__(self,owner,post):
        self.owner = 'айди группы'
        self.post = post


    def cls_cms(self):
        vk.wall.closeComments(
            owner_id = self.owner,
            post_id = self.post
        )
