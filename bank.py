class Bank:
    _instance = None
    
    def __init__(self):
        if Bank._instance is not None:
            raise Exception("This is a singleton!")
        self.users = []
        Bank._instance = self
        
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = Bank()
        return cls._instance
    
    def add_user(self, user):
        self.users.append(user)
        
    def find_user(self, name):
        return next((u for u in self.users if u.name == name), None)
