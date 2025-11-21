import re
from django.core.exceptions import ValidationError

def max_words_validator(value):
    words = re.findall(r'\b\w+\b', value)
    if len(words) > 500:
        raise ValidationError(f"Max 500 words allowed. You wrote {len(words)}.")
