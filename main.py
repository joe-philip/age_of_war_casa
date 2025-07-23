class AgeOfWar:
    def __init__(self, input: str) -> None:
        self.MILITIA = 'Militia'
        self.SPEARMEN = 'Spearmen'
        self.LIGHTCAVALRY = 'LightCavalry'
        self.HEAVYCAVALRY = 'HeavyCavalry'
        self.FOOTARCHER = 'FootArcher'
        self.CAVALRYARCHER = 'CavalryArcher'
        self.soldier_database: dict[str, dict] = {
            self.MILITIA: {},
            self.SPEARMEN: {},
            self.LIGHTCAVALRY: {},
            self.HEAVYCAVALRY: {},
            self.FOOTARCHER: {},
            self.CAVALRYARCHER: {},
        }
