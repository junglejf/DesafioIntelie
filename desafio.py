# -----------------------------------------------------------
# Desafio Intelie
#
# (C) 2019 Jorge Felipe Campos Chagas, Niterói-RJ, Brazil
# Released under GNU Public License (GPL)
# email jfcchagas@id.uff.br
# -----------------------------------------------------------
from __future__ import unicode_literals



facts = [
  ('gabriel', 'endereço', 'av rio branco, 109', True),
  ('joão', 'endereço', 'rua alice, 10', True),
  ('joão', 'endereço', 'rua bob, 88', True),
  ('joão', 'telefone', '234-5678', True),
  ('joão', 'telefone', '91234-5555', True),
  ('joão', 'telefone', '234-5678', False),
  ('gabriel', 'telefone', '98888-1111', True),
  ('gabriel', 'telefone', '56789-1010', True),
]
schema = [
    ('endereço', 'cardinality', 'one'),
    ('telefone', 'cardinality', 'many')
]

# Retorna cardinalidade de uma entidade se a tupla for no padrão (A,C,CV)
def get_cardinality (schema,entity):
    try:
        cardinality = next(
            cardinality_value for (name, _, cardinality_value) in schema
            if name == entity
        )
        return cardinality

    except StopIteration as e1:
        print(e1)
    except ValueError as e2:
        print(e2)
    except TypeError as e3:
        print(e3)

'''
Função responsável por conservar apenas o último registro de entidades 1:1.
Ela checa antes de inserir um novo registro com cardinalidade 1:1; caso já exista 
uma instância, esta será removida, já que tuplas são imutáveis e não podem ser
modificadas. 

Recebe como parâmetros a lista de fatos, a entidade e o atributo a ser controlado.
'''
def remove_old_fact (factlist,entity,atribute):
    for old_fact in factlist:
        if (entity in old_fact) and (atribute in old_fact):
            factlist.remove(old_fact)

'''
Função responsável por retornar o registro atualizado de fatos vigentes 
recebendo facts e schema como entrada
'''
def actual_facts(facts, schema):
    # Listas separadas para diminuir o espaço de busca no caso de cardinalidade == 'one'
    facts_many = []
    facts_one = []

    for fact in facts:
        entity_added = fact[-1]

        if entity_added:   # Filtrados os fatos ativos
            entity_name = fact[0]
            entity_atribute = fact[1]

            cardinality = get_cardinality(schema,entity_atribute)

            if cardinality == 'one':
                remove_old_fact(facts_one,entity_name,entity_atribute) # garantir só 1 registro quando mapeamento for 'one'
                facts_one.append(fact)
            else:
                facts_many.append(fact)

    return facts_one + facts_many


# Rodando o exemplo
updated_facts = actual_facts(facts,schema)
for fact in updated_facts:
    print(fact)