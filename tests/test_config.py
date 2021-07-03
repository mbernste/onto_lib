from onto_lib.config import *


def test_ontology_name_to_location():
    onto_loc = ontology_name_to_location()
    assert {'DOID', 'UBERON', 'CL', 'CVCL', 'UO', 'EFO', 'CHEBI', 'GO'}.issubset(onto_loc.keys())
