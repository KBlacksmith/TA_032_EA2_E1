from random import randrange

nombres = ["kenneth martin rodriguez garcia", "maria fernanda guerra reyes", "roberto tadeo cuellar gracia", "alejandra marisol cantu ruiz"]
matriculas = ["1916780", "1927750", "1732780", "1596437"]
error = {1: 'La cadena no inicia con los dígitos de la matrícula', 2: 'La cadena no contiene las iniciales de los apellidos',
3: 'La cadena no contiene los dígitos de la \nmatrícula después de las iniciales de los apellidos', 
4: 'La cadena no contiene las iniciales invertidas 2n veces',
5: 'La cadena no contiene el primer nombre después de las \niniciales invertidas',
6: 'La cadena no contiene el primer nombre por segunda vez',
7: 'La cadena contiene caracteres sobrantes'}
class Automata(): 
    def __init__(self) -> None:
        num = randrange(0, len(nombres))
        self.n = 0
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
        return 'Cadena inválida\n\nError #001: {}'.format(error[1])

    def validar1(self, cadena: str)->str: 
        if cadena.startswith(self.iniciales): 
            self.n=1
            return self.validar2(cadena[len(self.iniciales):])
        return 'Cadena inválida\n\nError #002: {}'.format(error[2])

    def validar2(self, cadena: str, n=1)->str: 
        if cadena.startswith(self.iniciales): 
            self.n += 1
            return self.validar2(cadena[len(self.iniciales):])
        elif cadena.startswith(self.matricula): 
            self.n *= 2 
            return self.validar3(cadena[len(self.matricula):])
        return 'Cadena inválida\n\nError #003: {}'.format(error[3])

    def validar3(self, cadena: str)->str: 
        if self.n>0: 
            if cadena.startswith(self.iniciales_inv): 
                self.n -= 1
                return self.validar3(cadena[len(self.iniciales_inv):])
            return 'Cadena inválida\n\nError #004: {}'.format(error[4])
        return self.validar4(cadena)

    def validar4(self, cadena: str)->str:
        if cadena.startswith(self.primer_nombre): 
            return self.validar5(cadena[len(self.primer_nombre):])
        elif cadena.startswith(self.iniciales_inv): 
            return 'Cadena inválida\n\nError #004: {}'.format(error[4])
        return 'Cadena inválida\n\nError #005: {}'.format(error[5])

    def validar5(self, cadena: str)->str: 
        if cadena.startswith(self.primer_nombre): 
            return self.validar6(cadena[len(self.primer_nombre):])
        return 'Cadena inválida\n\nError #006: {}'.format(error[6])

    def validar6(self, cadena: str)->str: 
        if cadena=='': 
            return 'Cadena válida\n\n'
        return 'Cadena inválida\n\nError #007: {}'.format(error[7])
        
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
        print("\nIndicaciones: Ingrese una cadena con la siguiente estructura")
        print("i(w^n)i((w')^2n)j^2, tal que: ")
        print("w = las iniciales de los apellidos, i = todos los dígitos\nde la matrícula, w' = w inversa, j = el primer nombre,\nn>=1, n no debe leerse")
        print('Nota: Todas las letras deben ser minúscula')
        print(f'Nombre: {miAutomata.nombre}')
        print(f'Matricula: {miAutomata.matricula}')
        cadena=input('Ingresar cadena: ')
        print(miAutomata.validar0(cadena))
        sn = validar_sn()