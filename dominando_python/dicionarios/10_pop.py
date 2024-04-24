contatos = {"thiago@gmail.com": {"nome": "Thiago", "telefone": "3333-2221"}}

resultado = contatos.pop("thiago@gmail.com")  # {'nome': 'Thiago', 'telefone': '3333-2221'}
print(resultado)

resultado = contatos.pop("thiago@gmail.com", {})  # {}
print(resultado)
