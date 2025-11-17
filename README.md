Projeto IRPF - Calculadora

O que foi alterado:
- A dedução simplificada deixou de ser um valor fixo. Agora é calculada como `min(20% do rendimento, teto mensal)`.
- O teto anual usado atualmente está em `app.py` como `SIMPLIFIED_TETO_ANUAL = 16754.34`. Atualize esse valor conforme a fonte oficial (Receita Federal) para o ano-base desejado.

Como testar localmente:

No PowerShell execute:

```powershell
python .\run_tests.py
```

Próximos passos sugeridos:
- Confirmar o valor oficial do teto anual da dedução simplificada e atualizar `SIMPLIFIED_TETO_ANUAL` em `app.py`.
- Validar as faixas e parcelas (`TABELA`) com a tabela progressiva oficial da Receita para o ano-base correto.
- Se desejar, adicionar testes automatizados com asserts e integrar em CI.
