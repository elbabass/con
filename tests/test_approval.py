from approvaltests.approvals import verify
from con import (
    traduit_commande, remplace_commande_principale, traduit_ligne_commande,
)



def test_examples():
    input = ["tracte",
            "pulse",
            "forme",
            "bine",
            "fonde",
            "pare",
            "signe",
            "state",
            "comitant"]
    verify("\n".join([genere_traduction(nom) for nom in input]))

def genere_traduction(nom):
  actual = traduit_commande(nom)
  return f"* ``git {actual}`` → ``con {nom}``"

