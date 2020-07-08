#inventario de tienda Version inicial 7/7/2020
class CantidadCamisas:
    CuelloRedondo =0
    CuelloV=0
    CamisaDeTirantes=0
    CamisaMangaLarga=0
    def CantidadCR(self,numero):
        self.CuelloRedondo=numero
        return self.CuelloRedondo
    def CantidadCV(self,numero):
        self.CuelloV=numero
        return self.CuelloV
    def CantidadCT(self,numero):
        self.CamisaDeTirantes=numero
        return self.CamisaDeTirantes
    def CantidadML(self,numero):
        self.CamisaMangaLarga=numero
        return self.CamisaMangaLarga
CantidadCamisasCR=CantidadCamisas
CantidadCamisasCR.CantidadCR(CantidadCamisasCR,10)
CantidadCamisasCv=CantidadCamisas
CantidadCamisasCv.CantidadCV(CantidadCamisas,2)
CantidadCamisasT=CantidadCamisas
CantidadCamisasT.CantidadCT(CantidadCamisasT,19)
CantidadCamisasML=CantidadCamisas
CantidadCamisasML.CantidadML(CantidadCamisasML,10)
print("El numero de camisas Cuello Redondo es:",CantidadCamisasCR.CuelloRedondo)
print("El numero de camisas Cuello V es:",CantidadCamisasCv.CuelloV)
print("El numero de camisas tirantes es:",CantidadCamisasT.CamisaDeTirantes)
print("El numero de camisas manga larga es:",CantidadCamisasML.CamisaMangaLarga)
print("La cantidad de camisas cuello redondo es:",CantidadCamisasCR.CuelloRedondo,"El numero de camisas Cuello V es:",CantidadCamisasCv.CuelloV,"El numero de camisas tirantes es:",CantidadCamisasT.CamisaDeTirantes,"El numero de camisas manga larga es:",CantidadCamisasML.CamisaMangaLarga)