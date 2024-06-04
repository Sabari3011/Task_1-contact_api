from django.shortcuts import render , HttpResponse
from rest_framework.response import Response
# Create your views here.
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
@api_view(["POST",])
def logoutUser(req):
    if req.method == 'POST':
        req.user.auth_token.delete()
        return Response({"msg":"deleted Successfuly"})



def userlogin(req):
    data = {"login":"trigered"}
    return HttpResponse(data)



class CheckApi(APIView):
    permission_classes = [IsAuthenticated]
    

    def get(self,req):
        return Response({"user":"Authenticated" ,"name" : f"{req.user.is_superuser}"})



# class RestrictedView(APIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         return Response(data={"message": "You have access to this restricted content."})