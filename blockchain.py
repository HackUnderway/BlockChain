# -*- coding: utf-8 -*-
import requests
from colorama import Fore, Style, init
import pyfiglet

#banner = pyfiglet.figlet_format("Bitcoin")
#print(banner)

# Inicializar colorama
init(autoreset=True)

# Arte ASCII
ascii_art = '''
                   .,:ldxxxxdl:,.                   
              .':oxxxxxxxxxxxxxxxxo:,.              
           'cdxxxxxxxxxxxxxxxxxxxxxxxxxc'           
        .cxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxc.        
      .lxxxxxxxxxxxxxxxxxkxxxxxxxxxxxxxxxxxxl.      
     cxxxxxxxxxxxxxxxxxx0MMKxxK0Oxxxxxxxxxxxxxc     
   .dxxxxxxxxxxxxkK0OkkxWMMkxKMMXxxxxxxxxxxxxxxd.   
  .xxxxxxxxxxxxxxKMMMMMMMMWK0WMMkxxxxxxxxxxxxxxxx.  
 .xxxxxxxxxxxxxxxxxkXMMMMMMMMMMMNX0kxxxxxxxxxxxxxx. 
 dxxxxxxxxxxxxxxxxxxXMMMMXkO0KNMMMMMXxxxxxxxxxxxxxd 
.xxxxxxxxxxxxxxxxxxkMMMMMkxxxxxOMMMMMKxxxxxxxxxxxxx'
lxxxxxxxxxxxxxxxxxxXMMMMNkxxxxkKMMMMM0xxxxxxxxxxxxxo
xxxxxxxxxxxxxxxxxxOMMMMMMMMWWWMMMMMW0xxxxxxxxxxxxxxx
dxxxxxxxxxxxxxxxxxNMMMMXO0KXNMMMMMNOxxxxxxxxxxxxxxxd
;xxxxxxxxxxxxxxxxOMMMMMkxxxxxkKMMMMMKxxxxxxxxxxxxxx;
 xxxxxxxxxxxxONXXWMMMMKxxxxxxxkMMMMMWxxxxxxxxxxxxxx 
 ;xxxxxxxxxxkNMMMMMMMMWXXK00KXWMMMMMKxxxxxxxxxxxxx: 
  lxxxxxxxxxxxxkO0WMMWMMMMMMMMMMMMWKxxxxxxxxxxxxxo  
   lxxxxxxxxxxxxxkMMWxxNMMKKKXXKKOxxxxxxxxxxxxxxo   
    ,xxxxxxxxxxxxKWM0xOMMWxxxxxxxxxxxxxxxxxxxxx,    
      dxxxxxxxxxxxxxxxOKXOxxxxxxxxxxxxxxxxxxxx      
        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx        
          ;xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx:          
             .xxxxxxxxxxxxxxxxxxxxxxxx.             
                   xxxxxxxxxxxxxx.                  
                         lo               
'''

# Función para colorear el arte ASCII
def print_colored_ascii(art):
    for line in art.splitlines():
        colored_line = ""
        for char in line:
            if char == 'x':
                # Naranja para las 'x'
                colored_line += Fore.LIGHTYELLOW_EX + char
            elif char in ['M', '0', 'K', 'W']:
                # Blanco para las letras y números
                colored_line += Fore.WHITE + char
            else:
                # Default sin color
                colored_line += Style.RESET_ALL + char
        print(colored_line)
    # Reset the color after finishing
    print(Style.RESET_ALL)

# Imprimir el arte coloreado
print_colored_ascii(ascii_art)


# Función para obtener información de una dirección de ₿itcoin
def get_btc_info(btc_address):
    # Usa el servicio de blockchain.info para obtener información sobre la dirección
    url = f"https://blockchain.info/rawaddr/{btc_address}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        print(Fore.LIGHTGREEN_EX + f"Dirección BTC: {data.get('address', 'No disponible')}")
        print(Fore.LIGHTGREEN_EX + f"Transacciones totales: {data.get('n_tx', 'No disponible')}")
        print(Fore.LIGHTGREEN_EX + f"Cantidad total recibida (en satoshis): {data.get('total_received', 'No disponible')}")
        print(Fore.LIGHTGREEN_EX + f"Cantidad total enviada (en satoshis): {data.get('total_sent', 'No disponible')}")
        print(Fore.LIGHTGREEN_EX + f"Balance actual (en satoshis): {data.get('final_balance', 'No disponible')}")
    
    except Exception as e:
        print(Fore.RED + f"Error obteniendo información de la dirección BTC: {e}")

if __name__ == "__main__":
    btc_address = input(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "Introduce una dirección de ₿itcoin: " + Style.RESET_ALL)
    get_btc_info(btc_address)

# Texto con negrita y color rojo usando colorama
print("\n\n\t" + Style.BRIGHT + "BlockChain OSINT " + Fore.RED + "I like to See You, Happy OSINT " + Style.RESET_ALL + "😃\n\n")
