import os
import google.generativeai as genai
from django.conf import settings

# Set the DJANGO_SETTINGS_MODULE to your project's settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# Import settings after the environment variable is set
from django.conf import settings

# Now, configure the Google Gemini API with your API key
genai.configure(api_key=settings.GOOGLE_GEMINI_API_KEY)

# List available models and convert the generator to a list
models = list(genai.list_models())
print(models)
