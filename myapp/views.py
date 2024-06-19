from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializer import UserInterfaceSerializer
import json
from .models import UserInterface

@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            user_name = data.get("UserName")
            user_email = data.get("UserEmail")
            user_password = data.get("UserPassword")
            user_phone = data.get("UserPhone")
            
            parsed_data = {
                "UserName": user_name,
                "UserEmail": user_email,
                "UserPassword": user_password,
                "UserPhone": user_phone
            }
            
            serializer = UserInterfaceSerializer(data=parsed_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"success": True, "message": "User registered successfully!"}, status=201)
            else:
                return JsonResponse({"success": False, "errors": serializer.errors}, status=400)
        
        except json.JSONDecodeError as e:
            return JsonResponse({"success": False, "message": "Invalid JSON", "details": str(e)}, status=400)
        
    return JsonResponse({"success": False, "message": "Only POST requests are allowed"}, status=405)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get("UserEmail")
            password = data.get("UserPassword")

            if not email or not password:
                return JsonResponse({"success": False, "message": "Email and password are required"}, status=400)

            try:
                user = UserInterface.objects.get(UserEmail=email)
            except UserInterface.DoesNotExist:
                return JsonResponse({"success": False, "message": "User not found"}, status=404)

            if password != user.UserPassword:
                return JsonResponse({"success": False, "message": "Invalid password"}, status=401)

            return JsonResponse({"success": True, "message": "Login successful"}, status=200)

        except json.JSONDecodeError as e:
            return JsonResponse({"success": False, "message": "Invalid JSON", "details": str(e)}, status=400)

    return JsonResponse({"success": False, "message": "Only POST requests are allowed"}, status=405)