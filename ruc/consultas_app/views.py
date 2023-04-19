

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import rucs

def mostrar_ruc(request, ruc):
    try:
        ruc_obj = rucs.objects.get(ruc=ruc)
    except rucs.DoesNotExist:
        return JsonResponse({'error': 'La RUC no fue encontrada'}, status=404)
    


    data = {
        'RUC': ruc_obj.ruc,
        'Razon_social': ruc_obj.razon_social if ruc_obj.razon_social != '-' else '',
        'Estado_del_contribuyente': ruc_obj.estado_del_contribuyente if ruc_obj.estado_del_contribuyente != '-' else '',
        'Condicion_de_domicilio': ruc_obj.condicion_de_domicilio if ruc_obj.condicion_de_domicilio != '-' else '',
        'Ubigeo': ruc_obj.ubigeo if ruc_obj.ubigeo != '-' else '',
        'direccion': f"{ruc_obj.tipo_via if ruc_obj.tipo_via != '-' else ''} {ruc_obj.nombre_via if ruc_obj.nombre_via != '-' else ''} {ruc_obj.codigo_zona if ruc_obj.codigo_zona != '-' else ''} {ruc_obj.tipo_zona if ruc_obj.tipo_zona != '-' else ''} {ruc_obj.numero if ruc_obj.numero != '-' else ''} {ruc_obj.interior if ruc_obj.interior != '-' else ''} {ruc_obj.lote if ruc_obj.lote != '-' else ''} {ruc_obj.departamento if ruc_obj.departamento != '-' else ''} {ruc_obj.manzana if ruc_obj.manzana != '-' else ''} {ruc_obj.kilometro if ruc_obj.kilometro != '-' else ''}".rstrip()
    }
        
    return JsonResponse(data)



