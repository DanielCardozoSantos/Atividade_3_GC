import sys
import os
from conversor import fahrenheit_para_celsius, celsius_para_fahrenheit

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

def test_f_para_c_ponto_congelamento():
    #Testa a conversão de 32°F para 0°C
    assert fahrenheit_para_celsius(32) == 0

def test_f_para_c_ponto_ebulicao():
    #Testa a conversão de 212°F para 100°C
    assert fahrenheit_para_celsius(212) == 100

def test_c_para_f_ponto_congelamento():
    #Testa a conversão de 0°C para 32°F
    assert celsius_para_fahrenheit(0) == 32

def test_c_para_f_valor_comum():
    #Testa a conversão de 25°C para 77°F."""
    assert celsius_para_fahrenheit(25) == 77