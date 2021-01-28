
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers

from datetime import datetime

from .models import Books

class index(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        all_books = list(Books.objects.all())
        qs_json = serializers.serialize('json', all_books)
        return HttpResponse(qs_json, content_type='application/json')

class reserve(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        message = ''
        try:
            the_book = Books.objects.get(id=id,status=0)
        except ObjectDoesNotExist:
            message = 'erro ao recuperar o livro'
        else:
            the_book.status = 1 #reservado
            the_book.data_reserva = datetime.now()
            the_book.reservado_por = request.user.id
            the_book.save()
            message = 'operacao realizada com sucesso'

        content = { 'message' : message }
        return Response(content)