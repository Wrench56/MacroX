import rich
import colorama

colorama.init()

def error(message):
    print(f'[{colorama.Fore.RED}ERRO{colorama.Style.RESET_ALL}]   {message}')

def info(message):
    print(f'[{colorama.Fore.BLUE}INFO{colorama.Style.RESET_ALL}]   {message}')

def warning(message):
    print(f'[{colorama.Fore.YELLOW}WARN{colorama.Style.RESET_ALL}]   {message}')

