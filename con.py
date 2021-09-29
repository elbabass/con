#!/usr/bin/env python
# coding: utf-8


import subprocess

__version__ = '0.1.0'

TRADUCTIONS = {
    u'pull': u'tracte',
    u"push": u"pulse",
    u"clone": u"forme",
    u"merge": u"verge",
    u"rebase": u"fonde",
    u"diff": u"pare",
    u"log": u"signe"
}


def traduit_commande(commande):
    return commande if commande not in TRADUCTIONS.keys() else TRADUCTIONS[commande]


def main():
    subprocess.call(['ls'])


if __name__ == '__main__':  # pragma: no cover
    main()
