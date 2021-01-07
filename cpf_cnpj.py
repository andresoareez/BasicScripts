from validate_docbr import CPF, CNPJ


class document:

    @staticmethod
    def create_document(document):
        if len(document) == 11:
            return DocCpf(document)
        elif len(document) == 14:
            return DocCnpj(document)
        else:
            raise ValueError("Quantidade de dígitos é inválida")


class DocCpf:
    def __init__(self, document):
        if self.to_valid(document):
            self.cpf = document
        else:
            raise ValueError("O Cpf não é válido")

    def __str__(self):
        return self.to_format()

    def to_valid(self, document):
        validator = CPF()
        return validator.validate(document)

    def to_format(self):
        padrao = CPF()
        return padrao.mask(self.cpf)


class DocCnpj:

    def __init__(self, document):
        if self.to_valid(document):
            self.cnpj = document
        else:
            raise ValueError ("O CNPJ não é válido")

    def __str__(self):
        return self.to_format()

    def to_valid(self, document):
        validator_cnpj = CNPJ()
        return validator_cnpj.validate(document)

    def to_format(self):
        pattern = CNPJ()
        return pattern.mask(self.cnpj)


