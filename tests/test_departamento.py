from unittest import TestCase
from mockito import *
from src.Departamento import *
from src.Empleado import Empleado


class TestDepartamento(TestCase):
    """ Clase test"""
    def test_get_salario_total(self):
        """
        Metodo para realizar pruebas

        Este metodo crea tres mockitos y realiza diversas pruebas para observar su correcto funcionamiento

        :return:
        """
        empleado1 = mock(Empleado)
        empleado2 = mock(Empleado)
        empleado3 = mock(Empleado)
        empleado4 = mock(Empleado)
        when(empleado1).get_salario().thenReturn(100)
        when(empleado2).get_salario().thenReturn(300)
        when(empleado3).get_salario().thenReturn(100)
        departamento = Departamento("software", 001)
        departamento.aniadir_empleado(empleado1)
        departamento.aniadir_empleado(empleado2)
        departamento.aniadir_empleado(empleado3)
        self.assertEqual(departamento.get_salario_total(), 500)

    def test_get_salario_total_mensual(self):
        empleado1 = mock(Empleado)
        empleado2 = mock(Empleado)
        when(empleado1).get_salario_mensual().thenReturn(1000)
        when(empleado2).get_salario_mensual().thenReturn(1000)
        departamento = Departamento("software", 001)
        departamento.aniadir_empleado(empleado1)
        departamento.aniadir_empleado(empleado2)
        self.assertEqual(departamento.get_salario_total_mensual(), 2000)