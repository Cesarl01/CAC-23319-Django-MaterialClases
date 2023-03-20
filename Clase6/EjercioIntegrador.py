from abc import ABC, abstractmethod

"""7.- Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una 
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es 
opcional. Crear los siguientes métodos para la clase:
• Un constructor, donde los datos pueden estar vacíos.
• Los setters y getters para cada uno de los atributos. El atributo no se puede modificar 
directamente, sólo ingresando o retirando dinero.
• mostrar(): Muestra los datos de la cuenta.
• ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es 
negativa, no se hará nada.
• retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números 
rojos"""

#Persona: Titular o persona responsable de los datos
class Persona(ABC):
    def __init__(self, nombre ="", edad =0, dni =0):
        self.__nombre = nombre
        self.__edad = edad    
        self.__dni = dni
    #print("estoy en la linea 16")
    def __str__(self) -> str:
        return f'{self.nombre, self.edad, self.dni}'

    #GETTER
    @property
    def nombre(self):
        return self.__nombre
    @property
    def edad(self):
        return self.__edad
    @property
    def dni(self):
        return self.__dni

    #SETTER
    @nombre.setter
    def nombre(self,nuevo_nombre):
        self.__nombre = nuevo_nombre

    @edad.setter
    def edad(self,edad_nueva):
        self.__edad=edad_nueva

    @dni.setter
    def dni(self,dni_nuevo):
        self.__dni=dni_nuevo

    @abstractmethod
    def registrarse(self):
        pass

class registro_personal(Persona):
    def __init__(self, nombre="", edad=0, dni=0):
        super().__init__(nombre, edad, dni)

    def registrarse(self):
        print("registro registro_personal exitoso")       
               
#mostrar: Registra y Muestra los datos de la cuenta de Persona(Titular)
class mostrar(Persona):    
    def __init__(self, nombre="", edad=0, dni=0, cuenta=0):
        super().__init__(nombre, edad, dni) 
        self.cuenta = cuenta
        #show_persona = Persona
    def registrarse(self):
        print("registro exitoso")           
    def __str__(self) -> str:
        return f'{self.cuenta}'
#ingreso: Ingreso de cantidad a la cuenta
class ingreso(Persona):
    def __init__(self, nombre="", edad=0, dni=0, cantidad= 0.0):
        super().__init__(nombre, edad, dni)
        self.cantidad = cantidad
        if cantidad > 0:
            self.registrarse()
            print("Registro de cantidad correcto")
        else:
            print("la cantidad negativa no se registro")            

    def registrarse(self):
        return super().registrarse()  
    def __str__(self) -> str:
        return f'{self.cantidad}'          

#retiro: Retiro de cantidad de la cuenta
class retiro(Persona):
    def __init__(self, nombre="", edad=0, dni=0, cantidad=0.0):
        super().__init__(nombre, edad, dni)
        self.cantidad = cantidad
        if self.cantidad > 0:
            self.registrarse()
            print("operación realizada correctamente")

    def registrarse(self):
        return super().registrarse()

    def __str__(self) -> str:
        return f'{self.cantidad}'  


"""8.- Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase 
CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase, 
además del titular y la cantidad se debe guardar una bonificación que estará expresada en 
tanto por ciento. Crear los siguientes métodos para la clase:
• Un constructor.
• Los setters y getters para el nuevo atributo.
• En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo 
tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es 
mayor de edad pero menor de 25 años y falso en caso contrario.
• Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
• El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la 
cuenta."""

#Persona: Titular o persona responsable de los datos

class CuentaJoven(Persona):
    def __init__(self, nombre="", edad=0, dni=0, boninficacion = 0.0):
        super().__init__(nombre, edad, dni)
    #print("estoy en la linea 133")
        self.__bonificacion = boninficacion
        self.edad = edad
        print("edad",self.edad)
        self.es_titular_valido()    

    def __str__(self) -> str:
        return f'{self.bonificacion}'
    #GETTER
    @property
    def bonificacion(self):
        return self.__bonificacion

    #SETTER
    @bonificacion.setter
    def bonificacion(self,bonificacion_nueva):
        self.__bonificacion = bonificacion_nueva

    def es_titular_valido(self):
        if self.edad >= 18 and self.edad < 25:
            self.registrarse()            
            return True
        else:
            return False
        
    def registrarse(self):
        print("Bonificacion realizada correctamente")
        return super().registrarse()
        
##############  EJECUCIÓN DEL CODIGO

bSalir = False
new_registro_persona= registro_personal("Cesar Machado", 29 ,"95548506")
new_registro_persona.registrarse()
show_Reg = mostrar("",0,0,10738200003844)
show_Reg.registrarse()
print(new_registro_persona)
print(show_Reg)
oper = input("ingrese una operacion, I: para ingreso o R: para retiro  ")

if oper == "i" or oper == "I":
    cant = float(input("indique la cantidad a ingresar  "))
    operacion = ingreso("",0,0,cant)
elif oper == "r" or oper == "R":
    cant = float(input("indique la cantidad a retirar  "))
    operacion = retiro("",0,0,cant)
elif oper not in ("r","R","i","I"):
    bSalir = True
    exit
if not bSalir:
    print(operacion)

titular_de_cuenta = CuentaJoven("",new_registro_persona.edad,0,25)
print(titular_de_cuenta)