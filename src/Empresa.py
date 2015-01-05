class Empresa():
    """ Clase empresa"""
    def __init__(self, nombre_empresa, cif, razon_social):
        """
        constructor

        inicializa el constructor

        :param nombre_empresa: nombre de la empresa
        :param cif: cif de la empresa
        :param razon_social: razon social de la empresa
        :return:
        """
        self.nombre_empresa = nombre_empresa
        self.cif = cif
        self.razon_social = razon_social
        self.listaDepartamentos = []
