from MetaMusic.core.bot import Meta
from MetaMusic.core.dir import dirr
from MetaMusic.core.git import git
from MetaMusic.core.userbot import Userbot
from MetaMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Meta()
userbot = Userbot()


from .platforms import Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, MusicAPI

Apple = Apple()
Resso = Resso()
SoundCloud = SoundCloud()
Spotify = Spotify()
Telegram = Telegram()
YouTube = YouTube()
MusicAPI = MusicAPI()