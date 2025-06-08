import hashlib

class LoadBalancer:
    def __init__(self,servers):
        self.servers=servers
    
    def get_server(self,key):
        # converting key to consistent integer
        hash_val = int(hashlib.sha256(key.encode()).hexdigest(),16)
        index = hash_val%len(self.servers)
        return self.servers[index]


# servers = ['SA','SB','SC']
servers = ['SA','SB','SC','SD']
lb = LoadBalancer(servers)
requests=['user1','user2','user3','user4','user5']
for req in requests:
    assigned_server = lb.get_server(req)
    print(f'Request from {req} assigned to {assigned_server} ')