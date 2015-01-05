class Departamento():
    """ Clase departamento """

    def __init__(self, nombre_depto, id_depto):
        """
        constructor

        inicializa el constructor
        :param nombre_depto: dept
        :param id_depto: identificador
        :type nombre_depto: String
        :type id_depto: String
        :return:
        """
        self.nombre_depto = nombre_depto
        self.id_depto = id_depto
        self.lista = []

    def get_nombre_depto(self):
        """
        Nombre dept

        Nombre completo depto

        :return: Metodo consultor nombre del departamento
        :rtype: String
        """
        return self.nombre_depto

    def get_salario_total_mensual(self):
        """
        Salario total

        Salaraio total mensual

        :return total: Devuelve el salario total mensual
        :rtype: Float
        """
        total = 0
        for empleado in self.lista:
            total = total + empleado.get_salario_mensual()
        return total

    def aniadir_empleado(self, empleado):
        """
        Anade un emepleado

        Anade un empleado a la lista

        :param empleado: el empleado a insertar
        :type empleado: Empleado
        :raise empleado: Puede lanzar una excepcion
        :return:
        """
        self.lista.append(empleado)

    def get_salario_total(self):
        """
        Devuelve el salario

        Devuelve el salario total

        :return total: devuelve el total
        :rtype total: Float
        """
        total = 0
        for empleado in self.lista:
            total = total + empleado.get_salario()
        return total