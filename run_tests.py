from app import calcular

cases = [
    (10000, 0, True, 'Salário 10.000, simplificado ON'),
    (10000, 0, False, 'Salário 10.000, simplificado OFF'),
    (3000, 1, True, 'Salário 3.000, 1 dependente, simplificado ON'),
    (1500, 0, False, 'Salário 1.500, isento provável'),
]

for salario, deps, simpl, desc in cases:
    res = calcular(salario, deps, simpl)
    print('---')
    print(desc)
    print(f"Salário bruto: R$ {res['salario']:.2f}")
    print(f"Desconto aplicado: R$ {res['desconto']:.2f}")
    print(f"Base de cálculo: R$ {res['base']:.2f}")
    if res['aliquota'] == 0.0:
        print('Alíquota: Isento')
    else:
        print(f"Alíquota: {res['aliquota']:.1f}%")
        print(f"Parcela a deduzir: R$ {res['parcela']:.2f}")
    print(f"IR devido: R$ {res['ir']:.2f}")
    print(f"Salário líquido: R$ {res['liquido']:.2f}")

print('\nTestes concluídos. Se quiser, posso adicionar asserts com valores esperados.')