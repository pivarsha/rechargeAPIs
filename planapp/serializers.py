from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50,min_length=6)
    username = serializers.CharField(max_length=50,min_length=4)
    password = serializers.CharField(max_length=150,write_only=True)
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            'username',
            "password",
        )

    def validate(self,args):
        email = args.get('email',None)
        username = args.get('username',None)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email':('email already exists')})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                {'Username':('username already exists')})
        return super().validate(args)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class MobileRechargePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileRechargePlan
        fields = ("id","name","price","validity","network")



class UserSerializer(serializers.ModelSerializer):
    mob = serializers.PrimaryKeyRelatedField(many=True,queryset= MobileRechargePlan.objects.all())
    Transac = serializers.PrimaryKeyRelatedField(many=True,queryset= Transaction.objects.all())
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'mobile',
            'transac'
        )

class MobileRechargePlanUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email')



class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ("id","plan","phone_number","amount","status","network")