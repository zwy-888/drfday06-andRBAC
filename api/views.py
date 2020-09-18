from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.authenticator import MyAuthentication
from api.Permission import MyPermission
from rest_framework.throttling import UserRateThrottle

from api.throttles import MyThrottles


class UserAPIView(APIView):
    # 局部配置
    authentication_classes = [MyAuthentication]  # 认证局部配置
    permission_classes = [MyPermission]  # 权限局部配置
    # throttle_classes = [UserRateThrottle]
    # scope = 'user'
    throttle_classes = [MyThrottles]
    scope = 'sms'

    """
    
1.AllowAny
has_permission()没有做任何处理直接返回True允许任何请求访问
2.IsAuthenticated
只允许认证通过的用户访问，游客无权访问
3.IsAdminUser
只允许超级管理员访问游客普通用户都没有权限登录后的管理员才有权限
4.IsAuthenticatedOrReadOnly
已经认证通过的用户可以进行读写操作，游客只读"""

    def post(self, request, *args, **kwargs):
        print(request)
        return Response('postok')

    def get(self, request, *args, **kwargs):
        return Response('getok')

    """
    找到相应的默认配置，可以自己重写，可以在局部（view中进行配置）优先使用局部中的配置
    定义类进行方法重写，将此类放入局部配置中即可调用自己的重写方法
    """
