from optparse import OptionParser

import ontology_graph
import load_ontology

ONT_NAME_TO_ONT_ID = {"EFO_CL_DOID_UBERON_CVCL":"17"}
ONT_ID_TO_OG = {
    x:load_ontology.load(x)[0] 
    for x in list(ONT_NAME_TO_ONT_ID.values())
}

def main():
    """
    results = get_ancestors_within_radius("CL:0000034", 4)
    for res in results:
        print ONT_ID_TO_OG["17"].id_to_term[res].name

    print(get_term_name_and_synonyms("CL:0000134"))
    """

    print(most_specific_terms(["CL:0000134", "CL:0000034", "CL:0000540"])) 

#########################################################
#   examples
#########################################################

def example_is_descendant():
    # True
    print(is_descendant(
        "CL:0000134",   # mesenchymal stem cell 
        "CL:0000034"    # stem cell
    ))

    # False
    print(is_descendant(
        "CL:0000134",   # mesenchymal stem cell 
        "CL:0000540"    # neuron
    ))

#########################################################
#   the API
#########################################################

def get_ontology_object(ont_id="17"):
    """
    Returns
    -------
    The ontology object
    """
    return ONT_ID_TO_OG[ont_id]


def get_term_name(term_id, ont_id="17"):
    """
    Given a term ID, return the term name.

    Parameters
    ----------
    term_id
        The ontology term ID.

    Returns
    ---------
    The term name.

    """
    og = ONT_ID_TO_OG[ont_id]
    return og.id_to_term[term_id].name


def get_term_name_and_synonyms(term_id):
    og = ONT_ID_TO_OG["17"]
    t_strs = set()
    term = og.id_to_term[term_id]
    t_strs.add(term.name)
    for syn in term.synonyms:
        t_strs.add(syn.syn_str)
    return list(t_strs) 


def descendants(term_id, ont_id="17"):
    """
    Get the descendant terms for a given input term.

    Parameters
    ----------
    term_id
        The ontology term ID.

    Returns
    ---------
    The term ID's of the descendant terms in the ontology.
    """
    og = ONT_ID_TO_OG[ont_id]
    return og.recursive_relationship(
        term_id, 
        recurs_relationships=['inv_is_a', 'inv_part_of']
    ) 


def ancestors(term_id, ont_id="17"):
    """
    Get the ancestor terms for a given input term.

    Parameters
    ----------
    term_id
        The ontology term ID.

    Returns
    ---------
    The term ID's of the descendant terms in the ontology.
    """
    og = ONT_ID_TO_OG[ont_id]
    return og.recursive_relationship(
        term_id,   
        recurs_relationships=['is_a', 'part_of']
    )

def most_specific_terms(term_ids, ont_id="17"):
    """
    Filter a set of ontology terms to only their most specific terms.
    
    Parameters
    ----------
    term_ids
        A collection of term ID's to be filtered.
    
    Returns
    -------
    A collection of term ID's within `term_ids` that are most-specific.
    That is, all term ID's within `term_ids` that do not have a 
    descendant in `term_ids`.
    """
    og = ONT_ID_TO_OG[ont_id]
    rels = ['is_a', 'part_of']
    return ontology_graph.most_specific_terms(
        term_ids, 
        og, 
        sup_relations=rels
    )


def most_general_terms(term_ids, ont_id="17"):
    """
    Filter a set of ontology terms to only their most general terms.
    
    Parameters
    ----------
    term_ids
        A collection of term ID's to be filtered.
    
    Returns
    -------
    A collection of term ID's within `term_ids` that are most general.
    That is, all term ID's within `term_ids` that do not have an 
    ancestor in `term_ids`.
    """
    og = ONT_ID_TO_OG[ont_id]
    rels = ['inv_is_a', 'inv_part_of']
    return ontology_graph.most_specific_terms(
        term_ids,
        og,
        sup_relations=rels
    )


def is_descendant(descendent, ancestor):
    og = ONT_ID_TO_OG["17"]
    sup_terms = og.recursive_relationship(
        descendent, 
        recurs_relationships=['is_a', 'part_of']
    )
    return ancestor in set(sup_terms)


def get_descendents_within_radius(term_id, radius):
    return _get_terms_within_radius(
        term_id, 
        radius, 
        relationships=['inv_is_a']
    )

def get_ancestors_within_radius(term_id, radius):
    return _get_terms_within_radius(
        term_id,
        radius,
        relationships=['is_a']
    )


def _get_terms_within_radius(
    term_id, 
    radius, 
    relationships
    ):
    og = ONT_ID_TO_OG["17"]
    result_terms = set()
    next_batch = set([term_id])
    for i in range(radius):
        new_next_batch = set()
        for curr_t_id in next_batch:
            curr_term = term = og.id_to_term[curr_t_id]
            for rel in relationships:
                if rel in curr_term.relationships:
                    new_next_batch.update(
                        curr_term.relationships[rel]
                    )
        result_terms.update(new_next_batch) 
        next_batch = new_next_batch
    return result_terms

if __name__ == "__main__":
    main()
