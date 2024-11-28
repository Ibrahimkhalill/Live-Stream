import json
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.decorators import api_view

from .models import DeviceInfo



@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Parse the request body
            print(data)  # Debug: Check what data is received

            username = data.get('username')
            password = data.get('password')
            device_info = data.get('deviceInfo')  # Get the device information

            # Check if device_info is present
            if not device_info:
                return JsonResponse({'success': False, 'message': 'Device information is missing'}, status=400)

            # Authenticate the user
            user = authenticate(username=username, password=password)
            if not user:
                return JsonResponse({'success': False, 'message': 'User not found'}, status=400)

            # Check password
            if not user.check_password(password):
                return JsonResponse({'success': False, 'message': 'Invalid password'}, status=400)

            # Retrieve or create the DeviceInfo object for the user
            device, created = DeviceInfo.objects.get_or_create(user=user)

            # If it's the first login, save the device info
            if created or not device.deviceID:
                device.deviceID = device_info.get('hostname')  # Save the deviceID
                device.device_info = device_info  # Save the device information as JSON
                device.save()
                return JsonResponse({'success': True, 'message': 'First-time login successful'})

            # Check if the device info matches
            if device.deviceID != device_info.get('hostname'):
                return JsonResponse({'success': False, 'message': 'Login from a new device is not allowed'}, status=400)

            return JsonResponse({'success': True, 'message': 'Login successful'})

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Invalid JSON format'}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)

    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)


from rest_framework.views import APIView
from rest_framework.response import Response
from .models import LiveStream
from .serializers import LiveStreamSerializer

class LiveStreamListView(APIView):
    def get(self, request):
        streams = LiveStream.objects.all()
        serializer = LiveStreamSerializer(streams, many=True)
        return Response(serializer.data)
    


@api_view(['POST'])
def logout(request):
    try:
        username = request.data.get('username')
       
        # Find the user by username
        user = User.objects.get(username=username)
    
        # Logic to remove the device ID from the user (this depends on your app's implementation)
        # For example, if you're storing device information in a separate model, you can delete it here
        user_device = DeviceInfo.objects.filter(user=user).first()
        if user_device:
            user_device.delete()
            

        # Perform logout logic, such as clearing the session or JWT token
        # Django will clear the session automatically if using Django's default session-based authentication
        
        return Response({'success': True}, status=200)
    
    except User.DoesNotExist:
        return Response({'success': False, 'message': 'User not found'}, status=400)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=500)