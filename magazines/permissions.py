import requests
from rest_framework.permissions import BasePermission


class IsAdminPermission(BasePermission):
    def has_permission(self, request, view):
        token = get_token(request)
        if token:
            data = {'token': token}
            url = "http://172.20.0.2:8001/api/v1/is_admin/"
            response = requests.post(url=url, json=data)
            if response.status_code == 200:
                data = response.json()
                return bool(data['is_admin'])
        return False



def get_token(request):
    auth_header = request.headers.get('Authorization')
    if auth_header.startswith('Token '):
        token = auth_header[len('Token '):]
        return token
    return None
