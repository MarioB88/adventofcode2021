
## Creamos una clase para hacer mas sencillo el manejo de tableros

class Board():
    def __init__(self):
        self.matriz = []
        
## Iteramos por el tablero para comprobar si ha ganado horizontalmente acabando las iteraciones cada vez que no sea posible la victoria

    def winner_horizontal(self):

        for row in self.matriz:
            winner = True
            for col in row:
                if not col[1]:
                    winner = False
                    break
            if winner:
                return True
                
## Hacemos lo mismo que horizontalmente pero verticalmente

    def winner_vertical(self):

        for j in range(0, len(self.matriz)):
            winner = True
            for row in self.matriz:
                if not row[j][1]:
                    winner = False
                    break
            if winner:
                return True
                
## Marcamos como verdadero los numeros del tablero que coincidan con el numero correspondiente

    def check_coincidence(self, n):
        for row in self.matriz:
            for col in row:
                if n == col[0]:
                    col[1] = True
                
## Calculamos la puntuacion como lo indica el enunciado

    def score(self):
        score = 0
        for row in self.matriz:
            for col in row:
                if not col[1]:
                    score += int(col[0])
        return score