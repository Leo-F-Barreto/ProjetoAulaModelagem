def calcular_frete(valor_carrinho, regiao, frete_base, cupom=None):
    if valor_carrinho <= 0:
        raise ValueError('Valor de carrinho inválido')

    # RB-01: Limites regionais para isenção
    limite_isencao = 300.00 if regiao.lower() == 'norte' else 200.00

    # RF-01: Zerar o frete se atingir o limite
    frete_final = 0.0 if valor_carrinho >= limite_isencao else frete_base

    # RF-03: Aplicar 10% de desconto sobre o carrinho se o cupom for válido
    valor_final = valor_carrinho
    if cupom == 'PROMO10':
        valor_final = valor_carrinho * 0.9

    return {
        "valor_carrinho": round(valor_final, 2),
        "frete_calculado": round(frete_final, 2),
        "total": round(valor_final + frete_final, 2)
    }