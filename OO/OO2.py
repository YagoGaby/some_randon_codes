class progama:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
    
    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()
 




class Filme(progama):
    def __init__(self, nome, ano, duracao):
        
        super().__init__(nome, ano)
        
        self.duracao = duracao 
       
    
vingadores = Filme('vingadores-guerra infinita', 2022, 160)


print(f'{vingadores.nome} - {vingadores.ano} - {vingadores.duracao}')


class Serie(progama):
    def __init__(self, nome, ano, temporadas):
        
        super().__init__(nome, ano )
        
        self.temporadas = temporadas 
        
    

GOT = Serie('Game of Thrones', 2014, 8)


print(f'{GOT.nome} - {GOT.ano} - {GOT.temporadas}')

filmes_e_series = [vingadores, GOT]

