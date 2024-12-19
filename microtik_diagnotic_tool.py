from librouteros import connect
import paramiko
#from librouteros.query import Key

# Data connection
API_HOST = '192.168.88.1'
API_USER = 'admin'
API_PASS = ''

def get_router_info(api):
    """Get the basis Microtik information"""
    system_info = list(api('/system/resource/print'))[0]
    print(f"\n=== MikroTik Info===")
    print(f"Model: {system_info['board-name']}")
    print(f"Version: {system_info['version']}")
    print(f"Uptime: {system_info['uptime']}")
    print(f"CPU-Load: {system_info['cpu-load']}%")
    print(f"Memory usage: {system_info['free-memory']} free of {system_info['total-memory']}")

def get_interfaces_status(api):
    """Get the status of the interfaces"""
    interfaces = list(api('/interface/print'))
    print(f"\n=== Interfaces status ===")
    #print(f"Model: {interfaces['board-name']}")
    for interface in interfaces:
        print(f"Interface name: {interface['name']} | Active: {interface['running']}")
        
def perform_ping_ssh(host, username, password, address="8.8.8.8", count=10, size=64, interval=0.1, ttl=20):
    """Perform an extended ping via SSH."""
    try:
        # Connect to MikroTik via SSH
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=username, password=password)

        # Execute the ping command
        command = f"ping {address} count={count} size={size} interval={interval} ttl={ttl}"
        stdin, stdout, stderr = ssh.exec_command(command)

        # Print the results
        print(f"\n=== Extended Ping to {address} ===")
        for line in stdout.read().decode().splitlines():
            print(line)

        ssh.close()
    except Exception as e:
        print(f"Error: {e}")

def get_clock_info(api):
    """Retrieve the clock configuration."""
    clock_info = list(api('/system/clock/print'))[0]
    print("\n=== Clock Configuration ===")
    print(f"Date: {clock_info['date']}")
    print(f"Time: {clock_info['time']}")


def main():
    try:
        print("Connecting to the Microtik...")
        # Connect to the Microtik
        api = connect(username=API_USER, password=API_PASS, host=API_HOST)
        print("Connected successfully\n")

        get_router_info(api)
        get_interfaces_status(api)
        perform_ping_ssh(host=API_HOST, username=API_USER, password=API_PASS)
        get_clock_info(api)


    except ConnectionError:
        print("Error: Connection error, check the IP and credentials.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("\nDiagnostic completed.")

if __name__ == '__main__':
    main()