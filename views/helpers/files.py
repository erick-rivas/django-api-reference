import os
import uuid

from django.core.files.storage import default_storage
from rest_framework import views
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from models.helpers.file import File
from serializers.helpers.file import FileSerializer


class FileView(views.APIView):  #

    parser_classes = (MultiPartParser,)

    def post(self, request):  #
        f = request.data['file']
        filename = uuid.uuid4().hex + "_" + f.name

        name = default_storage.save(filename, f)
        size = default_storage.size(name)
        url = default_storage.url(name)
        host_url = os.getenv('HOST_URL')
        url = url if url.startswith("http") else host_url + url

        model = File.objects.create(name=name, size=size, url=url)
        serializer = FileSerializer(model, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)