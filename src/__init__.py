from pymol import cmd, stored

from src.dnaseq import myqtdialog

def __init_plugin__(app=None):
    from pymol.plugins import addmenuitemqt
    addmenuitemqt('DNASeq Kinase Analyzer', myqtdialog)