#!/usr/bin/env python
# coding: utf-8

import subprocess
import sys

TRADUCTIONS = {
    u'tracte': u'pull',
    u"pulse": u"push",
    u"forme": u"clone",
    u"bine": u"merge",
    u"fonde": u"rebase",
    u"pare": u"diff",
    u"signe": u"log",
    u"state": u"status",
    u"comitant": u"commit"
}


def traduit_commande(commande):
    if commande in TRADUCTIONS.keys():
        return TRADUCTIONS[commande]
    else:
        return commande


def remplace_commande_principale(commande):
    commande[0] = 'git'
    return commande


def traduit_ligne_commande(ligne_commande):
    return [traduit_commande(arg) for arg in ligne_commande]


def main():
    ligne_commande = remplace_commande_principale(sys.argv)
    command_line_list = traduit_ligne_commande(ligne_commande)
    subprocess.call(command_line_list)


if __name__ == '__main__':  # pragma: no cover
    main()
