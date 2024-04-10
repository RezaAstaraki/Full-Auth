from django.conf import settings
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from djoser.social.views import ProviderAuthView


class CustomProviderAuthView(ProviderAuthView):
    def post(self, request, *args, **kwargs):
        print('*********************ProviderAuthView*****************************')
        response = super().post(request, *args, **kwargs)

        if response.status_code == 201:
            response_data = response.data  # Access response data directly
            access_token = response_data.get('access')
            refresh_token = response_data.get('refresh')
            if access_token:
                response.set_cookie(
                    'access',
                    access_token,
                    max_age=settings.AUTH_COOKIE_ACCESS_MAX_AGE,
                    secure=settings.AUTH_COOKIE_SECURE,
                    httponly=settings.AUTH_COOKIE_PATH,
                    path=settings.AUTH_COOKIE_PATH,
                    samesite=settings.AUTH_COOKIE_SAME_SITE,
                )
            if refresh_token:
                response.set_cookie(
                    'refresh',
                    refresh_token,
                    max_age=settings.AUTH_COOKIE_REFRESH_MAX_AGE,
                    secure=settings.AUTH_COOKIE_SECURE,
                    httponly=settings.AUTH_COOKIE_PATH,
                    path=settings.AUTH_COOKIE_PATH,
                    samesite=settings.AUTH_COOKIE_SAME_SITE,
                )

        return response


class CustomTokenObtainPairView(TokenObtainPairView):

    def post(self, request: Request, *args, **kwargs):
        print('*********************create*****************************')
        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            access_token = response.data.get('access')
            refresh_token = response.data.get('refresh')
            print(response.data.get('refresh'))

            response.set_cookie(
                'access',
                access_token,
                max_age=settings.AUTH_COOKIE_ACCESS_MAX_AGE,
                secure=settings.AUTH_COOKIE_SECURE,
                httponly=settings.AUTH_COOKIE_PATH,
                path=settings.AUTH_COOKIE_PATH,
                samesite=settings.AUTH_COOKIE_SAME_SITE,
            )
            response.set_cookie(
                'refresh',
                refresh_token,
                max_age=settings.AUTH_COOKIE_REFRESH_MAX_AGE,
                secure=settings.AUTH_COOKIE_SECURE,
                httponly=settings.AUTH_COOKIE_PATH,
                path=settings.AUTH_COOKIE_PATH,
                samesite=settings.AUTH_COOKIE_SAME_SITE,
            )
            # response = Response(status=status.HTTP_204_NO_CONTENT)

        return response


class CustomTokenRefreshView(TokenRefreshView):

    def post(self, request: Request, *args, **kwargs) -> Response:
        print('CustomTokenRefreshView post method is called ',
              '**********************refresh****************************')
        refresh_token = request.COOKIES.get('refresh')

        if refresh_token:
            request.data['refresh'] = refresh_token

        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            access_token = response.data.get('access')

            response.set_cookie(
                'access',
                access_token,
                max_age=settings.AUTH_COOKIE_ACCESS_MAX_AGE,
                secure=settings.AUTH_COOKIE_SECURE,
                httponly=settings.AUTH_COOKIE_PATH,
                path=settings.AUTH_COOKIE_PATH,
                samesite=settings.AUTH_COOKIE_SAME_SITE,
            )

            refresh_token = response.data.get('refresh')
            if refresh_token:
                response.set_cookie(
                    'refresh',
                    refresh_token,
                    max_age=settings.AUTH_COOKIE_REFRESH_MAX_AGE,
                    secure=settings.AUTH_COOKIE_SECURE,
                    httponly=settings.AUTH_COOKIE_PATH,
                    path=settings.AUTH_COOKIE_PATH,
                    samesite=settings.AUTH_COOKIE_SAME_SITE,
                )
                # response = Response(status=status.HTTP_204_NO_CONTENT)

        return response


class CustomTokenVerifyView(TokenVerifyView):
    def post(self, request, *args, **kwargs):
        print('CustomTokenRefreshView post method is called ',
              '**********************verify****************************')
        access_token = request.COOKIES.get('access')

        if access_token:
            request.data['token'] = access_token

        return super().post(request, *args, **kwargs)


class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        response = Response(status=status.HTTP_204_NO_CONTENT)
        response.delete_cookie('access')
        response.delete_cookie('refresh')
        return response
