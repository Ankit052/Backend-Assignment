from django.db import models
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta :
        model = User
        fields = "__all__"


    def validate(self, data):
        
        if data["first_name"]: 
            if not data["first_name"].isalpha():
                raise serializers.ValidationError({'error':"Please enter a valid first name"})        

            first_name=data["first_name"]
            data["first_name"] = first_name.capitalize()

            
        if data["last_name"]:
            if not data["last_name"].isalpha():
                raise serializers.ValidationError({'error':"Please enter a valid last name"})

            last_name=data["last_name"]
            data["last_name"] = last_name.capitalize()


        if data["city"]:
            city=data["city"]
            data["city"] = city.title()


        if data["state"]:
                state=data["state"]
                data["state"] = state.title()

        if data["zip"]:
            for i in data['zip']:
                if not i.isdigit():
                    raise serializers.ValidationError({'error':"Please enter a valid zip"})


        if data["company_name"]:
            company_name = data["company_name"]
            data["company_name"] = company_name.title()
            

        return data
