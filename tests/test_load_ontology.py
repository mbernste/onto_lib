from onto_lib.load_ontology import *


def test_main():
    res = main()
    assert res.id == 'CVCL:C792'


def test_load():
    og, i, r = load("1")
    assert i[0] == 'CL'
