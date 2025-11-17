import flet as ft

# regras 
DEPENDENT = 189.59
# Dedução simplificada: 20% do rendimento com teto anual (ex.: R$ 16.754,34 -> mensal equivalente)
# Observe: atualize `SIMPLIFIED_TETO_ANUAL` conforme regras oficiais da Receita
SIMPLIFIED_TETO_ANUAL = 16754.34
SIMPLIFIED_TETO_MENSAL = round(SIMPLIFIED_TETO_ANUAL / 12, 2)

# tabela de faixas (limite_superior, aliquota_percent, parcela_deduzir)
TABELA = [
    (1903.98, 0.0, 0.0),
    (2826.65, 7.5, 142.80),
    (3751.05, 15.0, 354.80),
    (4664.68, 22.5, 636.13),
    (float('inf'), 27.5, 869.36),
]

def achar_faixa(valor):
    for limite, aliq, parcela in TABELA:
        if valor <= limite:
            return aliq, parcela
    return 0.0, 0.0

def calcular(salario, dependentes, usar_simpl):
    try:
        s = float(str(salario).replace(',', '.'))
    except:
        s = 0.0
    try:
        d = int(dependentes)
    except:
        d = 0
    ded_depend = DEPENDENT * d
    # dedução simplificada = min(20% do salário, teto mensal)
    simpl_calc = min(0.20 * s, SIMPLIFIED_TETO_MENSAL)
    ded = ded_depend
    if usar_simpl and simpl_calc > ded_depend:
        ded = simpl_calc
    base = s - ded
    if base < 0:
        base = 0.0
    aliq_percent, parcela = achar_faixa(base)
    if aliq_percent == 0.0:
        imposto = 0.0
    else:
        imposto_bruto = base * (aliq_percent/100)
        imposto = imposto_bruto - parcela
        if imposto < 0:
            imposto = 0.0
    liquido = s - imposto
    # resultados simples
    return {
        'salario': round(s,2),
        'desconto': round(ded,2),
        'base': round(base,2),
        'aliquota': aliq_percent,
        'parcela': round(parcela,2),
        'ir': round(imposto,2),
        'liquido': round(liquido,2),
    }

def main(page: ft.Page):
    page.title = "IRPF Calculadora"
    page.padding = 12
    page.window_width = 360
    page.window_height = 700

    salario = ft.TextField(label="Salário bruto (R$)", keyboard_type=ft.KeyboardType.NUMBER, hint_text="Ex: 10000.00")
    dependentes = ft.TextField(label="Dependentes", keyboard_type=ft.KeyboardType.NUMBER, hint_text="0")
    simpl = ft.Checkbox(label="Usar desconto simplificado (20% limitado ao teto)")
    resultado = ft.Column()

    def on_click(e):
        res = calcular(salario.value, dependentes.value, simpl.value)
        resultado.controls.clear()
        resultado.controls.append(ft.Text(f"Salário: R$ {res['salario']:.2f}"))
        resultado.controls.append(ft.Text(f"Desconto: R$ {res['desconto']:.2f}"))
        resultado.controls.append(ft.Text(f"Salário base: R$ {res['base']:.2f}"))
        if res['aliquota'] == 0.0:
            resultado.controls.append(ft.Text("Alíquota: Isento"))
        else:
            resultado.controls.append(ft.Text(f"Alíquota: {res['aliquota']:.1f}%"))
            resultado.controls.append(ft.Text(f"Parcela a deduzir: R$ {res['parcela']:.2f}"))
        resultado.controls.append(ft.Text(f"IR devido: R$ {res['ir']:.2f}"))
        resultado.controls.append(ft.Text(f"Salário líquido: R$ {res['liquido']:.2f}"))
        page.update()

    def on_clear(e):
        salario.value = ""
        dependentes.value = ""
        simpl.value = False
        resultado.controls.clear()
        page.update()

    btn_calc = ft.ElevatedButton(text="Calcular", on_click=on_click)
    btn_clear = ft.OutlinedButton(text="Limpar", on_click=on_clear)
    botoes = ft.Row([btn_calc, btn_clear], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    page.add(ft.Column([ft.Text('Calculadora IRPF'), salario, dependentes, simpl, botoes, ft.Divider(), resultado], spacing=8))

if __name__ == '__main__':
    ft.app(target=main)
