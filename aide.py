import pause


good_ans = pause.right_ans
def reponse(name):
    """Message réponse de la commande"""
    #lareponse = "Voice les éléments qui déclenche " + name + "\n"+ good_ans
    for trigger in good_ans:
        triggers = trigger
    lareponse = "Voici les éléments qui déclenche " + name + "`" + good_ans + "`"
    return lareponse