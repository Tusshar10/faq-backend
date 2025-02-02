import pytest
from rest_framework.test import APIClient
from FAQ.models import FAQ


@pytest.mark.django_db
def test_faq_api_returns_translated_content():
    """Test if API returns the correct translated content based on language"""
    FAQ.objects.create(
        question="How does caching work?",
        answer="Caching stores data for quick retrieval.",
        question_hi="कैशिंग कैसे काम करती है?",
        answer_hi="कैशिंग डेटा को त्वरित पुनर्प्राप्ति के लिए संग्रहीत करता है।",
        question_bn="ক্যাশিং কীভাবে কাজ করে?",
        answer_bn="ক্যাশিং দ্রুত পুনরুদ্ধারের জন্য ডেটা সংরক্ষণ করে।",
    )

    client = APIClient()

    # Test default (English)
    response = client.get("/api/faqs/")
    assert response.status_code == 200
    response_data = response.json()
    assert response_data[0]["question"] == "How does caching work?"
    assert response_data[0]["answer"] == "Caching stores data for quick retrieval."

    # Test Hindi translation
    response_hi = client.get("/api/faqs/?lang=hi")
    assert response_hi.status_code == 200
    response_data_hi = response_hi.json()
    assert response_data_hi[0]["question"] == "कैशिंग कैसे काम करती है?"
    assert response_data_hi[0]["answer"] == "कैशिंग डेटा को त्वरित पुनर्प्राप्ति के लिए संग्रहीत करता है।"

    # Test Bengali translation
    response_bn = client.get("/api/faqs/?lang=bn")
    assert response_bn.status_code == 200
    response_data_bn = response_bn.json()
    assert response_data_bn[0]["question"] == "ক্যাশিং কীভাবে কাজ করে?"
    assert response_data_bn[0]["answer"] == "ক্যাশিং দ্রুত পুনরুদ্ধারের জন্য ডেটা সংরক্ষণ করে।"
