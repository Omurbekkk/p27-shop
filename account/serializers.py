from rest_framework import serializers

from .models import User

class RegisterUserSerializer(serializers.ModelSerializer):

    password_confirm = serializers.CharField(min_length=4, required=True)

    class Meta:
        model = User
        fields = ('email', 'phone', 'password', 'password_confirm')

    def validate(self, attrs):
        # ATTRS -> OrderedDict([('email', 'admin1@gmail.com'), ('phone', '996700071102'), ('password', '12345'), ('password_confirm', '12345')])
        pass1 = attrs.get('password')
        pass2 = attrs.pop('password_confirm')
        # ATTRS AFTER POP -> # ATTRS -> OrderedDict([('email', 'admin1@gmail.com'), ('phone', '996700071102'), ('password', '12345')])
        if pass1 != pass2:
            raise serializers.ValidationError('Passwords do not match!')
        return attrs
    
    def validate_email(self, email):
        # EMAIL -> aaaaa@gmail.com
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('User with this email already exists')
        return email
    # User с таким именем уже существует

    def create(self, validated_data):
        # VALIDATED_DATA -> {'email': 'admin3@gmail.com', 'phone': '996700071102', 'password': '12345'}
        return User.objects.create_user(**validated_data)
    
    

    


