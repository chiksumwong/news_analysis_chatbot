from rest_framework_mongoengine import serializers
from chatbot.models import News
 
class NewsSerializer(serializers.DocumentSerializer):
    class Meta:
        model = News
        fields = '__all__'