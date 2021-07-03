from setuptools import setup, find_packages

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="onto_lib",
    version='1.0.0',
    license="MIT",
    description="Tools for loading and manipulating ontologies in Python",
    long_description="""
    Most of the ontologies under consideration come from the OBO Foundry and are thus 
    interoperable. Specifically, the ontologies link together via edges between terms that may span multiple 
    ontologies. Thus, a single "ontology graph" may span multiple ontologies. The central object that is used in this 
    package is an "ontology graph" object which represents a subset of the union of all ontologies. The file, 
    ontology_configurations.json denotes all of the ontology graphs that can be queried. Note, each ontology graph 
    has an ID. For example, ontology graph 17 represents the union of the Cell Ontology, Uberon, Disease Ontology, 
    Experimental Factors Ontology, and Cellosaurus. 
    The program general_ontology_tools.py contains the API for querying these ontology configurations. Specifically, 
    it addresses the following tasks: 
    1. Find all ancestors or descendants of a given ontology term 
    2. Given two ontology terms, determine whether one is an ancestor of another 
    3. Given a set of ontology terms, filter the set for all most-specific terms in the set. A term is most-specific 
    if no other term in the set is a descendant of the term. 
    4. Given a set of ontology terms, filter the set for all 
    most-general terms in the set. A term is most-general if no other term in the set is a descendant of the term. 
    """,
    author="Matthew Bernstein",
    author_email="mnbernstein@wisc.edu",
    url="https://github.com/Bishop-Laboratory/onto_lib",
    download_url="https://github.com/Bishop-Laboratory/onto_lib/releases/download/v1.0.0/onto_lib-1.0.0.linux-x86_64"
                 ".tar.gz",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='ontology utility obo graph bioinformatics',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
)
