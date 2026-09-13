import pytest
from frete import calcular_frete

# >_ Conecta com: Atende RF-01 e RB-01
def test_frete_gratis_padrao():
    # Limite para outras regiões é R$ 200.00, logo R$ 250.00 deve zerar o frete.
    assert calcular_frete(valor_carrinho=250.0, regiao="Sudeste") == 0.0

# >_ Conecta com: Atende RF-01 e RB-01
def test_frete_gratis_regiao_norte():
    # Limite para a região Norte é R$ 300.00, logo R$ 300.00 exatos deve zerar o frete.
    assert calcular_frete(valor_carrinho=300.0, regiao="Norte") == 0.0

# >_ Conecta com: Atende RB-01 e RB-03
def test_cobrar_taxa_abaixo_limite():
    # Abaixo do limite de R$ 200.00, deve retornar a taxa de frete padrão (ex: 20.0).
    assert calcular_frete(valor_carrinho=150.0, regiao="Sudeste") == 20.0

# >_ Conecta com: Atende RB-02
def test_valor_carrinho_invalido():
    # Valores <= 0 devem lançar a exceção especificada.
    with pytest.raises(ValueError, match="Valor de carrinho inválido"):
        calcular_frete(valor_carrinho=0.0, regiao="Sudeste")

# >_ Conecta com: Atende RF-03
def test_aplicar_cupom_desconto():
    # O cupom 'PROMO10' deve reduzir o valor do carrinho em 10%.
    # Assumindo que para esse caso a função retorne um dicionário com os dados finais.
    resultado = calcular_frete(valor_carrinho=100.0, regiao="Sul", cupom="PROMO10")
    assert resultado["valor_carrinho"] == 90.0