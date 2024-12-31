import os
import pandas as pd
from django.conf import settings
from django.http import FileResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework import status
from .models import UploadedFile
from .utils.logging_utils import log_function_call
import logging
import uuid

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated, AllowAny

logger = logging.getLogger('api.services')


@log_function_call
def process_this(file_path):
    """
    Process the uploaded CSV file and add a new column 'Processed'.
    """
    try:
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Example processing: Add a new column
        df['Processed'] = df.sum(axis=1)
        
        # Save the processed file
        processed_file_path = file_path.replace('.csv', '_processed.csv')
        df.to_csv(processed_file_path, index=False)
        
        return processed_file_path
    except Exception as e:
        raise ValueError(f"Error processing file: {e}")


class FileUploadView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    @log_function_call
    def post(self, request, *args, **kwargs):
        print('FileUploadView.post:')
        file = request.FILES['file']
        try:
            # Generate a unique filename
            file_extension = file.name.split('.')[-1]
            unique_filename = f"{uuid.uuid4().hex}.{file_extension}"

            # Save file to the local filesystem
            upload_dir = os.path.join(settings.MEDIA_ROOT, 'uploads')
            os.makedirs(upload_dir, exist_ok=True)
            file_path = os.path.join(upload_dir, unique_filename)

            with open(file_path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

            # Save metadata to the database
            uploaded_file = UploadedFile.objects.create(
                file_name=unique_filename,
                original_name=file.name,
                file_path=file_path
            )

            return Response({'message': 'File uploaded successfully.', 'file_id': uploaded_file.id})
        except Exception as e:
            logger.error(f"Error in FileUploadView.post: {e}")
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @log_function_call
    def put(self, request, *args, **kwargs):
        """
        Process the uploaded file based on the file ID.
        """
        print('FileUploadView.put:')
        file_id = request.data.get('file_id')
        if not file_id:
            return Response({'error': 'File ID not provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Retrieve file metadata
            uploaded_file = UploadedFile.objects.get(id=file_id)
            
            # Process the file
            processed_file_path = process_this(uploaded_file.file_path)
            
            return Response({
                'message': 'File processed successfully.',
                'processed_file_path': processed_file_path
            })
        except UploadedFile.DoesNotExist:
            return Response({'error': 'File not found'}, status=status.HTTP_404_NOT_FOUND)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @log_function_call
    def get(self, request, *args, **kwargs):
        """
        Handle file download by returning the file as a response.
        """
        print('FileUploadView.get:')
        file_path = request.query_params.get('file_path')
        if not file_path:
            return Response({'error': 'File path not provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Ensure the file exists before returning it
            if os.path.exists(file_path):
                return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=os.path.basename(file_path))
            else:
                return Response({'error': 'File not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# In some file, e.g., views.py in an "api" app
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from allauth.account.utils import setup_user_email
from allauth.account.models import EmailAddress
from django.contrib.auth.models import User

class SignupView(APIView):
    permission_classes = [AllowAny]  # So anonymous users can create an account
    
    def post(self, request):
        email = request.data.get('email')
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')
        
        if not email or not password1:
            return Response({'error': 'Email and password are required.'}, status=400)
        
        if password1 != password2:
            return Response({'error': 'Passwords do not match'}, status=400)
        
        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email already in use'}, status=400)
        
        # Create user
        user = User.objects.create_user(username=email, email=email, password=password1)
        
        # Mark email as verified or handle actual verification flow
        EmailAddress.objects.create(user=user, email=email, primary=True, verified=True)
        
        return Response({'success': 'User created'}, status=201)
    
from rest_framework.views import APIView
from rest_framework.response import Response


# @method_decorator(csrf_exempt, name="dispatch")
# class UserInfoView(APIView):
#     permission_classes = [AllowAny]
    
#     @log_function_call
#     def get(self, request):
#         user = request.user
#         logger.info(f'username: {user.username}')
#         logger.info(f'email: {user.email}')
#         return Response({
#             'username': user.username,
#             'email': user.email,
#         })

@method_decorator(csrf_exempt, name="dispatch")
class UserInfoView(APIView):
    permission_classes = [AllowAny]

    @log_function_call
    def get(self, request):
        if request.user.is_authenticated:
            return Response({
                "authenticated": True,
                "username": request.user.username,
                "email": request.user.email,
            })
        else:
            return Response({"authenticated": False})

from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login

@method_decorator(csrf_exempt, name="dispatch")
class LoginView(APIView):
    permission_classes = [AllowAny]
    @log_function_call
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return Response({"success": True})
        return Response({"error": "Invalid credentials"}, status=400)