from HttpClients.GelbooruHttpClient import GelbooruHttpClient
from HttpClients.NekoHttpClient import NekoHttpClient
from HttpClients.WaifuHttpClient import WaifuHttpClient

WAIFU_API = WaifuHttpClient("https://api.waifu.pics/")
NEKO_API = NekoHttpClient("http://api.nekos.fun:8080/api/")
GELBOORU_API = GelbooruHttpClient("https://gelbooru.com//index.php?page=dapi&s=post&q=index")

commands = {
    "WAIFU": {"client": WAIFU_API, "category": "sfw/waifu", "karma": 10},
    "BONK": {"client": WAIFU_API, "category": "sfw/bonk", "karma": 20},
    "NEKO": {"client": WAIFU_API, "category": "nsfw/neko", "karma": -15},
    "HENTAI": {"client": WAIFU_API, "category": "nsfw/waifu", "karma": -10},
    "TRAP": {"client": WAIFU_API, "category": "nsfw/trap", "karma": -20},
    "UWU": {"client": WAIFU_API, "category": "sfw/neko", "karma": 15},
    "AWOO": {"client": WAIFU_API, "category": "sfw/awoo", "karma": 10},
    "MEGUMIN": {"client": WAIFU_API, "category": "sfw/megumin", "karma": 5},
    "BLOWJOB": {"client": WAIFU_API, "category": "nsfw/blowjob", "karma": -15},
    "NOM": {"client": WAIFU_API, "category": "sfw/nom", "karma": 15},
    "CUM": {"client": NEKO_API, "category": "cum", "karma": -10},
    "FEET": {"client": GELBOORU_API, "category": "foot_focus", "karma": 10},
    "LESBIAN": {"client": NEKO_API, "category": "lesbian", "karma": -15},
    "PUSSY": {"client": NEKO_API, "category": "pussy", "karma": -5},
    "AHEGAO": {"client": GELBOORU_API, "category": "ahegao", "karma": -10},
    "VTUBER": {"client": GELBOORU_API, "category": "virtual_youtuber+nude", "karma": -10}
}
