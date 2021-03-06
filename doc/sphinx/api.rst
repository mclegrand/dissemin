.. _page-api:

Dissemin API
============

Dissemin provides an API to query the availability of arbitrary papers.
Please do not assume the interface will not change in the future as it
is still being improved.

Querying by DOI
---------------

You can retrieve Dissemin's metadata for a specific paper by DOI:

https://dissem.in/api/10.1016/j.paid.2009.02.013.

Searching for papers
--------------------

The search interface is also exposed as an API. The parameters it
understands are the same as the human-readable version at
https://dissem.in/search . Statistics about
the results are also returned as well.

https://dissem.in/api/search/?q=pregroup

Understanding the results
-------------------------

::

    {

        "status": "ok",
        "paper": {
            "classification": "UNK",
            "title": "Refining the Conceptualization of an Important
    Future-Oriented Self-Regulatory Behavior: Proactive Coping",
            "pdf\_url": "http://www.ncbi.nlm.nih.gov/pubmed/19578529",
            "records": [
                {
                    "splash\_url":
    "https://doi.org/10.1016/j.paid.2009.02.013",
                    "doi": "10.1016/j.paid.2009.02.013",
                    "publisher": "Elsevier BV",
                    "issue": "2",
                    "journal": "Personality and Individual Differences",
                    "issn": "0191-8869",
                    "volume": "47",
                    "source": "crossref",
                    "policy": {
                        "romeo\_id": "30",
                        "preprint": "can",
                        "postprint": "can",
                        "published": "cannot"
                    },
                    "identifier":
    "oai:crossref.org:10.1016/j.paid.2009.02.013",
                    "type": "journal-article",
                    "pages": "139-144"
                },
                {
                    "splash\_url":
    "https://www.researchgate.net/publication/26648440\_Refining\_the\_Conceptualization\_of\_an\_Important\_Future-Oriented\_Self-Regulatory\_Behavior\_Proactive\_Coping",
                    "doi": "10.1016/j.paid.2009.02.013",
                    "contributors": "",
                    "abstract": "Proactive coping, directed at an upcoming as
    opposed to an ongoing stressor, is a new focus in positive psychology
    research. However, two differing conceptualizations of this construct
    create confusion. This study compared how each operationalization of
    proactive coping relates to well-being. Participants (N = 281) facing an
    upcoming college examination completed the Proactive Coping Inventory
    (PCI; consisting of two subscales that each assess one of the
    conceptualizations), the Proactive Competence Scale (PCS; that assesses
    the proactive coping process), and measures of well-being. The results
    demonstrated that conceptualizing proactive coping as a
    positively-focused striving for goals was predictive of well-being (the
    shared variance from affect, subjective well-being and physical
    symptoms), whereas conceptualizing proactive coping as focused on
    preventing a negative future was not. The first conceptualization of
    proactive coping's unique association with well-being was explained by
    two of the proactive competencies, use of resources and realistic goal
    setting, and the remaining variance in well-being was explained by the
    first factor of optimism. These results demonstrated that aspiring for a
    positive future is distinctly predictive of well-being and that research
    should focus on accumulating resources and goal setting in designing
    interventions to promote proactive coping.",
                    "pdf\_url":
    "https://www.researchgate.net/profile/Stephanie\_Sohl2/publication/26648440\_Refining\_the\_Conceptualization\_of\_an\_Important\_Future-Oriented\_Self-Regulatory\_Behavior\_Proactive\_Coping/links/55e463c008ae2fac47227a76.pdf",
                    "source": "researchgate",
                    "keywords": "",
                    "identifier": "oai:researchgate.net:26648440",
                    "type": "journal-article"
                },
                {
                    "splash\_url":
    "http://www.ncbi.nlm.nih.gov/pubmed/19578529",
                    "doi": "10.1016/j.paid.2009.02.013",
                    "contributors": "",
                    "abstract": "Proactive coping, directed at an upcoming as
    opposed to an ongoing stressor, is a new focus in positive psychology
    research. However, two differing conceptualizations of this construct
    create confusion. This study compared how each operationalization of
    proactive coping relates to well-being. Participants (N = 281) facing an
    upcoming college examination completed the Proactive Coping Inventory
    (PCI; consisting of two subscales that each assess one of the
    conceptualizations), the Proactive Competence Scale (PCS; that assesses
    the proactive coping process), and measures of well-being. The results
    demonstrated that conceptualizing proactive coping as a
    positively-focused striving for goals was predictive of well-being (the
    shared variance from affect, subjective well-being and physical
    symptoms), whereas conceptualizing proactive coping as focused on
    preventing a negative future was not. The first conceptualization of
    proactive coping’s unique association with well-being was explained by
    two of the proactive competencies, use of resources and realistic goal
    setting, and the remaining variance in well-being was explained by the
    first factor of optimism. These results demonstrated that aspiring for a
    positive future is distinctly predictive of well-being and that research
    should focus on accumulating resources and goal setting in designing
    interventions to promote proactive coping.",
                    "pdf\_url": "http://www.ncbi.nlm.nih.gov/pubmed/19578529",
                    "source": "base",
                    "keywords": "Article",
                    "identifier":
    "ftpubmed:oai:pubmedcentral.nih.gov:2705166",
                    "type": "other"
                }
            ],
            "authors": [
                {
                    "name": {
                        "last": "Sohl",
                        "first": "Stephanie Jean"
                    }
                },
                {
                    "name": {
                        "last": "Moyer",
                        "first": "Anne"
                    }
                }
            ],
            "date": "2009-07-01",
            "type": "journal-article"
        }

    }

Most fields are self-explanatory, here is a quick description of the
other ones:

-  ***classification*** is the code for the self-archiving policy of the
   publisher "OA" (available from the publisher), "OK" (some version can
   be shared), "UNK" (unknown/unclear sharing policy), "NOK"
   (restrictive sharing policy).
-  ***pdf\_url*** is the URL where dissemin thinks the full text can be
   accessed for free. This is rarely a direct link to an actual PDF
   file. It is set to ``null`` if we could not find a free source for
   this paper.
-  ***records*** gives a list of the places where the full text has been
   made available (so: repositories, homepages or social networks).
   Sometimes, these repositories only contain a bibliographical record
   and not the full text. The ***pdf\_url*** field of each record
   indicates our assessment of the availability of that record. If the
   publisher has been found in RoMEO, it also indicates the summary of
   its policy, using the codes drawn from `the RoMEO
   API <http://www.sherpa.ac.uk/romeo/api.html>`__. This list will
   remain empty if no DOI is provided.

License, usage
--------------

CAPSH claims no ownership of the metadata served via this API. It has
been collected from various free sources.

The interface itself should not be abused: please do not use concurrent
connections on it, and keep your requests to a slow rate (at most one
per second). If you need a faster access to this data, please get in
touch with us.
