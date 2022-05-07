from approvaltests.approvals import verify
from con import (
    traduit_commande, remplace_commande_principale, traduit_ligne_commande,
)


def test_examples():
    input_list = ["tracte",
                  "pulse",
                  "forme",
                  "bine",
                  "fonde",
                  "pare",
                  "signe",
                  "state",
                  "comitant",
                  "sulte"]
    generated_example = "== Con - Documentation\n\n\n"
    generated_example += "\n".join([genere_traduction(nom) for nom in input_list])
    verify(generated_example)


def genere_traduction(nom):
    actual = traduit_commande(nom)
    return f"* ``git {actual}`` → ``con {nom}``"
