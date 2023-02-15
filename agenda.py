class Agenda:
    def __init__(self):
        self.contatos = {}

    def adicionar_contato(self, numero, nome):
        if not 'Contatos' in self.contatos:
            self.contatos['Contatos'] = {numero: nome}
        else:
            self.contatos['Contatos'].update({numero: nome})
    
    def excluir_contato(self, numero):
        if numero not in self.contatos['Contatos']:
            print('Este numero não existe')
        else:
            self.contatos['Contatos'].pop(numero)

    def editar_contato(self, numero, nome):
        ...
        
        




class Conatato(Agenda):
    ...


agenda = Agenda()

agenda.adicionar_contato('21 8929238', 'Felipe')
agenda.adicionar_contato('21 9821398', 'Lucas')

print(agenda.contatos)

agenda.excluir_contato('21 9821398')


print(agenda.contatos)




