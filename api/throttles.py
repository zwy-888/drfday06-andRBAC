from rest_framework.throttling import SimpleRateThrottle


class MyThrottles(SimpleRateThrottle):
    # 判断请求是否可以访问

    scope = 'sms'

    # 只对get方法进行限制
    def get_cache_key(self, request, view):
        username = request.data.get('username')
        id = request.data.get('id')
        print('1111', username)
        # 别的就不做频率限制
        # print()
        print(id)
        if id == 'None':
            return None
        return True
