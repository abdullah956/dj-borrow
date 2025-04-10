from django.shortcuts import render
import google.generativeai as genai
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

genai.configure(api_key=settings.GOOGLE_GEMINI_API_KEY)

def chatbot_page(request):
    return render(request, "borrow.html")

@csrf_exempt
def chatbot_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_input = data.get("message", "")

        # Use a working model like "chat-bison-001"
        model = genai.GenerativeModel("models/gemini-1.5-pro")
        response = model.generate_content(user_input)  # Using generateText method

        return JsonResponse({"response": response.text})

    return JsonResponse({"error": "Invalid request"}, status=400)

