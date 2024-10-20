from rest_framework import serializers
from .models import Authenication, SupervisorAuthenication

class userserializers(serializers.ModelSerializer):
    class Meta:
        model = Authenication
        fields = ['id','username','password']


class supervisorserializers(serializers.ModelSerializer):
    class Meta:
        model = SupervisorAuthenication
        fields = ['id','username','password']