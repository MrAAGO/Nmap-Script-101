import subprocess

def scan_network(network, arguments):
    # Set the target network and the arguments for the nmap scan
    target = network
    args = arguments

    # Open a file to save the output of the nmap scan
    with open('nmap_output.txt', 'w') as f:
        # Call the nmap command and pass the target, arguments, and output file as command-line arguments
        result = subprocess.run(['nmap', target, args, '-oN', f.name], stdout=subprocess.PIPE)

# Define the target network and the arguments for the scan
network = '192.168.1.0/24'
arguments = '-T4 -p- -A'

# Scan the network and save the output to a file
scan_network(network, arguments)
