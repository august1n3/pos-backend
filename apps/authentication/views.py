from django.views import View
from django.contrib.auth import aauthenticate, login, logout
from apps.authentication.models import POSUser
from django.http import JsonResponse
import json
class AuthView(View):

    def post(self,request):
        credentials = json.loads(request.body)
        user = aauthenticate(username=credentials["username"], password=credentials["password"])
        try:
            if user is not None:
                login(request, user)
                return JsonResponse({
                    "status": "success",
                    "message": "Login was successfull"
                }, safe=False)
            else:
                return JsonResponse({
                    "status": "success",
                    "message": "Login was successfull"
                }, safe=False)
        except Exception as e:
            return JsonResponse({
                "status": "failed",
                "message": e
            }, safe=False)

    def get(self, request):
        user = request.user
        try:
            if user.is_authenticated:
                logout(request)
            else:
                return JsonResponse({
                    "status": "failed",
                    "message": "no logged in user"
             }, safe=False)
        except Exception as e:
            return JsonResponse({
                "status": "failed",
                "message": e.__str__()
            }, safe=False)

        

        