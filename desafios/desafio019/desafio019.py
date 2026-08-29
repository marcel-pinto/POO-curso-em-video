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

    def avancar_paginas(self, paginas = 1):
        cont = 0
        for _ in range(paginas):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(f"Pág {self.pagina_atual} :arrow_forward:", end=" ")
                sleep(Livro.tempo_passagem_pagina)
                cont += 1

        print(f"[blue]Você avançou {cont} páginas e agora está na [yellow]página {self.pagina_atual}[/][/]")

        if self.fim_do_livro():
            print(f":closed_book:[red] Você chegou ao final do livro '{self.titulo}'[/]")

    def fim_do_livro(self) -> bool:
        return self.pagina_atual == self.paginas_totais


l1 = Livro("10 coisas que aprendi", 20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(50)
