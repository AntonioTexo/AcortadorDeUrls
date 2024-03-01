from acortador import Acortador
from ventana import Ventana
import logging
import webbrowser
import pyperclip

class ProgramaAcortador():
    """
    Genera una ventana con la capacidad de acortar URL ingresados y pegarlos al portapapeles.
    """
    def __init__(self) -> None:
        # Se crea un objeto ventana y un acortador
        self.ventana = Ventana("Acortador de URLs por Antonio Texo")
        self.acortador = Acortador() 
        # Se agregan los compotentes a la ventana
        self.label_principal = self.ventana.agregar_label("Inserte URL para acortar", 0, 1, 5, 5)
        self.entry_url = self.ventana.agregar_entry(1, 1)
        self.boton_acortador = self.ventana.agregar_boton("Acortar url", 2, 1, self.acortaUrl, 5, 5)
        self.label_url_generado = self.ventana.agregar_label("", 3, 1, 5, 5)
        self.boton_copiar = self.ventana.agregar_boton("Copiar al portapapeles", 4, 1, self.copiarEnlace, 5, 5)
        self.boton_ir_a_url_generado = self.ventana.agregar_boton("Ir al url generado", 4, 2, self.abrir_url_generado, 5, 5)
        # Una variable que guardará nuestro URL acortado
        self.url_acortado: str = ""

    def abrir_url_generado(self) -> None:
        try:
            webbrowser.open(self.url_acortado)
        except ConnectionError:
            logging.debug("No se pudo abrir la URL solicitada debido a un problema de conexión.")
        except Exception as e:
            logging.error(f"Error al abrir la URL: {e}")

    def copiarEnlace(self) -> None:
        pyperclip.copy(self.url_acortado)

    def ejecutar(self) -> None:
        # Ciclo principal
        self.ventana.mainloop()
        
    def acortaUrl(self) -> None:
        """
        Toma el url ingresado y escribe un url acortado en su label correspondiente
        """
        url_ingresado = self.ventana.obtener_contenido_entry(self.entry_url)
        url_generado = self.acortador.acorta_url(url_ingresado)
        self.ventana.establecer_contenido_label(self.label_url_generado, url_generado)
        self.url_acortado = url_generado

def main() -> None:
    programa_principal = ProgramaAcortador()
    programa_principal.ejecutar()

if __name__ == "__main__":
    main()