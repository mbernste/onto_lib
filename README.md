# onto-lib

![Build Status](https://github.com/Bishop-Laboratory/onto_lib/workflows/package/badge.svg)

A library for loading, querying, and processing biomedical ontologies from OBO files.

### Ontologies included

This package arrives with the following ontologies:
* Disease Ontology (http://disease-ontology.org/)
* Cell Ontology (https://bioportal.bioontology.org/ontologies/CL)
* Uberon (http://uberon.github.io/)
* ChEBI (https://www.ebi.ac.uk/chebi/)
* Experimental Factor Ontology (http://www.ebi.ac.uk/efo/)
* Unit Ontology (https://bioportal.bioontology.org/ontologies/UO)
* Cellosaurus (http://web.expasy.org/cellosaurus/)

### Design philsophy

Most of the ontologies under consideration come from the OBO Foundry and are thus interoperable. Specifically, the ontologies link together via edges between terms that may span multiple ontologies. Thus, a single "ontology graph" may span multiple ontologies. The central object that is used in this package is an "ontology graph" object which represents a subset of the union of all ontologies. The file, `ontology_configurations.json` denotes all of the ontology graphs that can be queried. Note, each ontology graph has an ID. For example, ontology graph 17 represents the union of the Cell Ontology, Uberon, Disease Ontology, Experimental Factors Ontology, and Cellosaurus.

### Use

The program `general_ontology_tools.py` contains the API for querying these ontology
configurations. Specifically, it addresses the following tasks:

* Find all ancestors or descendants of a given ontology term
* Given two ontology terms, determine whether one is an ancestor of another
* Given a set of ontology terms, filter the set for all *most-specific* terms in the set. A term is *most-specific* if no other term in the set is a descendant of the term.
* Given a set of ontology terms, filter the set for all *most-general* terms in the set. A term is *most-general* if no other term in the set is a descendant of the term.

