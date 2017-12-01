import requests
import Base_class
import datetime
import matplotlib.pyplot as plt

class GetVkUserInfo(Base_class.BaseClient):
    BASE_URL = 'https://api.vk.com/method/'
    method = 'users.get'
    user_id_or_username = str

    def get_params(self, user_id_or_username):
        return {'user_ids': user_id_or_username}

    def _get_data(self, method, http_method):
        r = requests.get(self.generate_url(self.method), params=self.get_params(self.user_id_or_username))
        # print(r.url)
        return self.response_handler(r)

    # Обработка ответа от VK API

    def response_handler(self, response):
        print(response.json()['response'][0]['first_name'])
        print(response.json()['response'][0]['last_name'])
        return response.json()['response'][0]['uid']

class GetVkFriendsInfo(Base_class.BaseClient):
    BASE_URL = 'https://api.vk.com/method/'
    method = 'friends.get'
    user_id = str

    def get_params(self, user_id):
        return {'user_id': user_id, 'fields': 'bdate', }

    def _get_data(self, method, http_method):
        r = requests.get(self.generate_url(self.method), params=self.get_params(self.user_id))
        return self.response_handler(r)

    # Обработка ответа от VK API

    def response_handler(self, response):
        mas_ages = []
        count_of_friends = len(response.json()['response'])
        print(count_of_friends, ' friends')
        for i in range(count_of_friends):
            try:
                bd = response.json()['response'][i]['bdate']
                if len(bd) >= 8:
                    ageindays = datetime.datetime.today()-datetime.datetime.strptime(bd, '%d.%m.%Y')
                    mas_ages.append(int(ageindays.days/365))
            except:
                pass
        # print(mas_ages)
        setofages = list(set(mas_ages))
        setofages.sort()
        for el in setofages:
            count = 0
            for i in mas_ages:
                if i == el:
                    count += 1
            print(el, ' ', '|'*count)
        n, bins, patches = plt.hist(mas_ages, 50, facecolor='g')
        plt.xlabel('Возраст')
        plt.ylabel('Количество')
        plt.title('Гистограмма распределения')
        plt.grid(True)
        plt.show()
        return response.json()
