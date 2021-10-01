# coding: utf-8
import pytest

from con import (
    traduit_commande, remplace_commande_principale, traduit_ligne_commande,
)


@pytest.mark.parametrize("nom, name", [
    ("pulse", "push"),
    ("tracte", "pull"),
    ("bine", "merge"),
    ("pare", "diff"),
    ("fonde", "rebase"),
    ("signe", "log"),
    ("state", "status"),
    ("comitant", "commit")
])
def test_translate_push_to_pulse(nom, name):
    assert name == traduit_commande(nom)


def test_translate_unknown_command_returns_itself():
    assert "notranslation" == traduit_commande("notranslation")


def test_remplace_commande_principale_avec_git():
    input_command_argv = ["toto", "titi", "tutu", "tata"]
    expected_command_argv = ["git", "titi", "tutu", "tata"]
    assert expected_command_argv == remplace_commande_principale(input_command_argv)

def test_traduit_ligne_de_commande_complete():
    input_command_argv = ["git", "pulse", "tutu", "tata"]
    expected_command_argv = ["git", "push", "tutu", "tata"]
    assert expected_command_argv == traduit_ligne_commande(input_command_argv)
