# Ajudantes para escrever as ondas.
# W(título, molde em inglês, molde em português, mod, cenário, itens, ator)
# itens: lista de tuplas OU texto "peça en = peça pt = emoji; ..." ({x} é trocado pela peça).
# FREE = a frase inteira vem no item. [a|o] = forma feminina|masculina.
FREE = '{x}'

def W(title, en, pt, mod, bg, items, actor='A'):
    if isinstance(items, str):
        items = [tuple(f.strip() for f in it.split('=')) for it in items.split(';') if it.strip()]
    for it in items:
        assert len(it) == 3, (title, it)
    return dict(title=title, en=en, pt=pt, mod=mod, bg=bg, actor=actor, items=items)

def D(n, waves):
    return dict(n=n, waves=waves)
