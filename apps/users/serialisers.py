from rest_framework import serializers
from  .models import User

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','password'
                 )
        
class RegisterSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(
        max_length = 255, write_only = True
    )
    password2 = serializers.CharField(
        max_length = 255, write_only = True
    )
    
    class Meta:
        model = User
        fields = ('id', 'username','password','password2'
                 )
        
    def validate(self, attrs):
        if attrs['password'] !=attrs['password2']:
            raise serializers.ValidationError({'password': 'Пароли отличаются'})
        return super().validate(attrs)
    
    def create(self,validated_data):
        user = User.objects.create(
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user