import socket
from threading import Thread
from queue import Queue

# Define colors
red = '\033[91m'
gr = '\033[92m'
cyan = '\033[96m'
yellow = '\033[93m'
white = '\033[97m'
res = '\033[0m'

print(f"""
{gr}  _____                        _         _          _____ _____  
 |  __ \                      (_)       | |        |_   _|  __ \ 
 | |  | | ___  _ __ ___   __ _ _ _ __   | |_ ___     | | | |__) |
 | |  | |/ _ \| '_ ` _ \ / _` | | '_ \  | __/ _ \    | | |  ___/ 
 | |__| | (_) | | | | | | (_| | | | | | | || (_) |  _| |_| |     
 |_____/ \___/|_| |_| |_|\__,_|_|_| |_|  \__\___/  |_____|_|     
                                                                 
     🔰 {gr}Domain to IP - Oday PrivGrabber 🔰  
         🔰 Contact : T.me/odayturkeyzsec 🔰   
                  -- Private Tools --                     
{res}
""")

def check_domain_ip(domain):
    """Check if a domain can be resolved to an IP address."""
    try:
      
        ip = socket.gethostbyname(domain)
        return ip
    except socket.error:
      
        return None

def worker(queue, output_file):
    """Worker thread to process domains from the queue."""
    while not queue.empty():
        domain = queue.get()
        domain = domain.strip()
        if domain:
            ip = check_domain_ip(domain)
            if ip:
              
                with open(output_file, "a") as f:
                    f.write(f"{ip}\n")
                print(f"{gr}[+]{res} Domain {gr}{domain}{res} -> {white}{ip}{res}")
            else:
                print(f"{red}[-]{res} Domain {red}{domain}{res} This domain is inactive.")
        queue.task_done()

def main():
  
    input_file = input(f"{white}{res} List domain.txt : ").strip()
    output_file = "good.txt"
    threads = int(input(f"{white}{res} Threads : ").strip())

    print(f"{white}[INFO]{gr} Proccess Check IP {white}{input_file}{res}...\n")

    try:
      
        with open(input_file, "r") as f:
            domains = f.readlines()
    except FileNotFoundError:
        print(f"{red}[ERROR]{res} File {white}{input_file}{res} not found!")
        return

   
    queue = Queue()
    for domain in domains:
        queue.put(domain)

   
    print(f"{gr}[+]{res} Proccess Scanning {threads} threads...\n")
    for _ in range(threads):
        thread = Thread(target=worker, args=(queue, output_file))
        thread.daemon = True 
        thread.start()

    queue.join()  
    print(f"\n{gr}[+]{gr} Success been saved to {white}{output_file}{res}.")

if __name__ == "__main__":
    main()
