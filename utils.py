import os
from dotenv import load_dotenv

def nornir_set_creds(nr):
    """
    Handler so credentials are not stored in cleartext. Scripts by Kirt Byers.
    """
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

    username = os.environ.get("USERNAME")
    password = os.environ.get("PASSWORD")

    for host in nr.inventory.hosts.values():
        host.username = username
        host.password = password