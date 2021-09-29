# coding: utf-8
from con import (
    traduit_commande,
)


def test_translate_push_to_pulse():
    assert "pulse" == traduit_commande("push")


def test_translate_unknown_command_returns_itself():
    assert "notranslation" == traduit_commande("notranslation")
