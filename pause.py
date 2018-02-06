import datetime

"""
Module servant à définir les pauses et à les calculer
"""

global right_ans
right_ans = ["<@362613708159188992>", "TIME", "TEMPS", "PAUSE", "BITE"]
global now
now = datetime.datetime.now()


def prochainepause():
    """
    Fonction définissant la prochaine horraire de pause
    """
    now = datetime.datetime.now()
    now_brk = now.strftime("%H:%M:%S")
    smk = "08:30:00"
    srt = "09:00:00"
    brk1 = "10:30:00"
    e_brk1 = "10:45:00"
    eat = "12:30:00"
    e_eat = "13:30:00"
    brk2 = "15:15:00"
    e_brk2 = "15:30:00"
    end = "17:00:00"
    s_srt = "La journée démarrera bientôt !"
    s_smk = "Go fumer !"
    s_brk = "C'est la pause !"
    s_eat = "Go manger !"
    s_end = "Finish !"
    s_we = "Nop !"

    if now.weekday is 5 or now.weekday is 6:
        return s_we
    
    elif now_brk < srt:
        return s_srt
    elif now_brk < brk1:
        return brk1
    #elif now_brk > brk1 and now_brk < eat:
    #    return eat
    #elif now_brk > brk1 and now_brk > eat and now_brk < brk2:
    #    return brk2
    #elif now_brk > brk2 and now_brk > miam and now_brk > brk1 and now_brk < end:
    #    return end
    #else:
    #    return None
    elif now_brk < e_brk1:
        return s_brk
    elif now_brk < eat:
        return eat
    elif now_brk < e_eat:
        return s_eat
    elif now_brk < brk2:
        return brk2
    elif now_brk < e_brk2:
        return s_brk
    elif now_brk < end:
        return end
    elif now_brk > end:
        return s_end
    else:
        pass

def tempsrestant(lapause):
    """
    Fonction définissant le temps restant entre x et x temps
    Paramètres(prochainepause)
    """
    if lapause[-1] == "!":
        return lapause
    else:
        maintenant_restant = datetime.datetime.now().strftime("%H:%M:%S")
        start = datetime.datetime.strptime(lapause, '%H:%M:%S')
        ends = datetime.datetime.strptime(maintenant_restant, '%H:%M:%S')

        diff = start - ends
        diff2 = str(diff).split(",")
        diff3 = "".join(diff2)
        return diff3

def check_message(message):
    """
    Vérifie que la commande à été tapée correctement
    """

    if message.upper() in right_ans:
        return True
