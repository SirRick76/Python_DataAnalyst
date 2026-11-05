class AnaliseVendas:
    
    def __init__(self, loja, periodo,vendas):
        self.loja = loja
        self.periodo = periodo
        self.vendas = vendas
    def calcular_total(self):
        return sum(self.vendas)
    def calcular_media(self):
        return sum(self.vendas)/len(self.vendas)
    def apresentar_resultados(self):
        total = self.calcular_total()
        media = self.calcular_media()
        return f"{self.loja} | {self.periodo} | Total: {total}€ | Média: {media:.2f}€"

vendaBragaJan= AnaliseVendas("Braga","Janeiro",[450,800,320,650])
vendaPortoJan= AnaliseVendas("Porto","Janeiro",[900,750,400,600])
vendaBragaFev= AnaliseVendas("Braga","Fevereiro",[600,700,500,850])
vendaGuimaraesFev = AnaliseVendas("Guimarães", "Fevereiro",[700,950,500,800])

class AnaliseVendasComObjetivo(AnaliseVendas):
    def __init__(self, loja, periodo, vendas,objetivo):
        super().__init__(loja, periodo, vendas)
        self.objetivo=objetivo
    def verificar_objetivo(self):
        if sum(self.vendas)>self.objetivo:
            return("Objetivo atingido")
        else:
            return("Objetivo não atingido")

    def apresentar_resultados(self):
        total = self.calcular_total()
        media = self.calcular_media()
        objetivos=self.verificar_objetivo()
        return f"{self.loja} | {self.periodo} | Total: {total}€ | Média: {media:.2f}€| Objetivo: {objetivos}"

vendaPortoJan = AnaliseVendasComObjetivo("Porto","Janeiro",[900,750,400,600],2600)
vendaGuimaraesFev = AnaliseVendasComObjetivo("Guimarães", "Fevereiro",[700,950,500,800],3000)
