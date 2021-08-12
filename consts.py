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