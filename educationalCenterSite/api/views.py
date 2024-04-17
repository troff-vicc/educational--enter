from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserAdminsSerializer
class UserAdminViews(APIView):
    def post(self, request, format=None):
        serializer = UserAdminsSerializer(data=request.data)
        if serializer.is_valid():
            import sqlite3
            conn = sqlite3.connect('educationalDate.db')
            cursor = conn.cursor()
            cursor.execute('UPDATE users SET admin = ? WHERE id = ?', (serializer.validated_data['checkAdmin'], serializer.validated_data['idUsers']))
            conn.commit()
            return Response('accepted', status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)