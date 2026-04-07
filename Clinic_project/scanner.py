import socket

def start_scan():
    print("--- port security scanning tool - إعداد عباس كعدة ---")
    target = input("Enter the website address to check it19    (example google.com): ")
    # فحص أشهر 3 منافذ أمنية
    ports = [21, 80, 443] 
    
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[+] المنفذ {port}: open (ثغرة محتملة)")
        else:
            print(f"[-] المنفذ {port}: close (آمن)")
        s.close()

if __name__ == "__main__":
    start_scan()