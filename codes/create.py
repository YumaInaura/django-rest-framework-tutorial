#!/usr/bin/env python

# Usage

# ./manage.py shell < ./codes/create.py 
# ./manage.py shell < ./codes/create.py | jq

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

import json

snippet = Snippet(code='print("hello, world")\n')
snippet.save()

serializer = SnippetSerializer(snippet)

print(json.dumps(serializer.data))

