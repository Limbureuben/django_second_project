from django.http import JsonResponse
from django.shortcuts import render
from projectBuilders.projectBuilders import UserBuilder
from project_dto.project import *
from .models import *
import graphene
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.views import APIView
from .serializer import FileSerializer
from .models import Files
from rest_framework.response import Response
from graphene import Mutation, Boolean, String
from django.core.exceptions import PermissionDenied


    
class RegisterUser(graphene.Mutation):
    user = graphene.Field(UserRegistrationObject)
    success = graphene.Boolean()
    message = graphene.String()
    
    class Arguments:
        input = UserRegistrationInputObject(required=True)
        
    def mutate(self, info, input):
        username = input.username
        email = input.email
        password = input.password
        password_confirm = input.password_confirm
        
        ##check if the user exist
        if User.objects.filter(username=username).exists():
            return RegisterUser(success=False, message="username alredy exists")
        
        ##check if the email exist
        if User.objects.filter(email=email).exists():
            return RegisterUser(success=False, message="Email alredy exists")
        
        if password != password_confirm:
            return RegisterUser(success=False, message="Passwords do not match")
        
        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        return RegisterUser(
            user = UserRegistrationObject(id=user.id, username=user.username, email=user.email),
            success = True,
            message = "Registration successfully"
        )
        
        
class LoginUser(graphene.Mutation):
    # user = graphene.Field(UserLoginObject)
    # success = graphene.Boolean()
    user = graphene.Field(UserLoginObject)
    success = graphene.Boolean()
    message = graphene.String()

    
    class Arguments:
        input = UserLoginInputObject(required=True)
        
    def mutate(self, info, input):
       username = input.username
       password = input.password
       
       try:
           # Authenticate and log in the user
            result = UserBuilder.login_user(username, password)
            user = result['user']
            return LoginUser(
                user = UserLoginObject(
                    id = user.id,
                    username = user.username,
                    email = user.email,
                    refresh_token = result['refresh_token'],
                    access_token = result['access_token']
                ),
                success=True,
                message="Login successful"
            )
       except PermissionDenied as e:
           return LoginUser(success=False, message=str(e))

















class FileUploadView(APIView):
    
    def post(self, request):
        file = request.FILES.get("file")
        
        if file:
            try:
                saved_file = Files.objects.create(file=file)
                return Response({"error": False, "data": FileSerializer(saved_file).data})
            except Exception as e:
                return Response({"error": True, "message": str(e)})
            
        return Response({"error": True, "message": "No file uploaded"})
    
    def get(self, request):
        try:
            data = Files.objects.all()
            return Response(FileSerializer(instance=data, many=True).data)
        except Exception as e:
            return Response({"error": True, "message": str(e)})















































































































# @csrf_exempt
# def execute_code(request):
#     if request.method == 'POST':
#         try:
#             # Parse the JSON data
#             data = json.loads(request.body)
#             temperature = data.get('temperature')
#             humidity = data.get('humidity')

#             # Print the temperature and humidity to the console
#             print(f"Temperature: {temperature} °C")
#             print(f"Humidity: {humidity} %")

#             # Save data to the Weather model
#             if temperature is not None and humidity is not None:
#                 Weather.objects.create(
#                     temperature=int(temperature),  # Ensure it's stored as an integer
#                     humidity=int(humidity)         # Ensure it's stored as an integer
#                 )
#                 return JsonResponse({'status': 'success', 'message': 'Data received and stored successfully'}, status=200)
#             else:
#                 return JsonResponse({'status': 'error', 'message': 'Invalid data'}, status=400)
#         except json.JSONDecodeError:
#             return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
#         except ValueError:
#             return JsonResponse({'status': 'error', 'message': 'Invalid data type'}, status=400)
#     else:
#         return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

# from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .models import Weather
# # from .serializers import WeatherSerializer
# # import pandas as pd
# from rest_framework.views import APIView
# from .serializer import FileSerializer
# from .models import Files

# from rest_framework.parsers import FileUploadParser
# @api_view(['GET'])
# def hourly_average_summary(request):
#     data = Weather.objects.all().order_by('created_at')
#     serializer = WeatherSerializer(data, many=True)
#     df = pd.DataFrame(serializer.data)
#     df['created_at'] = pd.to_datetime(df['created_at'])
#     df.set_index('created_at', inplace=True)
#     df_resampled = df.resample('10T').agg({
#         'temperature': 'mean',
#         'humidity': 'mean'
#     }).reset_index()
#     df_resampled.fillna(0, inplace=True)  # Replace NaN values with 0
    
#     df_resampled.replace([float('inf'), float('-inf')], 0, inplace=True)  # Replace infinite values with 0
    
#     # Delete rows where either 'Temperature Average' or 'Humidity Average' is 0
#     df_resampled = df_resampled[(df_resampled['temperature'] != 0) & (df_resampled['humidity'] != 0)]
#     df_resampled.replace([float('inf'), float('-inf')], 0, inplace=True)  # Replace infinite values with 0
#     df_resampled.columns = ['Date', 'Temperature Average', 'Humidity Average']
#     response_data = df_resampled.to_dict(orient='records')
#     return Response(response_data)



# @api_view(['GET'])
# def current_weather(request):
#     try:
#         # Retrieve the latest weather record
#         latest_weather = Weather.objects.latest('created_at')
        
#         # Serialize the latest weather record
#         serializer = WeatherSerializer(latest_weather)
        
#         # Return the serialized data
#         return Response(serializer.data)
    
#     except Weather.DoesNotExist:
#         # If no weather data is available, return an empty response or an error message
#         return Response({"error": "No weather data available."}, status=404)
    
    
