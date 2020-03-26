from rest_framework import serializers
from .models import User,Profile

class RegisterSerializer(serializers.ModelSerializer):
    password    =   serializers.CharField(max_length=120,min_length=8,write_only=True)
    confirm_password    = serializers.CharField(max_length=120,min_length=8,write_only=True)



    class Meta:
        model   =   User
        fields  =   ['username','email','password','confirm_password','role']


    def validate(self,data):
        confirm_password    =   data['confirm_password']
        password            =   data['password']
        if not self.do_password_match(password,confirm_password):
            return serializers.ValidationError({'password':'password do not match.'})
        return data

    def create(self,validated_data):
        del validated_data['confirm_password']
        return User.objects.create_user(**validated_data)

    def do_password_match(self,password1,password2):
        return password1==password2


class ProfileSerializer(serializers.ModelSerializer):
    class   Meta:
        model  =   Profile
        fields  =   '__all__'
