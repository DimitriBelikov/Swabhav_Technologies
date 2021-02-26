from services import contact_services as csvc

class contact_app:
    def __init__(self):
        self.services = csvc()
    
    def start_app(self):
        