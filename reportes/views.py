from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import pandas as pd
from .models import Reporte


def lista_reportes(request):
    if request.method == 'POST':
        consultor_id = request.POST.get('consultor')
        descripcion = request.POST.get('descripcion')
        estado = request.POST.get('estado')

        consultor = None
        if consultor_id and consultor_id.isdigit():
            consultor = User.objects.get(id=consultor_id)

        Reporte.objects.create(
            consultor=consultor,
            descripcion=descripcion,
            estado=estado
        )

        messages.success(request, "Reporte registrado correctamente.")
        return redirect('lista_reportes')

    reportes = Reporte.objects.all().order_by('id')

    return render(request, 'reportes/lista_reportes.html', {
        'reportes': reportes,
        'users': User.objects.all()
    })


def editar_reporte(request, id):
    reporte = get_object_or_404(Reporte, id=id)

    if request.method == 'POST':
        consultor_id = request.POST.get('consultor')
        descripcion = request.POST.get('descripcion')
        estado = request.POST.get('estado')

        if consultor_id and consultor_id.isdigit():
            reporte.consultor_id = consultor_id
        else:
            reporte.consultor = None

        reporte.descripcion = descripcion
        reporte.estado = estado
        reporte.save()

        messages.success(request, "Reporte actualizado correctamente.")
        return redirect('lista_reportes')

    return redirect('lista_reportes')


def reporte_pdf(request, reporte_id):
    reporte = get_object_or_404(Reporte, id=reporte_id)

    html_string = render_to_string('reportes/reporte_pdf.html', {'reporte': reporte})
    html = HTML(string=html_string)
    pdf = html.write_pdf()

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=reporte_{reporte.id}.pdf'
    return response


def reporte_excel(request, reporte_id):
    reporte = get_object_or_404(Reporte, id=reporte_id)

    data = {
        'ID': [reporte.id],
        'Consultor': [reporte.consultor.username if reporte.consultor else "Sin asignar"],
        'Fecha de Emisión': [reporte.fecha_emision],
        'Descripción': [reporte.descripcion],
        'Estado': [reporte.estado],
    }

    df = pd.DataFrame(data)
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = f'attachment; filename=reporte_{reporte.id}.xlsx'
    df.to_excel(response, index=False)
    return response


def eliminar_reporte(request, reporte_id):
    reporte = get_object_or_404(Reporte, id=reporte_id)
    reporte.delete()
    messages.success(request, "Reporte eliminado correctamente.")
    return redirect('lista_reportes')
