import instabot

instaBot = instabot.Bot()

instaBot.login(username="", password="")

santaFe = instaBot.get_geotag_medias('224442573')
print(santaFe)
