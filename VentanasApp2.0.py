def m():
    cuantas_ventanas = int(input("¿Cuántas ventanas desea calcular?"))
    for i in range(cuantas_ventanas):
        print("<--------","Ventana", i + 1,"-------->")
        size()


def size():
    precios_aluminio = {"normal": 3334, "blanco": 2000, "negro": 2667}
    precios_vidrio = {"simple": 30000, "doble": 60000, "oscuro": 80000, "laminado": 120000, "blindex": 150000}
    while True:
            try:
                x = float(input("¿Ancho de la ventana en milímetros?"))
                if x > 1800 or x < 500:
                    print("El ancho no puede ser mayor a 1800 milímetros ni menor a 500 milímetros")
                    continue
                break
            except ValueError:
                print("Por favor ingrese un número válido para el ancho.")
    x = x / 1000
    while True:
            try:
                y = float(input("¿Alto de la ventana en milímetros?"))
                if y > 2500 or y < 300:
                    print("El alto no puede ser mayor a 2500 milímetros ni menor a 300 milímetros")
                    continue
                break
            except ValueError:
                print("Por favor ingrese un número válido para el alto.")
    y = y / 1000
    while True:
            tipo_vidrio = input('¿Qué tipo de vidrio desea? (simple, doble, oscuro, laminado, blindex)')
            tipo_vidrio_precio = precios_vidrio.get(tipo_vidrio, None)
            if tipo_vidrio_precio is not None:
                break
            print("No tenemos ese tipo de vidrio.")
    while True:
            color_aluminio = input('¿Qué color de aluminio desea? (normal, blanco, negro)')
            tipo_aluminio_precio = precios_aluminio.get(color_aluminio, None)
            if tipo_aluminio_precio is not None:
                break
            print("No tenemos ese tipo de aluminio.")
    v = {'x':x, 'y':y, 'tipo_vidrio':tipo_vidrio, 'color_aluminio':color_aluminio}
    return calculo(v)

def calculo(v):

    precios_aluminio = {"normal": 3334, "blanco": 2000, "negro": 2667}
    precios_vidrio = {"simple": 30000, "doble": 60000, "oscuro": 80000, "laminado": 120000, "blindex": 150000}
    x = v['x']
    y = v['y']
    tipo_vidrio = v['tipo_vidrio']
    color_aluminio = v['color_aluminio']
    w = (x * 2) + (y * 2)
    costo_aluminio = round(precios_aluminio[color_aluminio] * w)
    costo_vidrio = round((precios_vidrio[tipo_vidrio] /4.5)*(x * y),2)
    costo = costo_aluminio + costo_vidrio

    material_utilizado_aluminio = round(w, 2)
    material_utilizado_vidrio = round((x * y), 2)
    tira_aluminio = 6
    if w > 6: 
        tira_aluminio = 12
    plancha_vidrio = 4.5

    # Se calcula el valor del material utilizado
    valor_aluminio_utilizado = round(tira_aluminio * precios_aluminio[color_aluminio],2)
    valor_vidrio_utilizado = round(costo_vidrio,2)


    # Se calcula el material sobrante
    material_sobrante_aluminio = round(tira_aluminio - material_utilizado_aluminio, 2)
    material_sobrante_vidrio = round(plancha_vidrio - material_utilizado_vidrio, 2)

    # Se calcula el valor del material sobrante
    valor_sobrante_aluminio = round(material_sobrante_aluminio * precios_aluminio[color_aluminio], 2)
    valor_sobrante_vidrio = round(material_sobrante_vidrio * (precios_vidrio[tipo_vidrio] / 4.5), 2)

    altura_vidrio_sobrante = round(2.5 - y,2) # Y es el alto
    ancho_vidrio_sobrante = round(1.8 - x,2) # X es el ancho
    valores_finales = {
        'x': x,
        'y': y,
        'tipo_vidrio': tipo_vidrio,
        'color_aluminio': color_aluminio,
        'costo_ventana': costo_vidrio + costo_aluminio,
        'costo_ventana_con_ganancia': round((costo_vidrio + costo_aluminio) * (0.35) + (costo_vidrio + costo_aluminio),2),
        'material_utilizado_aluminio': {'metros': material_utilizado_aluminio, 'valor': valor_aluminio_utilizado},
        'material_utilizado_vidrio': {'metros_cuadrados': material_utilizado_vidrio, 'valor': valor_vidrio_utilizado},
        'material_sobrante_aluminio': {'metros': material_sobrante_aluminio, 'valor': valor_sobrante_aluminio},
        'material_sobrante_vidrio': {'metros_cuadrados': material_sobrante_vidrio, 'alto': altura_vidrio_sobrante, 'ancho': ancho_vidrio_sobrante, 'valor': valor_sobrante_vidrio},
    }
    return resultado(valores_finales)

def resultado(valores_finales):
    x = valores_finales['x']
    y = valores_finales['y']
    tipo_vidrio = valores_finales['tipo_vidrio']
    color_aluminio = valores_finales['color_aluminio']
    costo = valores_finales['costo_ventana']
    costo_con_ganancia = valores_finales['costo_ventana_con_ganancia']
    material_utilizado_aluminio = valores_finales['material_utilizado_aluminio']['metros']
    valor_aluminio_utilizado = valores_finales['material_utilizado_aluminio']['valor']
    material_utilizado_vidrio = valores_finales['material_utilizado_vidrio']['metros_cuadrados']
    valor_vidrio_utilizado = valores_finales['material_utilizado_vidrio']['valor']
    material_sobrante_aluminio = valores_finales['material_sobrante_aluminio']['metros']
    valor_sobrante_aluminio = valores_finales['material_sobrante_aluminio']['valor']
    material_sobrante_vidrio = valores_finales['material_sobrante_vidrio']['metros_cuadrados']
    altura_vidrio_sobrante = valores_finales['material_sobrante_vidrio']['alto']
    ancho_vidrio_sobrante = valores_finales['material_sobrante_vidrio']['ancho']
    valor_sobrante_vidrio = valores_finales['material_sobrante_vidrio']['valor']
    
    print('-------------- Costo de la ventana -----------------')

    print(f'El valor de la ventana es {costo:,}$')
    print(f'El valor de la ventana con ganancia es {(costo * 0.35) + costo:,}$ (35%)')

    print("-------------- Material Utilizado -------------------")
    print(f'El material utilizado de aluminio es {material_utilizado_aluminio} metros. Su valor es de {valor_aluminio_utilizado:,}$')
    print(f'El material utilizado de vidrio es {material_utilizado_vidrio} metros cuadrados. Su valor es de {valor_vidrio_utilizado:,}$')

    print("-------------- Material Sobrante ---------------------")
    print(f'El material sobrante de aluminio es {material_sobrante_aluminio} metros. Su valor es de {valor_sobrante_aluminio:,}$')
    print(f'El material sobrante de vidrio es {material_sobrante_vidrio} metros cuadrados,\ncon un alto de {altura_vidrio_sobrante} mts y un ancho de {ancho_vidrio_sobrante} mts . Su valor es de {valor_sobrante_vidrio:,}$')

m()