from onto_lib.ontology_graph import *


def test_term():
    term = Term(
        termid='CL:0000555',
        name='neuronal brush cell'
    )
    assert term.is_a() == []

# TODO: Need actual tests here eventually...
