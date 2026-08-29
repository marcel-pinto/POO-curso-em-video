from rich import print
from rich.panel import Panel

class ControleRemoto:
    def __init__(self, num_canais = 5, vol_max = 5):
        self.tv_ligada = False
        self.canais = range(1, num_canais+1)
        self.volumes = list(range(1, vol_max+1))

        self.canal_atual = 1
        self.vol_atual = 1
        self.vol_max = vol_max
        self.num_canais = num_canais

    def mudar_canal(self, botao):
        if botao == ">":
            self.canal_atual += 1
        elif botao == "<":
            self.canal_atual -= 1

        self.canal_atual = self.atualizar(self.canal_atual, self.num_canais)

    def atualizar(self, x_atual, xmax):
        if x_atual % xmax == 0:
            new_x = xmax
        else:
            new_x = x_atual % xmax
        return new_x

    def toggle_ligar(self):
        self.tv_ligada = not self.tv_ligada

    def mudar_volume(self, botao):
        if botao == "+" and self.vol_atual < self.vol_max:
            self.vol_atual += 1
        elif botao == "-" and self.vol_atual > 1:
            self.vol_atual -= 1


    def pressionar_botao(self, botao):
        match botao:
            case "@":
                self.toggle_ligar()
            case (">" | "<"):
                self.mudar_canal(botao) if self.tv_ligada else None
            case ("+" | "-"):
                self.mudar_volume(botao) if self.tv_ligada else None
            case _:
                pass

    def canal_selecionado(self):
        canais = [
            f"[on yellow]{c} [/]" if c == self.canal_atual else f"{c}"
            for c in range(1, self.num_canais+1)
        ]
        canal_selecionado = " ".join(canais)
        return canal_selecionado

    def volume_selecionado(self):
        volumes = [
            "[on green] [/]" if vol <= self.vol_atual - 1 else "[on white] [/]" 
            for vol in range(self.vol_max)
            ]
        return "".join(volumes)

    
    def display(self, largura = 35):
        if self.tv_ligada:
            message =  "CANAL  =  " + self.canal_selecionado()
            message += "\nVOLUME = " + self.volume_selecionado()
        else:
            message = ":prohibited: [red]A TV está desligada [/]"
        panel = Panel(message, title="[ TV ]", width=largura)
        print(panel, end="\r", flush=True)
        # return panel

c = ControleRemoto()

while True:
    c.display()
    botao = input(f"< CH{c.canal_atual} >    -  VOL{c.vol_atual} + ")
    if botao == "0":
        break
    else:
        c.pressionar_botao(botao)
