# File: docs/specs/frete.md

# Especificação: Cálculo de Frete

## Requisitos Funcionais
* **RF-01 (Event-Driven):** WHEN o usuário calcular o frete e o carrinho atingir o limite regional, THE SYSTEM SHALL zerar o frete.
* **RF-02 (Ubiquitous):** THE SYSTEM SHALL responder 90% resquisições em menos de 2s.
* **RF-03 (Event-Driven):** WHEN o usuário aplicar o cupom 'PROMO10', THE SYSTEM SHALL aplicar 10% sobre o valor total do carrinho.

## Regras de Negócio e Exceções
* **RB-01:** WHILE a região for 'Norte' o limite é R$300.00. Demais regiões: R$200.00.
* **RB-02:** IF valor <= 0, THEN exibir erro 'Valor de carrinho inválido'.
