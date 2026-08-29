from rich import print
from time import sleep
class Livro:
    tempo_passagem_pagina = 0.2

    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas_totais = paginas
        self.pagina_atual = 1

        mensagem = f":book: [blue]Você acabou de abrir o livro '[red]{self.titulo}[/]' que tem {self.paginas_totais} páginas no total. "
        mensagem += f"Você está na [yellow]página {self.pagina_atual}[/][/]"

        print(mensagem)

    def __str__(self):
        return f"Esse é o livro {self.titulo} com {self.paginas_totais} páginas. Você está na página {self.pagina_atual}."

    def avancar_paginas(self, paginas):
        for i in range(1, paginas+1):
            if self.pagina_atual == self.paginas_totais:
                break
            self.pagina_atual += 1
            sleep(Livro.tempo_passagem_pagina)
            print(f"Pág {self.pagina_atual} :arrow_forward:", end=" ")

        print(f"[blue]Você avançou {i} páginas e agora está na [yellow]página {self.pagina_atual}[/][/]")



        if self.pagina_atual == self.paginas_totais:
            print(f":rotating_light:[red] Você chegou ao final do livro '{self.titulo}'[/]")



l1 = Livro("10 coisas que aprendi", 20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(100)
# print(l1)