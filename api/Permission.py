from rest_framework.permissions import BasePermission

from api.models import User


class MyPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method in ('GET', "HEAD", "OPTIONS"):
            return True
        username = request.data.get("username")
        # 如果用户访问时写操作 判断用户是否有登录信息
        # 应该获取前端信息
        user = User.objects.filter(username=username).first()
        if user:
            return True
        return False

