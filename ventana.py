import tkinter as tk

class Ventana(tk.Tk):
    # Constructor
    def __init__(self, 
                 titulo: str = "Nueva ventana", 
                 ancho: int=400,
                 alto: int=360
                 ) -> None:
        super().__init__() # Iniciamos el objeto de la clase madre
        self.minsize(width=ancho, height=alto) # Ajustamos el tamaño de la ventana
        self.title(titulo) # Agregamos un título
    
    def agregar_entry(self,
                      fila: int,
                      columna: int,
                      paddingx: int = 0,
                      paddingy: int = 0
                      ) -> tk.Entry:
        entrada = tk.Entry(self)
        entrada.grid(row=fila, column=columna, padx=paddingx, pady=paddingy)
        return entrada

    def agregar_boton(self,
                      texto: str = None, 
                      fila: int = None,
                      columna: int = None,
                      comando: callable=None,
                      paddingx: int = 0,
                      paddingy: int = 0
                      ) -> tk.Button:
        boton = tk.Button(self, text=texto, command=comando)
        boton.grid(row=fila, column=columna, padx=paddingx, pady=paddingy)
        return boton

    def agregar_label(self,
                      texto: str,
                      fila: int,
                      columna: int,
                      paddingx: int = 0, 
                      paddingy: int = 0
                      ) -> tk.Label:
        label = tk.Label(self, text=texto)
        label.grid(row=fila, column=columna, padx=paddingx, pady=paddingy)
        return label
    
    def editar_accion_boton(self, boton: tk.Button, accion: callable=None) -> None:
        boton.config(command=accion)
    
    def obtener_contenido_entry(self, entry: tk.Entry) -> str:
        return entry.get()
        
    def establecer_contenido_label(self, label: tk.Label, contenido: str) -> None:
        label.config(text=contenido)
        
def main() -> None:
    mi_ventana = Ventana("Prueba", 600, 480)
    boton_saludo = mi_ventana.agregar_boton("Saludo", 1, 1)
    entry_mi_nombre = mi_ventana.agregar_entry(2,1)
    def escribe_mi_nombre() -> None:
        contenido = mi_ventana.obtener_contenido_entry(entry_mi_nombre)
        print(contenido)
    mi_ventana.editar_accion_boton(boton_saludo, escribe_mi_nombre)
    nombre = 'tonoto'
    mi_ventana.mainloop()

if __name__ == '__main__':
    main()