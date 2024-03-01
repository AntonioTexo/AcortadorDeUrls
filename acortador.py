import pyshorteners as pys

class Acortador(pys.Shortener):
    """
    Clase heredada de Shortener
    """
    def __init__(self) -> None:
        """
        Inicializa un objeto de la clase Acortador.
        """
        super().__init__()

    def acorta_url(self, url_por_acortar: str) -> str:
        """
        Acorta un URL válido utilizando la extensión tinyurl.

        :param url: El URL que se va a acortar.
        :type url: str
        :return: El URL acortado.
        :rtype: str
        """
        acortado = self.tinyurl.short(url_por_acortar)
        return acortado
        
    
    def imprime_acortadores_disponibles(self) -> None:
        """
        Imprime la lista de servicios de acortamiento de URL disponibles.

        :return: None
        """
        print(self.available_shorteners)

def main() -> None:
    acortador = Acortador()
    print(acortador.acorta_url("https://www.facebook.com/"))

if __name__ == "__main__":
    main()
