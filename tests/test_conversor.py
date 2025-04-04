
import pytest

from main import conver_moeda, taxa_camb 

#teste para ver se conversao retorna um numero.
def test_conversao_valida():
    resultado = conver_moeda(10, "USD", "BRL")  
    assert isinstance(resultado, float)  

#teste se a taxa de cambio é buscada corretamente.
def test_taxa_camb():
    taxa = taxa_camb("USD", "BRL")
    assert isinstance(taxa, float)  

#teste para verificar erro quando a moeda de destino é invalida.
def test_conversao_moeda_invalida():
    with pytest.raises(ValueError):
        conver_moeda(10, "USD", "XXX") 

#teste para verificar erro quando a moeda de origem é inválida.
def test_taxa_camb_invalida():
    with pytest.raises(Exception):
        taxa_camb("XXX", "BRL") 

# teste para converter um valor zero
def test_conversao_zero():
    resultado = conver_moeda(0, "USD", "BRL")
    assert resultado == 0
    