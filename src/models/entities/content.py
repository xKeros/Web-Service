from utils.DateFormat import DateFormat


class Content():

    def __init__(self, id_publicacion,  encabezado = None, registro = None) -> None:
        self.id_publicacion = id_publicacion
        self.encabezado = encabezado
        self.registro = registro

    def to_JSON(self):
        return {
            'id_publicacion': self.id_publicacion,
            'encabezado': self.encabezado,
            'registro': DateFormat.convert_date(self.registro)
        }
