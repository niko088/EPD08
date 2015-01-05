class Empleado():
    """ Clase empleado"""
    def __init__(self, nombre, apellidos, dni, direccion, edad, email, salario):
        """
        constructor

        inicializa el constructor

        :param nombre: nombre del empleado
        :param apellidos: apellidos del empleado
        :param dni: dni del empleado
        :param direccion: direccion del empleado
        :param edad: edad del empleado
        :param email: email del empleado
        :param salario: salario del empleado
        :return:
        """
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.direccion = direccion
        self.edad = edad
        self.email = email
        self.salario = salario

    def get_salario(self):
        """
        metodo consultor del salario

        devuelve el salario del empleado

        :return salario: devuelve el salario
        :rtype salario: Float
        """
        return self.salario

    def get_dni(self):
        """
        metodo consulto del dni

        devuelve el dni del empleado


        :return dni: devuelve el dni del empleado
        :rtype dni: String
        """
        return self.dni

    def get_edad(self):
        """
        metodo consulto de la edad

        devuelve la edad del empleado


        :return edad: devuelve la edad del empleado
        :rtype edad: Integer
        """
        return self.edad

    def get_email(self):
        """
        metodo consulto del email

        devuelve el email del empleado

        :return email: devuelve el email del empleado
        :rtype email: String
        """
        return self.email

    def get_direccion(self):
        """
        metodo consulto de la direccion

        devuelve de la direccion del empleado


        :return direccion: devuelve la direcion del empleado
        :rtype dni: String
        """
        return self.direccion

    def get_salario_mensual(self):
        """
        metodo consulto del salario mensual

        devuelve el salario mensual del empleado


        :return salario: devuelve el salario entre 12
        :rtype dni: Float
        """
        return self.salario / 12

    def get_nombre_apellidos(self):
        return self.nombre + " " + self.apellidos

