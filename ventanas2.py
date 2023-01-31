def main():
    n = int(input("¿Cuántas ventanas deseas construir? "))
    i = 0
    while i < n: # Se repite la función n veces
        ventanas()
        i += 1
    print(resultado())

def ventanas():
        precios_aluminio = {"normal": 3334, "blanco": 2000, "negro": 2667}
        precios_vidrio = {"simple": 30000, "doble": 60000, "oscuro": 80000, "laminado": 120000, "blindex": 150000}

        while True:
            tipo_aluminio = input("¿Qué tipo de aluminio desea?")
            tipo_aluminio_precio = precios_aluminio.get(tipo_aluminio, None)
            if tipo_aluminio_precio is not None:
                break
            print("No tenemos ese tipo de aluminio.")

        while True:
            tipo_vidrio = input("¿Qué tipo de vidrio desea?")
            tipo_vidrio_precio = precios_vidrio.get(tipo_vidrio, None)
            if tipo_vidrio_precio is not None:
                break
            print("No tenemos ese tipo de vidrio.")

        while True:
            try:
                ancho = float(input("¿Ancho de la ventana en milímetros?"))
                if ancho > 1800 or ancho < 500:
                    print("El ancho no puede ser mayor a 1800 milímetros ni menor a 500 milímetros")
                    continue
                break
            except ValueError:
                print("Por favor ingrese un número válido para el ancho.")

        while True:
            try:
                alto = float(input("¿Alto de la ventana en milímetros?"))
                if alto > 2500 or alto < 300:
                    print("El alto no puede ser mayor a 2500 milímetros ni menor a 300 milímetros")
                    continue
                break
            except ValueError:
                print("Por favor ingrese un número válido para el alto.")

        ancho_metro = float(ancho / 1000) # Se convierte el ancho a metros
        alto_metro = float(alto / 1000) # Se convierte el alto a metros
        area_ventana = ancho_metro * alto_metro
        perimetro_ventana = (ancho_metro * 2) + (alto_metro * 2)

        valor_vidrio = round((area_ventana * tipo_vidrio_precio)/4.5,2)
        valor_aluminio = round(perimetro_ventana * tipo_aluminio_precio,2)

        # Se calcula el material utilizado
        material_utilizado_aluminio = round(perimetro_ventana, 2)
        material_utilizado_vidrio = round(area_ventana, 2)
        tira_aluminio = 6
        if perimetro_ventana > 6: 
            tira_aluminio = 12
        plancha_vidrio = 4.5

        # Se calcula el valor del material utilizado
        valor_aluminio_utilizado = round(tira_aluminio * tipo_aluminio_precio,2)
        valor_vidrio_utilizado = round(valor_vidrio,2)


        # Se calcula el material sobrante
        material_sobrante_aluminio = round(tira_aluminio - material_utilizado_aluminio, 2)
        material_sobrante_vidrio = round(plancha_vidrio - material_utilizado_vidrio, 2)

        # Se calcula el valor del material sobrante
        valor_sobrante_aluminio = round(material_sobrante_aluminio * tipo_aluminio_precio, 2)
        valor_sobrante_vidrio = round(material_sobrante_vidrio * (tipo_vidrio_precio / 4.5), 2)

        altura_vidrio_sobrante = round(2.5 - alto_metro,2)
        ancho_vidrio_sobrante = round(1.8 - ancho_metro,2)

        print('-------------- Costo de la ventana -----------------')

        print(f'El valor de la ventana es {valor_vidrio + valor_aluminio:,}$')
        print(f'El valor de la ventana con ganancia es {round((valor_vidrio + valor_aluminio) * (0.35) + (valor_vidrio + valor_aluminio),2):,}$ (35%)')

        print("-------------- Material Utilizado -------------------")
        print(f'El material utilizado de aluminio es {material_utilizado_aluminio} metros. Su valor es de {valor_aluminio_utilizado:,}$')
        print(f'El material utilizado de vidrio es {material_utilizado_vidrio} metros cuadrados. Su valor es de {valor_vidrio_utilizado:,}$')

        print("-------------- Material Sobrante ---------------------")
        print(f'El material sobrante de aluminio es {material_sobrante_aluminio} metros. Su valor es de {valor_sobrante_aluminio:,}$')
        print(f'El material sobrante de vidrio es {material_sobrante_vidrio} metros cuadrados,\ncon un alto de {altura_vidrio_sobrante} mts y un ancho de {ancho_vidrio_sobrante} mts . Su valor es de {valor_sobrante_vidrio:,}$')

def resultado():
    #recoger datos de ventanas()

    #calcular el total de ventanas

    #imprimir el total de ventanas

main()