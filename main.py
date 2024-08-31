import os
import requests
import threading
import concurrent.futures
import time
import socket
import socks
from datetime import datetime
from colorama import Fore, Style
from pystyle import Write, System, Colors

# KETTİP ASCII Art
ascii_art = """

 _        _______ ___________________________ _______ 
| \    /\(  ____ \\__   __/\__   __/\__   __/(  ____ ) 
|  \  / /| (    \/   ) (      ) (      ) (   | (    )|
|  (_/ / | (__       | |      | |      | |   | (____)|
|   _ (  |  __)      | |      | |      | |   |  _____)
|  ( \ \ | (         | |      | |      | |   | (      
|  /  \ \| (____/\   | |      | |   ___) (___| )      
|_/    \/(_______/   )_(      )_(   \_______/|/       

Kettip Scripts Tools

 NOT: Miktar belirlemeyi ayarlamayı unuttum 99  99 99 girebilirsiniz                        
"""
