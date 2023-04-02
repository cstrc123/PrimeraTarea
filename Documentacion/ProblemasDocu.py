# PROBLEMA 1:   Se necesita crear un programa que reciba del usuario una frase y decida si esa
# frase es un palíndromo o no. Un palíndromo se puede leer de igual forma de
# izquierda a derecha, que de derecha a izquierda. Ejemplo: "Anita lava la tina".

# Documentación:
# Pedirle al usuario una frase
# Ver si la frase cumple con la función de leerse de igual manera de derecha, izquierda, izquierda, derecha
# Hacer un plan de seguimiento a cada palabra para comprobar que es un palíndromo
# Si es palíndromo, imprimir: "La frase ----- se lee de la misma manera al revés"
# Si no es palíndromo, imprimir: "La frase ------ no se lee de la misma manera al revés"
# Se podría pedir de nuevo al usuario que digite una nueva frase
# Imprimir una frase para finalizar el programa como "Fin del programa"


# PROBLEMA 2: Un servidor crea logs por cada acción que se realiza en él. El administrador desea
# un programa que todos los días borre todos los logs excepto si el log contiene la
# palabra "error"; si contiene esta palabra, se debe copiar el log al directorio "Errores"
# y se debe enviar un correo al administrador.

# Docuemntación:
# Preguntarle al administrador cuál es log que él desea que no se borre
# Averiguar cuantos logs crea el servidor 
# Sabiendo cuantos logs crea el servidor, hay que empezar a hacer un programa que sepa identificar cada log
# Identificando los logs, el programa sabrá cuando parar en caso de que aparezca la palabra "Error"
# El programa debe hacer un canal hacia el directorio para poder mandar cada log que contenga la palabra "Error"
# El programa debe estar hecho para trabajar automáticamente
# Se hará un correo automático repetitivo si sólo y cuando el directorio reciba un log de "Error" 
# Correo llegará al administrador diciendo "NUEVO ERROR LOCALIZADO" 


# PROBLEMA 3: Cree una solución que permita al usuario ingresar un número entero. Dado dicho
# número, el programa debe determinar si los dígitos de este número se pueden
# ordenar de forma tal que el resultado sea un múltiplo de 5.

# Documentación:
# Pedirle al usuario un número entero
# Si el número es de 1 dígito
# Contar desde -1 o 1 hasta el número que se digitó 
# Por cada número revisar si es multiplo de 5
# El número digitado sí es multiplo de 5 
# Imprimir una frase que le haga saber al usuario que su número si se puede multiplicar por 5
# El número digitado no es multiplo de 5
# Imprimir una frase que le haga saber al usuario que su número no se puede multiplicar por 5
# Si el número que digitó el usuario es de 2 dígitos
# Hacer un programa que verifique cual es el primer dígito, esto empezando desde -1 o 1
# Hacer un programa que verifique cual es el segundo dígito, esto empezando desde -1 o 1
# El programa debe saber si se pueden ordenar para formar un número múltiplo de 5
# Se puede formar un número múltiplo de 5
# Imprimir una frase que le haga saber al usuario que su número cambió para que fuera múltiplo de 5
# No se puede formar un número que sea múltiplo de 5
# Imprimir una frase que le haga saber al usuario que su número no puede ser multiplicado por 5
# Imprimir un final para el programa o decidir si pedir un número diferente al usuario
