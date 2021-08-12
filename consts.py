#Andree Toledo 18439
#PROYECTO 1 REDES 2021

#Print class Colors retrieved from:
#https://www.edureka.co/community/99631/how-to-print-colored-text-in-python

HEADER = '\033[95m'
OKBLUE = '\033[94m' + 'OK: '
OKGREEN = '\033[92m' + 'OK: '
WARNING = '\033[93m' + 'WARNING: '
FAIL = '\033[91m' + 'FAIL: '
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
BLUE = '\033[94m'
RED = '\033[91m'
YELLOW = '\033[93m'

# Menu messages
login_menu = f"""
{HEADER}|~~~~~~~~~~~~~~~~~| MENU DE INICIO |~~~~~~~~~~~~~~~~~|{ENDC}
Elija el numero de la opcion que desea.
1: Registar nueva cuenta
2: Iniciar sesion en una cuenta existente
3: Salir
{HEADER}|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|{ENDC}
"""

main_menu = f"""
{HEADER}|~~~~~~~~~~~~~~~~~| MENU PRINCIPAL |~~~~~~~~~~~~~~~~~|{ENDC}
Elija el numero de la opcion que desea.
1: Mostrar todos los usuarios conectados y mi lista de contactos
2: Agregar un usuario a mi lista de contactos
3: Mostrar detalles de usuario
4: Chat privado
5: Chat grupal
6: Mensaje de presencia
7: Enviar archivo
8: Cerrar sesión
9: Eliminar mi cuenta
{HEADER}|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|{ENDC}
"""

roup_options = f"""
\tSeleccione una de las siguientes opciones:
\t1: Crea un chat grupal
\t2: Unirse a un chat grupal
\t3: Enviar mensaje al grupo
\t4: Salir de un chat grupal
\t5: Cancelar
"""

show_options = f"""
\tSeleccione una de las siguientes opciones:
\t1. chat
\t2. Ausente
\t3. Largo tiempo ausente 
\t4. No molestar
"""
#3. XA
#4. DND

# Errors messages
error_msg = f"""
{FAIL}Algo ha salido mal...{ENDC}
"""
invalid_option = f'{FAIL}porfavor, ingrese una opcion valida!{ENDC}'

chat_session = f"""
||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|           ESTAS EN UNA SESIÓN DE CHAT PRIVADA        |
||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Escribe {BOLD}exit{ENDC} para salir de la sesion de chat.
"""

# Userful variables
show_array = ['chat', 'away', 'xa', 'dnd']

# NOTIFICATIONS:
NEW_MESSAGE = '''
|~~~~~~~~~~~~~~> MENSAJE NUEVO <~~~~~~~~~~~~~~|
'''

FILE_OFFER = '''
<~~~~~~~~~~~~~~| ARCHIVO OFRECIDO |~~~~~~~~~~~~~~>
'''

SUSCRIPTION = '''
|~~~~~~~~~~~~~~| SUSCRIPCION |~~~~~~~~~~~~~~|
'''

GOT_ONLINE = '''
|~~~~~~~~~~~~~~> EN LINEA <~~~~~~~~~~~~~~|
'''

GROUPCHAT = '''
|~~~~~~~~~~~~~~>  CHAT GRUPAL <~~~~~~~~~~~~~~|
'''

STREAM_TRANSFER = '''
|~~~~~~~~~~~~~~> TRANSMISION INICIADA <~~~~~~~~~~~~~~|
         Transferencia de archivo iniciada!

Porfavor espere...
'''
