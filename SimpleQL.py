import json
import re
import webbrowser

while True:
    print()
    print("Ingrese un Comando:")
    aux = input()

    F1 = re.compile(r'( |)cargar ( |)\b', re.I)
    F2 = re.compile(r'( |)seleccionar ( |)\b', re.I)
    F3 = re.compile(r'( |)maximo ( |)', re.I)
    F4 = re.compile(r'( |)minimo ( |)', re.I)
    F5 = re.compile(r'( |)suma ( |)', re.I)
    F6 = re.compile(r'( |)reportar ( |)', re.I)

    aux2 = re.compile(r'( |),( |)\b')
    aux3 = re.compile(r'(| )donde(| )\b', re.I)
    aux4 = re.compile(r'( |)=( |)')
    aux5 = re.compile(r'( |)"( |)')

    com1 = re.compile(r"(\w+)")
    s = com1.search(aux)

    if (s.group(1).lower()) == 'cargar':
        del1 = F1.sub("", aux)
        del2 = aux2.sub(" ", del1)
        print()
        Narchivo = del2.split()

        for n in Narchivo:
            print("se cargo el " + '"'+n+'"' + " con exito.")

    elif "seleccionar *" in aux.lower():
        del3 = F2.sub("", aux)
        print()
        del4 = aux2.sub(" ", del3)
        registroAux = del4.lower().split()

        if "donde" in registroAux:
            del5 = aux3.sub(" ", del4)
            del6 = aux4.sub(":", del5)
            del7 = aux5.sub("", del6)
            registroCod = del7.split()
            cond = str(registroCod[-1]).lower()

            for n in Narchivo:
                with open(n) as file:
                    data = json.load(file)
                    for i in data:
                        a = 'Nombre:'+ i['nombre']
                        b = 'Edad:' + str(i['edad'])
                        c = 'Activo:'+ str(i['activo'])
                        d = 'Promedio:'+ str(i['promedio'])
                        arrayVer2 = [a.lower(), b.lower(), c.lower(), d.lower()]
                        arrayVer = [a, b, c, d]

                        if cond in arrayVer2:
                            print(arrayVer[0])
                            print(arrayVer[1])
                            print(arrayVer[2])
                            print(arrayVer[3])
                            print()
                file.close()

        else:
            for n in Narchivo:
                with open(n) as file:
                    data = json.load(file)
                    for i in data:
                        print('Nombre:', i['nombre'])
                        print('Edad:', i['edad'])
                        print('Activo:', i['activo'])
                        print('Promedio:', i['promedio'])
                        print()
                file.close()

    elif (s.group(1).lower()) == 'seleccionar':
        del3 = F2.sub("", aux)
        print()
        del4 = aux2.sub(" ", del3)
        registroAux = del4.lower().split()

        if "donde" in registroAux:
            del5 = aux3.sub(" ", del4)
            del6 = aux4.sub(":", del5)
            del7 = aux5.sub("", del6)
            registroCod = del7.split()

            cond = str(registroCod[-1]).lower()

            for n in Narchivo:
                with open(n) as file:
                    data = json.load(file)
                    for i in data:
                        a = 'Nombre:'+ i['nombre']
                        b = 'Edad:' + str(i['edad'])
                        c = 'Activo:'+ str(i['activo'])
                        d = 'Promedio:'+ str(i['promedio'])
                        arrayVer2 = [a.lower(), b.lower(), c.lower(), d.lower()]
                        arrayVer = [a, b, c, d]

                        if cond in arrayVer2:
                            if 'nombre' in registroCod:
                                print(arrayVer[0])
                            if 'edad' in registroCod:
                                print(arrayVer[1])
                            if 'activo' in registroCod:
                                print(arrayVer[2])
                            if 'promedio' in registroCod:
                                print(arrayVer[3])
                            print()
                file.close()

        else:
            for n in Narchivo:
                with open(n) as file:
                    data = json.load(file)
                    for i in data:
                        a = 'Nombre:'+ i['nombre']
                        b = 'Edad:' + str(i['edad'])
                        c = 'Activo:'+ str(i['activo'])
                        d = 'Promedio:'+ str(i['promedio'])
                        arrayVer = [a, b, c, d]

                        if 'nombre' in registroCod:
                            print(arrayVer[0])
                        if 'edad' in registroCod:
                            print(arrayVer[1])
                        if 'activo' in registroCod:
                            print(arrayVer[2])
                        if 'promedio' in registroCod:
                            print(arrayVer[3])
                        print()

    elif (s.group(1).lower()) == 'maximo':
        del8 = F3.sub("", aux)
        print()
        registroAux = del8.lower().split()

        arrayMax = []

        for n in Narchivo:
            with open(n) as file:
                data = json.load(file)
                for i in data:
                    b = i['edad']
                    d = i['promedio']
                    arrayVer = [b, d]
                    if 'edad' in registroAux:
                        arrayMax.append(arrayVer[0])
                    if 'promedio' in registroAux:
                        arrayMax.append(arrayVer[1])
                file.close()
        print("El " + registroAux[0] + " maximo en el registro es de " + str(max(arrayMax)))


    elif (s.group(1).lower()) == 'minimo':
        del9 = F4.sub("", aux)
        print()
        registroAux = del9.lower().split()

        arrayMin = []


        for n in Narchivo:
            with open(n) as file:
                data = json.load(file)
                for i in data:
                    b = i['edad']
                    d = i['promedio']
                    arrayVer = [b, d]
                    if 'edad' in registroAux:
                        arrayMin.append(arrayVer[0])
                    if 'promedio' in registroAux:
                        arrayMin.append(arrayVer[1])
                file.close()
        print("El " + registroAux[0] + " minimo en el registro es de " + str(min(arrayMin)))


    elif (s.group(1).lower()) == 'suma':
        del10 = F5.sub("", aux)
        print()
        registroAux = del10.lower().split()

        arraySuma = []
        for n in Narchivo:
            with open(n) as file:
                data = json.load(file)
                for i in data:
                    b = i['edad']
                    d = i['promedio']
                    arrayVer = [b, d]
                    if 'edad' in registroAux:
                        arraySuma.append(arrayVer[0])
                    if 'promedio' in registroAux:
                        arraySuma.append(arrayVer[1])
                file.close()
        print("La suma de " + registroAux[0] + " en el registro es de " + str(sum(arraySuma)))


    elif "cuenta" in aux.lower():
        print()
        x = 0
        for n in Narchivo:
            with open(n) as file:
                data = json.load(file)
                for i in data:
                    x = x + 1
                file.close()
        print("El numero registro es de que se han cargado a memoria es de " + str(x))


    elif (s.group(1).lower()) == 'reportar':
        del11 = F6.sub("", aux)
        registroAux = del11.lower().split()
        print()
        Nregistro = int(registroAux[0])
        x = 0
        for n in Narchivo:
            with open(n) as file:
                data = json.load(file)
                for i in data:
                    x = x + 1
        if (Nregistro <= x):
            web = open('Reportar.html', 'w')
            x=1
            mensaje = """
            <!DOCTYPE html>
            <html lang="es">
            <head>
                <meta charset="utf-8" />
                <meta name="author" content="Julio Enrique Wu Chiu" />
                <title>REPORTAR</title>
            <style>
                body{background-color:black}
                body{font-family: 'Comic Sans MS'; color:aliceblue; padding:80px}
                table{border-collapse:collapse}
                th {border: 2px chocolate solid; margin:auto; color:lawngreen}
                td {border: 2px chocolate solid; padding:10px; width:200px; margin:auto; text-align:center}
            </style>
            </head>
            <body>
            <center>
                <table class="registro">
                    <thead style="background-color:">
                        <tr>
                            <th colspan="5"><h1>REPORTAR </h1></th>
                        </tr>
                        <tr>
                            <td><h2>REGISTRO</h2></td>
                            <td><h2>NOMBRE</h2></td>
                            <td><h2>EDAD</h2></td>
                            <td><h2>ACTIVO</h2></td>
                            <td><h2>PROMEDIO</h2></td>
                        </tr>
                    </thead>
                    <tbody>"""
            web.write(mensaje)
            for n in Narchivo:
                with open(n) as file:
                    data = json.load(file)
                    for i in data:
                        a = i['nombre']
                        b = i['edad']
                        c = i['activo']
                        d = i['promedio']
                        arrayVer = [a, b, c, d]
                        if x <= Nregistro:
                            texto = "<tr> <td>"+str(x)+"</td><td>"+str(a)+"</td><td>"+str(b)+"</td><td>"+str(c)+"</td><td>"+str(d)+"</td></tr>"
                            x += 1
                            web.write(texto)
                    file.close()
            mensaje2 ="""
                    </tbody>
                </table>
            </center>
            </body>
            </html>
            """
            web.write(mensaje2)
            web.close()

            webbrowser.open_new_tab('Reportar.html')

        else:
            print("ERROR: La cantidad al reportar es mayor a la cantidad de registro cargardo al memoria")


    else:
        print("Error de sintaxis")




