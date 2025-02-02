import pytest
from FAQ.models import FAQ


@pytest.mark.django_db
def test_faq_model_auto_translation():
    """Test if the FAQ model automatically translates questions and answers"""
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a Python web framework."
    )

    assert faq.question_hi is not None
    assert faq.question_bn is not None
    assert faq.answer_hi is not None
    assert faq.answer_bn is not None
