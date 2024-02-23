class Client:
    def __init__(self,age,number,e_mail):
        self.age = age
        self.number = number
        self.e_mail = e_mail
        
    def show(self):
        print("Вік, клієнта:", self.age)
        print("nomer klienta:", self.number)
        print("Adresa klienta:", self.e_mail)
Client1 = Client(22, 6562785786, "oguzok1488@gmail.com")
Client2 = Client(34, 7578785989, "lavayasha@gmail.com")
Client3 = Client(19, 9376037475, "zapupkina@gmail.com")
Client1.show()
Client2.number ="7837583736"
Client3.show()
