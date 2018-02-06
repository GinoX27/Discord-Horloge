import asyncio
import datetime
import discord
import pause
import aide

token = "token"
pinged = "<@362613708159188992>"
ping_ginox27 = "<@117636215011803145>"
ping_everyone = "<@365423175703461888>"
token_horloge = "token_horloge"
client = discord.Client()
salon_horloge = discord.Object(id="365057695201624067")



@client.event
async def on_message(message):
    """
    À la réception d'un message
    """


    if pause.check_message(message.content) is True and not message.channel.is_private:
        print("Jour : " +str(datetime.datetime.weekday(datetime.datetime.now())))
        answer_brk = ""
        answer_brk_nostr = ""
        tmp_pause = pause.prochainepause()
        if tmp_pause[-1] == "!":
            answer_brk = " " + tmp_pause
            answer_brk_nostr = answer_brk
        else:
            answer_brk_nostr = pause.tempsrestant(tmp_pause)
            answer_brk = " Il reste " + pause.tempsrestant(tmp_pause)

        tmp_msg = discord.Embed(title="Statut",
                                description=answer_brk,
                                color=0x010101,)
        print(message.content+ " utilisé par "+ message.author.name)
        await client.send_message(salon_horloge, message.author.mention, embed=tmp_msg)
        print("Résultat de la commande : "+ answer_brk_nostr)
        print("Temps de la prochaine pause : "+ tmp_pause, end='\n\n')
    if message.content == "!tg" and message.author.id == "117636215011803145":
        await client.close()
    if message.content == "!tg" and message.author.id != "117636215011803145":
        rep_emb = discord.Embed(title=ping_ginox27 + " a tenté de m'arrêter",
                                description="**Vatfer**")
        await client.send_message(salon_horloge, message.author.mention, embed=rep_emb)
    if message.content == pinged + " help" or message.content == pinged + " aide":
        await client.send_message(salon_horloge, aide.reponse(client.user.name))

@client.event
async def on_ready():
    """
    Quand le client est prêt
    """
    print("Connecté en tant que "+ client.user.name + " " + client.user.id, end='\n\n')



client.run(token_horloge)
