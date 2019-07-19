import key
import requests

host = 'fw_ip_address' # change this ip to match your target

def get_api_key():
    """
    Gets API key from firewall or panorama and prints the output
    """
    get_key = requests.get('https://' + host + '/api/?type=keygen&'\
                 'user=admin&password=paloalto', verify=False)
    print(get_key.text)


def get_sys_info():
    """
    Gets system information. Using function to validate API key
    """
    output = requests.get('https://' + host + '/api/?type=op&cmd='\
            '<show><system><info></info></system></show>&key='\
            + key.pan_vm_key, verify=False)
    print(output.text)


# get_api_key()
get_sys_info()
