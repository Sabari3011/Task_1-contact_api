from rest_framework import serializers
from .models import ContactModel


class ContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ContactModel
        fields = '__all__'

    def validate_message(self , data):
        if (len(data) < 6 ):
            raise serializers.ValidationError("message Field atleast requires 6 characters")
        return data
        # print("..............................................",data)