contatos = {"thiago@gmail.com": {"nome": "Thiago", "telefone": "3333-2221"}}

contatos.update({"thiago@gmail.com": {"nome": "Thi"}})
print(contatos)  # {'thiago@gmail.com': {'nome': 'Thi'}}

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
# {'thiago@gmail.com': {'nome': 'Thi'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}
print(contatos)
