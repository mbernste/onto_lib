from . import ontology_graph


def get_ontology_object(ont_id_to_og, ont_id="17"):
    """
    Returns
    -------
    The ontology object
    """
    return ont_id_to_og[ont_id]


def get_term_name(term_id, ont_id_to_og, ont_id="17"):
    """
    Given a term ID, return the term name.

    Parameters
    ----------
    term_id: The ontology term ID.
    ont_id_to_og: The ontology mapping.
    ont_id: The ontology ID

    Returns
    ---------
    The term name.

    """
    og = ont_id_to_og[ont_id]
    return og.id_to_term[term_id].name


def get_term_name_and_synonyms(term_id,
                               ont_id_to_og):
    og = ont_id_to_og["17"]
    t_strs = set()
    term = og.id_to_term[term_id]
    t_strs.add(term.name)
    for syn in term.synonyms:
        t_strs.add(syn.syn_str)
    return list(t_strs)


def descendants(term_id, ont_id_to_og, ont_id="17"):
    """
    Get the descendant terms for a given input term.

    Parameters
    ----------
    term_id: The ontology term ID.
    ont_id_to_og: The ontology graph ID map
    ont_id: The ontology ID

    Returns
    ---------
    The term ID's of the descendant terms in the ontology.
    """
    og = ont_id_to_og[ont_id]
    return og.recursive_relationship(
        term_id,
        recurs_relationships=['inv_is_a', 'inv_part_of']
    )


def ancestors(term_id, ont_id_to_og, ont_id="17"):
    """
    Get the ancestor terms for a given input term.

    Parameters
    ----------
    term_id: The ontology term ID.
    ont_id_to_og: The ontology graph map.
    ont_id: The ontology ID.

    Returns
    ---------
    The term ID's of the descendant terms in the ontology.
    """
    og = ont_id_to_og[ont_id]
    return og.recursive_relationship(
        term_id,
        recurs_relationships=['is_a', 'part_of']
    )


def most_specific_terms(term_ids, ont_id_to_og, ont_id="17"):
    """
    Filter a set of ontology terms to only their most specific terms.
    Parameters
    ----------
    term_ids: A collection of term ID's to be filtered.
    ont_id_to_og: The ontology graph map.
    ont_id: The ontology ID
    Returns
    -------
    A collection of term ID's within `term_ids` that are most-specific.
    That is, all term ID's within `term_ids` that do not have a
    descendant in `term_ids`.
    """
    og = ont_id_to_og[ont_id]
    rels = ['is_a', 'part_of']
    return ontology_graph.most_specific_terms(
        term_ids,
        og,
        sup_relations=rels
    )


def most_general_terms(term_ids, ont_id_to_og, ont_id="17"):
    """
    Filter a set of ontology terms to only their most general terms.
    Parameters
    ----------
    term_ids: A collection of term ID's to be filtered.
    ont_id_to_og: The ontology graph map.
    ont_id: The ontology ID
    Returns
    -------
    A collection of term ID's within `term_ids` that are most general.
    That is, all term ID's within `term_ids` that do not have an
    ancestor in `term_ids`.
    """
    og = ont_id_to_og[ont_id]
    rels = ['inv_is_a', 'inv_part_of']
    return ontology_graph.most_specific_terms(
        term_ids,
        og,
        sup_relations=rels
    )


def is_descendant(descendent, ancestor, ont_id_to_og):
    og = ont_id_to_og["17"]
    sup_terms = og.recursive_relationship(
        descendent,
        recurs_relationships=['is_a', 'part_of']
    )
    return ancestor in set(sup_terms)


def get_descendents_within_radius(term_id, ont_id_to_og, radius):
    return get_terms_within_radius(
        term_id,
        radius,
        relationships=['inv_is_a'],
        ont_id_to_og=ont_id_to_og
    )


def get_ancestors_within_radius(term_id, radius, ont_id_to_og):
    return get_terms_within_radius(
        term_id,
        radius,
        relationships=['is_a'],
        ont_id_to_og=ont_id_to_og
    )


def get_terms_within_radius(
        term_id,
        radius,
        relationships,
        ont_id_to_og
):
    og = ont_id_to_og["17"]
    result_terms = set()
    next_batch = {term_id}
    for i in range(radius):
        new_next_batch = set()
        for curr_t_id in next_batch:
            curr_term = og.id_to_term[curr_t_id]
            for rel in relationships:
                if rel in curr_term.relationships:
                    new_next_batch.update(
                        curr_term.relationships[rel]
                    )
        result_terms.update(new_next_batch)
        next_batch = new_next_batch
    return result_terms
