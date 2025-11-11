    
from autenticacion_usuario.autenticacion import Autenticacion 


sistema = Autenticacion()

sistema.Registrar("vicente", "1234")
sistema.Registrar("ana", "abcd")
sistema.Registrar("vicente", "otra_clave")   


sistema.usuario_registrado("vicente")
sistema.usuario_registrado("juan")


sistema.login("vicente", "1234")    
sistema.login("vicente", "9999")     
sistema.login("juan", "cualquier") 