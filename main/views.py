from django.shortcuts import render
from django.http import HttpResponse
from .models import Components
from io import BytesIO
from docx import Document
# Create your views here.
def index(request):
    cpu = Components.objects.all().filter(type="Процессор")
    gpu = Components.objects.all().filter(type="Видеокарта")
    mather = Components.objects.all().filter(type="Материнская плата")
    ram = Components.objects.all().filter(type='Оперативная память')
    power_block = Components.objects.all().filter(type='Блок питания')
    hdd = Components.objects.all().filter(type="Накопитель")
    mouse = Components.objects.all().filter(type="Мышка")
    keyboard = Components.objects.all().filter(type="Клавиатура")
    monitor = Components.objects.all().filter(type="Монитор")
    return render(request, 'main/index.html', {"cpu" : cpu, "gpu" : gpu,
     "mather" : mather, "ram" : ram, "power_block" : power_block,
      "hdd" : hdd, "mouse" : mouse, "keyboard" : keyboard, "monitor" : monitor})

def get_docx(request):
    text = request.POST['text-docx']
    document = Document()
    text = text.replace('<br>', '\n')
    document.add_paragraph(f"{text}")
    f = BytesIO()
    document.save(f)
    length = f.tell()
    f.seek(0)
    response = HttpResponse(
        f.getvalue(),
        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )
    response['Content-Disposition'] = 'attachment; filename= Ваша сборка.docx'
    response['Content-Length'] = length
    return response