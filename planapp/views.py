from django.shortcuts import render
from .models import *
from .serializers import *
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.response import Response
import uuid
from rest_framework import status,permissions
from django.contrib.auth.models import User




class RegistrationAPIViews(generics.GenericAPIView):
    serializer_class = RegistrationSerializer
    queryset = MobileRechargePlan.objects.all()
    
    def post(self,request):
        serializer = self.get_serializer(data=request.data) 

        if (serializer.is_valid()):
            serializer.save()
            return Response({"RequestId":str(uuid.uuid4()),
            "Message":"User created successfully",
            "User":serializer.data},status=status.HTTP_201_CREATED)
       
        return Response({"Errors":serializer.errors},status=status.HTTP_400_BAD_REQUEST)



class ListPlans(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = MobileRechargePlan.objects.all()
    serializer_class = MobileRechargePlanSerializer

class DetailListPlans(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = MobileRechargePlan.objects.all()
    serializer_class = MobileRechargePlanSerializer


class ListInitiatePlan(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Transaction.objects.all()
    # lookup_field = 'pk'
    serializer_class = TransactionSerializer

class DetailInitiatePlan(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Transaction.objects.all()
    lookup_field = 'pk'
    serializer_class = TransactionSerializer


class ListUser(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer



# Function based for only recharge 

# def list_plan(request):
#     plans = MobileRechargePlan.objects.all()
#     serializer = MobileRechargePlanSerializer(plans,many=True)
#     return JsonResponse({"plans":serializer.data})

# def initiate_recharge(request):
#     plans = Transaction.objects.all()
#     serializer = TransactionSerializer(plans,many=True) 
#     return JsonResponse({"Your Recharge successfull":serializer.data})



