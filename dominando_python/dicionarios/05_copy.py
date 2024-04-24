contatos = {"thiago@gmail.com": {"nome": "Thiago", "telefone": "3333-2221"}}

copia = contatos.copy()
copia["thiago@gmail.com"] = {"nome": "Thi"}

print(contatos["thiago@gmail.com"])  # {"nome": "Thiago", "telefone": "3333-2221"}

print(copia["thiago@gmail.com"])  # {"nome": "Thi"}
