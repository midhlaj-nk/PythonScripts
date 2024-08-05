def add_to_hosts(ip_address, domain):
    try:
        with open('/etc/hosts', 'a') as hosts_file:
            hosts_file.write(ip_address + ' ' + domain + '\n')
        print("Entry added successfully to /etc/hosts")
    except PermissionError:
        print("Permission denied. Please run this script with sudo.")

def main():
    ip_address = input("Enter IP address: ")
    domain = input("Enter domain: ")
    add_to_hosts(ip_address, domain)

if __name__ == "__main__":
    main()