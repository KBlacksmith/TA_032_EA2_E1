from random import randrange

nombres = ["kenneth martin rodriguez garcia", "maria fernanda guerra reyes", "roberto tadeo cuellar gracia", "alejandra marisol cantu ruiz"]
matriculas = ["1916780", "1927750", "1732780", "1596437"]

class Automata(): 
    def __init__(self) -> None:
        num = randrange(0, len(nombres))
        self.nombre= nombres[num]
        self.nombres = self.nombre.split(' ')
        self.iniciales= self.nombres[-2][0]+self.nombres[-1][0]
        self.iniciales_inv = self.nombres[-1][0]+self.nombres[-2][0]
        self.matricula=matriculas[num]
        self.primer_nombre = self.nombres[0]
        self.font = ('bold', 15)
    def validar0(self, cadena: str)->str: 
        if cadena.startswith(self.matricula): 
            return self.validar1(cadena[len(self.matricula):])
        return 'Cadena inválida\n\nError #001: La cadena no inicia con los dígitos de la matrícula\n'
    def validar1(self, cadena: str)->str: 
        if cadena.startswith(self.iniciales): 
            return self.validar2(cadena[len(self.iniciales):])
        return 'Cadena inválida\n\nError #002: La cadena no contiene las iniciales de los apellidos\n'
    def validar2(self, cadena: str)->str: 
        if cadena.startswith(self.iniciales): 
            return self.validar2(cadena[len(self.iniciales):])
        elif cadena.startswith(self.matricula): 
            return self.validar3(cadena[len(self.matricula):])
        return 'Cadena inválida\n\nError #003: La cadena no contiene los dígitos de la \nmatrícula después de las iniciales de los apellidos\n'
    def validar3(self, cadena: str)->str: 
        if cadena.startswith(self.iniciales_inv): 
            return self.validar4(cadena[len(self.iniciales_inv):])
        return 'Cadena inválida\n\nError #004: La cadena no contiene las iniciales \ninvertidas de los apellidos\n'
    def validar4(self, cadena: str)->str: 
        if cadena.startswith(self.iniciales_inv): 
            return self.validar5(cadena[len(self.iniciales_inv):])
        return 'Cadena inválida\n\nError #005: La cadena no tiene una cantidad par de las iniciales invertidas \nde los apellidos\n'
    def validar5(self, cadena: str)->str: 
        if cadena.startswith(self.iniciales_inv): 
            return self.validar4(cadena[len(self.iniciales_inv):])
        elif cadena.startswith(self.primer_nombre): 
            return self.validar6(cadena[len(self.primer_nombre):])
        return 'Cadena inválida\n\nError #006: La cadena no contiene el primer nombre después de las \niniciales invertidas\n'
    def validar6(self, cadena: str)->str: 
        if cadena.startswith(self.primer_nombre): 
            return self.validar7(cadena[len(self.primer_nombre):])
        return 'Cadena inválida\n\nError #007: La cadena no contiene el primer nombre por segunda vez\n'
    def validar7(self, cadena: str)->str: 
        if cadena=='': 
            return 'Cadena válida\n\n'
        return 'Cadena inválida\n\nError #008: La cadena contiene caracteres sobrantes\n'
def validar_sn():
    sn = input('¿Desea validar otra cadena?\nS--Sí\nN--No\n').lower()
    while  sn!='s' and sn !='n': 
        sn = input('Caracter inválido, ingrese s/n: ')
    return sn
if __name__=="__main__":
    sn='s'
    cadena=''
    resultado = (False, '')
    miAutomata = Automata()
    while sn=='s': 
        print(f'Nombre: {miAutomata.nombre}')
        print(f'Matricula: {miAutomata.matricula}')
        print('Reglas: i(w^n)i(w^-1)^2n j^2')
        cadena=input('Ingrese una cadena para validación: ')
        resultado=miAutomata.validar0(cadena)
        if resultado[0]:
            print('Cadena válida\n\n\n')
            pass
        else: 
            print('Error: '+resultado[1])
            pass
        sn = validar_sn()