from onto_lib.general_ontology_tools import *
from onto_lib.load_ontology import *


ont_name_to_ont_id = {"EFO_CL_DOID_UBERON_CVCL": "17"}
ont_id_to_og = {
    x: load(x)[0]
    for x in list(ont_name_to_ont_id.values())
}


def test_is_descendant():
    # True
    should_true = is_descendant(
        "CL:0000134",  # mesenchymal stem cell
        "CL:0000034",  # stem cell
        ont_id_to_og=ont_id_to_og
    )

    # False
    should_false = is_descendant(
        "CL:0000134",  # mesenchymal stem cell
        "CL:0000540",  # neuron
        ont_id_to_og=ont_id_to_og
    )

    assert should_true and not should_false


def test_get_ontology_object():
    res = get_ontology_object(ont_id_to_og)
    assert res.__class__.__name__ == "MappableOntologyGraph"


def test_get_term_name():
    res = get_term_name('CL:0000540', ont_id_to_og)
    assert res == "neuron"


def test_get_term_name_and_synonyms():
    res = get_term_name_and_synonyms('CL:0000540', ont_id_to_og)
    assert {'nerve cell', 'neuron'}.issubset(res)


def test_descendants():
    res = descendants('CL:0000540', ont_id_to_og)
    assert 'CL:0000678' in res


def test_ancestors():
    res = ancestors('CL:0000678', ont_id_to_og)
    assert "CL:0000540" in res


def test_most_specific_terms():
    ids = descendants('CL:0000540', ont_id_to_og)
    assert 'CL:0000702' in most_specific_terms(ids, ont_id_to_og)


def test_most_specific_terms_custom():
    """
    results = get_ancestors_within_radius("CL:0000034", 4)
    for res in results:
        print ont_id_to_og["17"].id_to_term[res].name

    print(get_term_name_and_synonyms("CL:0000134"))
    """
    res = most_specific_terms(["CL:0000134", "CL:0000034", "CL:0000540"],
                              ont_id_to_og=ont_id_to_og)

    assert {'CL:0000540', 'CL:0000134'}.issubset(res)


def test_most_general_terms_custom():
    """
    results = get_ancestors_within_radius("CL:0000034", 4)
    for res in results:
        print ont_id_to_og["17"].id_to_term[res].name

    print(get_term_name_and_synonyms("CL:0000134"))
    """
    res = most_general_terms(["CL:0000134", "CL:0000034", "CL:0000540"],
                             ont_id_to_og=ont_id_to_og)

    assert {'CL:0000034', 'CL:0000540'}.issubset(res)


def test_get_descendents_within_radius():
    res = get_descendents_within_radius(term_id='CL:0000034',
                                        ont_id_to_og=ont_id_to_og,
                                        radius=2)

    assert 'CL:0002248' in res


def test_get_ancestors_within_radius():
    res = get_ancestors_within_radius(term_id='CL:0000034',
                                      ont_id_to_og=ont_id_to_og,
                                      radius=2)

    assert 'CL:0000003' in res


def test_get_terms_within_radius():
    res = get_terms_within_radius(term_id='CL:0000034',
                                  ont_id_to_og=ont_id_to_og,
                                  relationships=['is_a'],
                                  radius=2)

    assert 'CL:0000003' in res
