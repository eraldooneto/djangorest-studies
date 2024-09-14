from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

"""
This code creates a serializer to the model Snippet, that serializes the data from the model to JSON format.
It can be used for: 
- Validate the input data
- Create new Snippets models in the database
- Update Snippets models in the database
- Serialize the objects to an adequate format for APIs, like JSON
"""


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
    
