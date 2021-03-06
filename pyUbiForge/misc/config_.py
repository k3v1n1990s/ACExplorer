import json


class Config:
	def __init__(self):
		try:
			with open("config.json") as f:
				self.CONFIG = json.load(f)
		except:
			self.CONFIG = {}

		default_config = {
			"missingNo": "resources/missingNo.png",

			"gameFolders": {
				"ACU": "",
			},

			"dumpFolder": "",

			"logFile": "ACExplorer.log",
			"tempFilesMaxMemoryMB": 2048,
			"writeToDisk": False,
			"dev": False
		}

		for key, val in default_config.items():
			if key not in self.CONFIG:
				self.CONFIG[key] = val

		for key, val in default_config["gameFolders"].items():
			if key not in self.CONFIG["gameFolders"]:
				self.CONFIG["gameFolders"][key] = val

	@property
	def raw(self):
		return self.CONFIG

	def __getitem__(self, item):
		return self.CONFIG.get(item, None)

	def __setitem__(self, key, value):
		self.CONFIG[key] = value

	def game_folder(self, identifier):
		return self.CONFIG["gameFolders"].get(identifier, ".")

	def save(self):
		with open('./config.json', 'w') as f:
			json.dump(self.raw, f, indent=4)
