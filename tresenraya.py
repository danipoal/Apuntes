import tkinter as tk

class TicTacToe(tk.Frame):
  def __init__(self, parent):
    tk.Frame.__init__(self, parent)
    self.parent = parent
    self.buttons = [[tk.Button(self, width=10, height=5, command=lambda r=r, c=c: self.play(r, c)) for c in range(3)] for r in range(3)]
    for r in range(3):
      for c in range(3):
        self.buttons[r][c].grid(row=r, column=c)
    self.board = [[' ' for _ in range(3)] for _ in range(3)]
    self.player = 'X'

  def play(self, row, col):
    if self.board[row][col] != ' ':
      return
    self.board[row][col] = self.player
    self.buttons[row][col]['text'] = self.player
    if self.player == 'X':
      self.player = 'O'
    else:
      self.player = 'X'
    winner = self.check_winner()
    if winner:
      self.parent.title(f"El ganador es {winner}")

  def check_winner(self):
    # Verificar filas
    for row in self.board:
      if row[0] != ' ' and row[0] == row[1] == row[2]:
        return row[0]
    # Verificar columnas
    for col in range(3):
      if self.board[0][col] != ' ' and self.board[0][col] == self.board[1][col] == self.board[2][col]:
        return self.board[0][col]
    # Verificar diagonales
    if self.board[0][0] != ' ' and self.board[0][0] == self.board[1][1] == self.board[2][2]:
      return self.board[0][0]
    if self.board[0][2] != ' ' and self.board[0][2] == self.board[1][1] == self.board[2][0]:
      return self.board[0][2]
    return None

if __name__ == "__main__":
  root = tk.Tk()
  root.title("3 en raya")
  TicTacToe(root).pack()
  root.mainloop()

#__init__: es el método constructor de la clase TicTacToe. Se ejecuta cuando se crea una nueva instancia de la clase. Inicializa el tablero y el primer jugador y crea una matriz de botones para representar el tablero.
#play: es un método de la clase TicTacToe que se llama cada vez que se hace clic en un botón del tablero. Actualiza el tablero y cambia el turno del jugador. También verifica si hay un ganador y, si es así, cambia el título de la ventana para mostrar el nombre del ganador.
#check_winner: es un método de la clase TicTacToe que verifica si hay un ganador en el tablero actual. Si hay un ganador, devuelve el nombre del ganador; de lo contrario, devuelve None.
#pack: es un método del widget Frame que empaqueta el widget dentro de su contenedor padre.
#mainloop: es un método de la ventana principal que inicia el bucle principal de la aplicación. Esto hace que la ventana se muestre en la pantalla y permite que el usuario interactúe con ella.

#Importamos la biblioteca de interfaz gráfica de usuario (GUI) Tkinter como tk.
#Definimos la clase TicTacToe que hereda de la clase Frame de Tkinter. Esta clase representa el juego de 3 en raya y contiene toda la lógica del juego.
#En el método constructor __init__, inicializamos la clase padre Frame y guardamos una referencia al widget padre (la ventana principal). Luego creamos una matriz de botones para representar el tablero y los empaquetamos en la ventana usando el método grid. También inicializamos el tablero y el primer jugador.
#Definimos el método play, que se llama cada vez que se hace clic en un botón del tablero. Este método actualiza el tablero y cambia el turno del jugador. También verifica si hay un ganador y, si es así, cambia el título de la ventana para mostrar el nombre del ganador.
#Definimos el método check_winner, que verifica si hay un ganador en el tablero actual. Si hay un ganador, devuelve el nombre del ganador; de lo contrario, devuelve None.
#Si el módulo se está ejecutando directamente (es decir, no se está importando desde otro módulo), creamos una instancia de la clase Tk para crear la ventana principal y establecemos su título. Luego creamos una instancia de la clase TicTacToe y la empaquetamos dentro de la ventana principal. Finalmente, iniciamos el bucle principal de la aplicación con el método mainloop.##