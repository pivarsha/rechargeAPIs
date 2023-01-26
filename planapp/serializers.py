from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50, min_length=6)
    username = serializers.CharField(max_length=50, min_length=6)
    password = serializers.CharField(max_length=100, write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'username',
            'password',
        )

    def validate(self, args):
        email = args.get("email",None)  #mishrasonu921@gmail.com
        username = args.get("username",None)    #guthlii

        if User.objects.filter(email=email).exists(): #mishrasonu921@gmail.com 
            raise serializers.ValidationError({"Email":("Email already exists")}) 

        if User.objects.filter(username=username).exists(): #guthlii 
            raise serializers.ValidationError({"Username":("This username is already exists")})
        
        return super().validate(args) # mishrasonu921@gmail.com , guthlii
    

    def create(self, validated_data): 
        return User.objects.create_user(**validated_data) #mishrasonu9211@gmail.com,guthlii








class MobileRechargePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileRechargePlan
        fields = ("id","name","price","validity","network")




class UserSerializer(serializers.ModelSerializer):
    recharge = serializers.PrimaryKeyRelatedField(many=True,queryset=MobileRechargePlan.objects.all())
    transac = serializers.PrimaryKeyRelatedField(many=True,queryset=Transaction.objects.all())

    class Meta:
        model = User
        fields = ('id','username','email','recharge','transac')


class MobileRechargePlanUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email')




class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ("id","plan","phone_number","amount","status","network")