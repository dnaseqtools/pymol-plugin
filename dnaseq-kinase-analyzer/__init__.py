from pymol import cmd, stored



def __init_plugin__(app=None):
    from .ui.dnaseq import myqtdialog

    from pymol.plugins import addmenuitemqt
    addmenuitemqt('DNASeq Kinase Analyzer', myqtdialog)