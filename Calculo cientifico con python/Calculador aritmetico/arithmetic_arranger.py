import re
def arithmetic_arranger(problems, result = False):
    operandos1 = list()
    operandos2 = list()
    operadores = list()
    # Validaciones
    # Validacion de cantidad de problemas
    if len(problems) > 5:
        return "Error: Too many problems."
    for problem in problems:
        # Validacion de operadores
        operador = re.search("[+-]",problem)
        if(operador is None):
            return "Error: Operator must be '+' or '-'."
        else:
            op = re.compile("[+-]")
            operadores.append(op.findall(problem)[0])
        index = 0
        for element in problem.split():
            if((re.search("[+-]",element) is None)):
                # Validacion de si son numeros
                number = re.search("^[0-9]+$",element)
                if(number is None):
                    return "Error: Numbers must only contain digits."
                else:
                    # Validacion de si tiene la longitud correcta
                    if(len(element) > 4):
                        return "Error: Numbers cannot be more than four digits."
                oper = re.compile("^[0-9]+$")
                if(index == 0):
                    operandos1.append(oper.findall(element)[0])
                else:
                    operandos2.append(oper.findall(element)[0])
                index += 1

    # Resolucion de problemas
    index = 0
    linea1 = ""
    linea2 = ""
    lineaGuiones = ""
    lineaResultado = ""

    while(index < len(problems)):
        guiones = "-"
        op1 = int(operandos1[index])
        op2 = int(operandos2[index])
        op = operadores[index]

        res = 0
        if(op == "+"):
            res = op1 + op2
        else:
            res = op1 - op2
        
        num1 = operandos1[index]
        num2 = operandos2[index]

        op = op.ljust(len(operadores[index])+1)
        if(len(num1) > len(num2)):
            while(len(num1) != len(num2)):
                num2 = num2.rjust(len(num2)+1)
        while(len(num1) != (len(num2)+len(op))):
            num1 = num1.rjust(len(num1)+1)
        
        while(len(guiones) != (len(num2)+len(op))):
            guiones = guiones.replace(guiones, "-"+ guiones)
        
        res = str(res)
        res = res.rjust(len(num2)+len(op))
            
        linea1 = linea1.replace(linea1,linea1 + num1)
        linea2 = linea2.replace(linea2,linea2 + op + num2)
        lineaGuiones = lineaGuiones.replace(lineaGuiones, lineaGuiones + guiones)
        lineaResultado = lineaResultado.replace(lineaResultado, lineaResultado + res)
        
        index += 1
        if(index < len(problems)):
            linea1 = linea1.ljust(len(linea1)+4)
            linea2 = linea2.ljust(len(linea2)+4)
            lineaGuiones = lineaGuiones.ljust(len(lineaGuiones)+4)
            lineaResultado = lineaResultado.ljust(len(lineaResultado)+4)


    linea1 = linea1.replace(linea1,linea1 + '\n' )
    linea2 = linea2.replace(linea2,linea2 + '\n' )
        
    if(result == True):
        lineaGuiones = lineaGuiones.replace(lineaGuiones, lineaGuiones + '\n' )
        cadResultado = linea1 + linea2 + lineaGuiones + lineaResultado
    else:
        cadResultado = linea1 + linea2 + lineaGuiones
    
    return cadResultado