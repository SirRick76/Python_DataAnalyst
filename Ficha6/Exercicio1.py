class Cliente:
    empresa = "Tech Solutions"
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone
    def apresentar(self):
        print("Nome:", self.nome, "| Email:", self.email)
    @classmethod
    def get_empresa(cls):
        print(cls.empresa)
    @staticmethod
    def saudacao():
        print("Bem-vindo ao sistema de clientes!")
cliente1= Cliente("Ricardo","r@gmail.com","939393939")
cliente2= Cliente("Sara","s@gmail.com","939393938")
cliente3= Cliente("Bruma","b@gmail.com","939393937")

class ClientePremium(Cliente):
    def __init__(self, nome, email, telefone,desconto):
        super().__init__(nome, email, telefone)
        self.desconto = desconto
    def apresentar(self):
        print("Nome:", self.nome, "| Email:", self.email,"| Telefone:", self.telefone,"| Desconto:", self.desconto)

class ClienteRegular(Cliente):
    def __init__(self, nome, email, telefone):
            super().__init__(nome, email, telefone)
    def apresentar(self):
            print("Nome:", self.nome, "| Email:", self.email,"| Telefone:", self.telefone,"| Cliente Regular")

cliente1 = ClientePremium("Ricardo", "r@gmail.com", "939393939", 15)
cliente2 = ClienteRegular("Sara", "s@gmail.com", "939393938")
cliente3 = ClientePremium("Bruma", "b@gmail.com", "939393937", 20)