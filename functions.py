
from pathlib import Path

def generate_source_filename(name=None, year=2017):
    if name == 'depot': 
        return 'depots_deneigement_saison_{s}-{e}.csv'.format(s=year,e=year+1)
    elif name == 'secteur': 
        return 'secteurs_deneigement_saison_{s}-{e}.csv'.format(s=year,e=year+1)
    elif name == 'transaction': 
        return 'transactions_deneigement_saison_{s}-{e}.csv'.format(s=year,e=year+1)
    elif name == 'contrat': 
        return 'contrats_deneigement_saison_{s}-{e}.csv'.format(s=year,e=year+1)        
    else:
        raise 'name should be depot, secteur, transaction, contrat'
        return None

def generate_source_path(name=None,year=2017, prepath='./'):
    if name == 'depot':
        return Path(prepath,'data','depot',generate_source_filename(name,year))
    if name == 'secteur':
        return Path(prepath,'data','secteur',generate_source_filename(name,year))    
    if name == 'transaction':
        return Path(prepath,'data','transaction',generate_source_filename(name,year))
    if name == 'contrat':
        return Path(prepath,'data','contrat',generate_source_filename(name,year))
    else:
        return None