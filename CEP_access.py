import requests


class Search_address:
    def __init__(self,cep):
        cep = str(cep)
        if self.validatingcep(cep):
            self.cep = cep
        else:
            raise ValueError("Quantidade de dígitos do CEP é inválido")

    def __str__(self):
        return self.formatingcep()

    def validatingcep(self, cep):
        if len(cep) == 8:
            return True
        else:
            raise False


    def formatingcep(self):
        return "{}-{}".format(self.cep[:5], self.cep[5:])

    def acess_by_cep(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        r = requests.get(url)
        data = r.json()
        return (data['logradouro'], data['bairro'], data['localidade'], data['uf'])