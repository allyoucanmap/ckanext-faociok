#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from ckan.lib.i18n import get_lang
from ckanext.faociok.models import Vocabulary, VocabularyTerm


def get_fao_datatype(name):
    lang = get_lang()
    term = VocabularyTerm.get(Vocabulary.VOCABULARY_DATATYPE, name)
    return (term.get_label(lang).label or term.name) if term else None

def get_fao_m49_region(name):
    lang = get_lang()
    term = VocabularyTerm.get(Vocabulary.VOCABULARY_M49_REGIONS, name)
    if term:
        return term.get_label(lang).label or term.get_label('en').label
    return name 

def format_term(term, depth):
    return u'{}{}{}'.format('-' * depth, ' ' if depth else '', term)

def get_vocabulary_items(vocabulary_name):
    return [{'value': i[0], 'text': format_term(i[1], i[2])} for i in VocabularyTerm.get_terms(vocabulary_name, lang=get_lang())]
    
def load_json(value, fail=False):
    try:
        return json.loads(value)
    except (ValueError, TypeError,):
        if fail:
            raise
        return value

def get_vocabulary_items_annotated(vocabulary_name):
    return VocabularyTerm.get_terms(vocabulary_name, lang=get_lang(), include_dataset_count=True)
