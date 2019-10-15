import instabot

instaBot = instabot.Bot()

instaBot.login(username="dronfy", password="hmukhtm822")

santaFe = instaBot.get_geotag_medias('224442573')
print(santaFe)