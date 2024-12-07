#
# -- basicCodeBlock.py
#
from pymol import cmd, stored

def __init_plugin__(app=None):
    from pymol.plugins import addmenuitemqt
    addmenuitemqt('DNASeq Kinase Analyzer', myqtdialog)

def myqtdialog():
    from pymol.Qt import QtWidgets
    QtWidgets.QMessageBox.information(None, 'DNASeq Kinase Analyzer', "There's nothing here yet because it's a WIP. There will be though!!")