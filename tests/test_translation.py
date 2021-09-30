# coding: utf-8
import pytest

from con import (
    traduit_commande,
)


@pytest.mark.parametrize("nom, name", [
    ("pulse", "push"),
    ("tracte", "pull"),
    ("bine", "merge"),
    ("pare", "diff"),
    ("fonde", "rebase"),
    ("signe", "log")
])
def test_translate_push_to_pulse(nom, name):
    assert nom == traduit_commande(name)


def test_translate_unknown_command_returns_itself():
    assert "notranslation" == traduit_commande("notranslation")
