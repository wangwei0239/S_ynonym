from django.http import HttpResponse
from django.http import StreamingHttpResponse
from . import settings
import os


def process_upload_file(request):
    file = request.FILES.get('source_file',None)
    if file is None:
        return HttpResponse("file not exist in the request")

    file_path = os.path.join(settings.BASE_DIR, '1.txt')
    dest = open(file_path, 'wb+')
    dest.write(file.read())
    dest.close()
    return HttpResponse("upload success")


def download_file(request):
    file = os.path.join(settings.BASE_DIR, '1.txt')
    response = StreamingHttpResponse(read_file(file))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format('1.txt')
    return response


def read_file(filename, chunk_size=512):
    with open(filename, 'rb') as f:
        while True:
            c=f.read(chunk_size)
            if c:
                yield c
            else:
                break