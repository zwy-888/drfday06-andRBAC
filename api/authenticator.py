from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication, BasicAuthentication

from api.models import User


class MyAuthentication(BaseAuthentication):

    def authenticate(self, request):
        print('111')
        # 获取认证信息 , 没有就返回None  get不会报错
        auth = request.META.get("HTTP_AUTHORIZATION", None)
        print(auth)
        if auth is None:
            # 代表没有认证，为游客
            return None
        # 设置验证信息的校验  将前端的AUTHORIZATION 信息进行分割成列表
        auth_list = auth.split()
        if not (len(auth_list) == 2 and auth_list[0].lower() == 'auth'):  # 格式前面为 auth 后面为yan
            # if not (len(auth_list) == 2 and auth_list[0].lower() == "auth"):
            raise exceptions.APIException('用户验证信息格式有误')

        if auth_list[1] != 'yan':
            raise exceptions.APIException('用户信息有误')
        # 校验是否存在此用户
        user = User.objects.filter(username="python").first()

        if not user:
            raise exceptions.APIException('用户不存在')
        return (user, None)
