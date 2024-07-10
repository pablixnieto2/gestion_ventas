def calcular_descuento(precio, porcentaje):
    return precio - (precio * (porcentaje / 100))

def generar_codigo_unico(model, campo):
    import uuid
    codigo = str(uuid.uuid4())[:6].upper()
    while model.objects.filter(**{campo: codigo}).exists():
        codigo = str(uuid.uuid4())[:6].upper()
    return codigo
