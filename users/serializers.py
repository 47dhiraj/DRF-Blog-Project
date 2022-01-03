from rest_framework import serializers
from users.models import NewUser


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    email = serializers.EmailField(required=True)
    user_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = NewUser
        fields = ('id', 'email', 'user_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}               # password lai read garna namilos from browser url or postman bata

    # serializers.py file ko serializer.save() run hunda yo create method call huncha...... Just ModelSerializer ko in-built create method lai overwrite gareko
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this

        instance = self.Meta.model(**validated_data)            # validated_data json format ma auncha but database ma data save garda model instance or as  a object ko rupma data save garnu parcha tesailey yo line le josn data lai model instance ma lai jancha.
        if password is not None:
            instance.set_password(password)                     # set_password method django ko inbuilt method ho... yesle paswword encryption gacha.
        instance.save()
        return instance
