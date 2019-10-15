import instabot

instaBot = instabot.Bot()

instaBot.login(username="username", password="password")

santaFe = instaBot.get_geotag_users("")
print (santaFe)

# Sigue a todos los usuarios que usen el Hashtag
# usuarios = instaBot.get_hashtag_users("Hashtag")
# for u in usuarios:
#	instaBot.follow(instaBot.get_username_from_user_id(u))

# Cumplir condición para follow al idUsuario
listaUsuarios = []

for user in santaFe:
	if (instaBot.get_user_followers(user) > 1000)
		listaUsuarios.append(u)
	

for idUsuario in listaUsuarios:
bot.follow(bot.get_username_from_user_id(idUsuario))

#idChu = bot.get_user_id_from_username('barbimt')
#bot.get_user_medias =("idChu")


