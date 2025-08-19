# -*- coding: utf-8 -*-
import requests
import os
from datetime import datetime
from colorama import Fore, Style, init

os.system("printf '\033]2;₿lockChain v2.0 👨🏽‍💻\a'")

init(autoreset=True)

# Arte ASCII BTC
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

def print_colored_ascii(art):
    for line in art.splitlines():
        colored_line = ""
        for char in line:
            if char == 'x':
                colored_line += Fore.LIGHTYELLOW_EX + char
            elif char in ['M', '0', 'K', 'W']:
                colored_line += Fore.WHITE + char
            else:
                colored_line += Style.RESET_ALL + char
        print(colored_line)
    print(Style.RESET_ALL)

def satoshi_to_btc(satoshi):
    return satoshi / 100000000

def get_btc_info(btc_address):
    url = f"https://blockchain.info/rawaddr/{btc_address}"
    try:
        response = requests.get(url)
        data = response.json()
        
        print(Fore.LIGHTGREEN_EX + f"\n[+] BTC Wallet: {data.get('address')}")
        print(Fore.LIGHTGREEN_EX + f" ├──Total Balance : {satoshi_to_btc(data.get('final_balance'))} BTC")
        print(Fore.LIGHTGREEN_EX + f" ├──Total Transactions : {data.get('n_tx')}")
        print(Fore.LIGHTGREEN_EX + f" ├──Total Received : {satoshi_to_btc(data.get('total_received'))} BTC")
        print(Fore.LIGHTGREEN_EX + f" ├──Total Sent : {satoshi_to_btc(data.get('total_sent'))} BTC")
        
        if 'txs' in data and len(data['txs']) > 0:
            first_tx = data['txs'][-1]  # La primera transacción es la última en la lista
            timestamp = first_tx.get('time')
            date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
            print(Fore.LIGHTGREEN_EX + f" └──First Transaction : {date} (timestamp: {timestamp})")
    
    except Exception as e:
        print(Fore.RED + f"Error: {e}")

if __name__ == "__main__":
    print_colored_ascii(ascii_art)

    # Author
    firma = "By: Hack Underway\n"
    print(Style.BRIGHT + Fore.WHITE + firma.rjust(35) + Style.RESET_ALL)

    btc_address = input(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "Introduce una dirección de ₿itcoin: " + Style.RESET_ALL)
    get_btc_info(btc_address)
    
    print("\n" + " " * 2 + Style.BRIGHT + Fore.RED + "BlockChain OSINT " + Fore.WHITE + Style.BRIGHT + "I like to See You " + Fore.RED + "Happy OSINT" + Style.RESET_ALL + " 🚀\n")
