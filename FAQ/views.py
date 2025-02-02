from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.cache import cache
from .models import FAQ
from .serializers import FAQSerializer


class FAQListView(APIView):
    def get(self, request):
        """Returns FAQs in the requested language using Redis cache"""
        lang = request.query_params.get("lang", "en")

        # Check if cached data exists
        cached_faqs = cache.get(f"faqs_{lang}")

        if cached_faqs:
            return Response(cached_faqs)  # Return cached data

        # If not cached, fetch from DB and store in cache
        faqs = FAQ.objects.all()
        serializer = FAQSerializer(
            faqs, many=True, context={
                "request": request})
        cache.set(
            f"faqs_{lang}",
            serializer.data,
            timeout=400)  # Cache

        return Response(serializer.data)
