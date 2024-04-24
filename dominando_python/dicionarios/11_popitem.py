contatos = {"thiago@gmail.com": {"nome": "Thiago", "telefone": "3333-2221"}}

resultado = contatos.popitem()  # ('thiago@gmail.com', {'nome': 'Thiago', 'telefone': '3333-2221'})
print(resultado)

# contatos.popitem()  # KeyError
