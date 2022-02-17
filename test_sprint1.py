from sprint1 import remetente_prefixo_dr_dra, total_remetente_prefixo_dr_dra
from sprint1 import destinatario_prefixo_dr_dra,  total_destinatario_prefixo_dr_dra
from sprint1 import remetente_destinatario_prefixo_dr_dra
from sprint1 import destinatario_busca_sobrenomes
from sprint1 import destinatario_busca_sobrenomes_primeiros
from sprint1 import destinatario_busca_sobrenomes_ultimos
from sprint1 import remetente_destinatario_mesmo_estado
from sprint1 import busca_email_remetente
from sprint1 import busca_email_destinatario
from sprint1 import busca_estado_remetente
from sprint1 import busca_email_remetente_por_dominio
from sprint1 import busca_email_destinatario_por_dominio
from sprint1 import busca_cpf
from sprint1 import busca_primeira_data_por_mes
from sprint1 import busca_segunda_data_por_mes
from sprint1 import busca_terceira_data_por_mes
from sprint1 import busca_data

import pickle
import pytest


class LoadData:
    def load_list(self):
        with open('lista.bin', 'rb') as list_in_file:
            self.lista = pickle.load(list_in_file)


class TestRemetentePrefixoDrDra(LoadData):
    def test_prefixo_dr_dra(self):
        self.load_list()
        sublista = remetente_prefixo_dr_dra(self.lista)
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 354

    def test_total_prefixo_dr_dra(self):
        self.load_list()
        total = total_remetente_prefixo_dr_dra(self.lista)
        assert isinstance(total, int)
        assert total == 354


class TestDestinatarioPrefixoDrDra(LoadData):
    def test_prefixo_dr_dra(self):
        self.load_list()
        sublista = destinatario_prefixo_dr_dra(self.lista)
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 319

    def test_total_destinatario_prefixo_dr_dra(self):
        self.load_list()
        total = total_destinatario_prefixo_dr_dra(self.lista)
        assert isinstance(total, int)
        assert total == 319


class TestDestinatarioRemetentePrefixoDrDra(LoadData):
    def test_prefixo_dr_dra(self):
        self.load_list()
        sublista = remetente_destinatario_prefixo_dr_dra(self.lista)
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert sublista[0][0].startswith('Dr')
        assert sublista[0][4].startswith('Dr')
        assert len(sublista) == 24


class TestDestinatarioBuscaSobrenomes(LoadData):
    def test_busca_sobrenomes(self):
        self.load_list()
        sublista = destinatario_busca_sobrenomes(self.lista, 'Silva')
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 78
        assert len(sublista[0]) == 2
        sublista = destinatario_busca_sobrenomes(self.lista, 'Fogaça')
        assert len(sublista) == 74
        assert len(sublista[0]) == 2


class TestDestinatarioBuscaSobrenomesPrimeiros(LoadData):
    def test_busca_sobrenomes(self):
        self.load_list()
        sublista = destinatario_busca_sobrenomes_primeiros(self.lista, 'Silva')
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 10
        assert len(sublista[0]) == 2
        sublista = destinatario_busca_sobrenomes_primeiros(self.lista, 'Fogaça')
        assert len(sublista) == 10
        assert len(sublista[0]) == 2


class TestDestinatarioBuscaSobrenomesUltimos(LoadData):
    def test_busca_sobrenomes(self):
        self.load_list()
        sublista = destinatario_busca_sobrenomes_ultimos(self.lista, 'Silva')
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 10
        assert len(sublista[0]) == 2
        sublista_ini = destinatario_busca_sobrenomes_primeiros(self.lista, 'Fogaça')
        sublista = destinatario_busca_sobrenomes_ultimos(self.lista, 'Fogaça')
        assert len(sublista) == 10
        assert len(sublista[0]) == 2
        assert sublista_ini != sublista


class TestRemetenteDestinatarioMesmoEstado(LoadData):
    def test_remetente_destinatario_mesmo_estado(self):
        self.load_list()
        sublista = remetente_destinatario_mesmo_estado(self.lista)
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 195
        assert len(sublista[0]) == 11


class TestBuscaEmailRemetente(LoadData):
    def test_busca_email_remetente(self):
        self.load_list()
        sublista = busca_email_remetente(self.lista, 'cteixeira@yahoo.com.br')
        assert isinstance(sublista, list)
        assert isinstance(sublista, tuple)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 2
        assert len(sublista[0]) == 11
        sublista = busca_email_remetente(self.lista, 'manuela29@barros.br')
        assert isinstance(sublista, list)
        assert isinstance(sublista, tuple)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 1
        assert len(sublista[0]) == 11
        sublista = busca_email_remetente(self.lista, 'xyz@xtz.com')
        assert isinstance(sublista, list)
        assert isinstance(sublista, tuple)
        assert len(sublista) == 0


class TestBuscaEmailDestinatario(LoadData):
    def test_busca_email_destinatario(self):
        self.load_list()
        sublista = busca_email_destinatario(self.lista, 'ocaldeira@gmail.com')
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 2
        assert len(sublista[0]) == 11
        sublista = busca_email_destinatario(self.lista, 'samuel17@hotmail.com')
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 1
        assert len(sublista[0]) == 11
        sublista = busca_email_destinatario(self.lista, 'xyz@xtz.com')
        assert isinstance(sublista, list)
        assert len(sublista) == 0


class TestBuscaEstadoRemetente(LoadData):
    def test_busca_estado_remetente(self):
        self.load_list()
        sublista = busca_estado_remetente(self.lista)
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], str)
        assert len(sublista) == 27


class TestBuscaEmailRemetentePorDominio(LoadData):
    def test_busca_email_remetente_por_dominio(self):
        self.load_list()
        lista_com_dados = busca_email_remetente_por_dominio(self.lista)
        assert isinstance(lista_com_dados, list)
        assert isinstance(lista_com_dados[0], tuple)
        assert len(lista_com_dados) == 442
        lista_com_dados = busca_email_remetente_por_dominio(self.lista, 'bol.com.br')
        assert isinstance(lista_com_dados, list)
        assert isinstance(lista_com_dados[0], tuple)
        assert len(lista_com_dados) == 420
        lista_vazia = busca_email_remetente_por_dominio(self.lista, 'gmail3.com')
        assert isinstance(lista_vazia, list)
        assert lista_vazia == []


class TestBuscaEmailDestinatarioPorDominio(LoadData):
    def test_busca_email_remetente_por_dominio(self):
        self.load_list()
        lista_com_dados = busca_email_destinatario_por_dominio(self.lista)
        assert isinstance(lista_com_dados, list)
        assert isinstance(lista_com_dados[0], tuple)
        assert len(lista_com_dados) == 454
        lista_com_dados = busca_email_destinatario_por_dominio(self.lista, 'bol.com.br')
        assert isinstance(lista_com_dados, list)
        assert isinstance(lista_com_dados[0], tuple)
        assert len(lista_com_dados) == 409
        lista_vazia = busca_email_destinatario_por_dominio(self.lista, 'gmail3.com')
        assert isinstance(lista_vazia, list)
        assert lista_vazia == []


class TestBuscaCPF(LoadData):
    def test_busca_cpf(self):
        self.load_list()
        lista_com_dados = busca_cpf(self.lista, '238.540.761-26')
        assert isinstance(lista_com_dados, list)
        assert isinstance(lista_com_dados[0], tuple)
        assert lista_com_dados[0][0] == 'Catarina Oliveira'
        assert len(lista_com_dados) == 1
        lista_com_dados = busca_cpf(self.lista, '874.639.152-55')
        assert isinstance(lista_com_dados, list)
        assert isinstance(lista_com_dados[0], tuple)
        assert lista_com_dados[0][0] == 'Catarina Oliveira'
        assert len(lista_com_dados) == 1
        lista_vazia = busca_cpf(self.lista, '000.000.000-00')
        assert isinstance(lista_com_dados, list)
        assert isinstance(lista_com_dados[0], tuple)
        assert len(lista_vazia) == 0


class TestBuscaPrimeiraDataMes(LoadData):
    def test_primeira_data_mes(self):
        self.load_list()
        lista_com_dados = busca_primeira_data_por_mes(self.lista, '02')
        assert isinstance(lista_com_dados, list)
        assert isinstance(lista_com_dados[0], tuple)
        assert len(lista_com_dados) == 1885
        lista_vazia = busca_primeira_data_por_mes(self.lista, '13')
        assert isinstance(lista_vazia, list)
        assert len(lista_vazia) == 0


class TestBuscaSegundaDataMes(LoadData):
    def test_segunda_data_mes(self):
        self.load_list()
        lista_com_dados = busca_segunda_data_por_mes(self.lista, '05')
        assert isinstance(lista_com_dados, list)
        assert isinstance(lista_com_dados[0], tuple)
        assert len(lista_com_dados) == 1382
        lista_vazia = busca_segunda_data_por_mes(self.lista, '13')
        assert isinstance(lista_vazia, list)
        assert len(lista_vazia) == 0


class TestBuscaTerceiraDataMes(LoadData):
    def test_segunda_data_mes(self):
        self.load_list()
        lista_com_dados = busca_terceira_data_por_mes(self.lista, '07')
        assert isinstance(lista_com_dados, list)
        assert isinstance(lista_com_dados[0], tuple)
        assert len(lista_com_dados) == 1415
        lista_vazia = busca_terceira_data_por_mes(self.lista, '13')
        assert isinstance(lista_vazia, list)
        assert len(lista_vazia) == 0


class TestBuscaData(LoadData):
    def test_busca_data(self):
        self.load_list()
        lista_com_dados = busca_data(self.lista)
        assert isinstance(lista_com_dados, list)
        assert isinstance(lista_com_dados[0], tuple)
        assert len(lista_com_dados) == 89
        lista_com_dados = busca_data(self.lista, dia='15')
        assert isinstance(lista_com_dados, list)
        assert isinstance(lista_com_dados[0], tuple)
        assert len(lista_com_dados) == 95
        lista_com_dados = busca_data(self.lista, dia='15', mes='03')
        assert isinstance(lista_com_dados, list)
        assert isinstance(lista_com_dados[0], tuple)
        assert len(lista_com_dados) == 61
        lista_vazia = busca_data(self.lista, dia='15', mes='03', ano='2017')
        assert isinstance(lista_vazia, list)
        assert len(lista_vazia) == 0

