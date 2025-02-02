from rest_framework import serializers
from .models import FAQ


class FAQSerializer(serializers.ModelSerializer):
    question = serializers.SerializerMethodField()
    answer = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = ["id", "question", "answer"]  

    def get_question(self, obj):
        """Return translated question based on request language"""
        lang = self.context.get("request").query_params.get("lang", "en")
        return obj.get_translated_content(lang)["question"]

    def get_answer(self, obj):
        """Return translated answer based on request language"""
        lang = self.context.get("request").query_params.get("lang", "en")
        return obj.get_translated_content(lang)["answer"]
