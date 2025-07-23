from re import findall


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
        self.extract_input_data(input)

    def soldier_hierarchy(self) -> dict[str, list]:
        return {
            self.MILITIA: [self.SPEARMEN, self.LIGHTCAVALRY],
            self.SPEARMEN: [self.LIGHTCAVALRY, self.HEAVYCAVALRY],
            self.LIGHTCAVALRY: [self.FOOTARCHER, self.CAVALRYARCHER],
            self.HEAVYCAVALRY: [self.FOOTARCHER, self.LIGHTCAVALRY],
            self.FOOTARCHER: [self.SPEARMEN, self.HEAVYCAVALRY],
            self.CAVALRYARCHER: [self.MILITIA, self.CAVALRYARCHER],
        }

    def parse_input_line(self, line: str) -> dict[str, dict]:
        matches = findall(r';?(([MSLHCF][a-zA-Z]+)#(\d+))+;?', line)
        return_data = {}
        for match in matches:
            return_data[match[1]] = {
                'title': match[1],
                'count': int(match[2])
            }
        return return_data

    def store_data_to_soldier_database(self, data: dict[str, dict], data_type: str) -> None:
        for item in data:
            if item in self.soldier_database:
                self.soldier_database[item][data_type] = data[item].get(
                    'count', 0
                )
            else:
                self.soldier_database[item] = {
                    data_type: data[item].get('count', 0)}

    def extract_input_data(self, input: str) -> None:
        lines = input.strip().split('\n')
        own_data = self.parse_input_line(lines[0])
        self.store_data_to_soldier_database(own_data, 'own')
        enemy_data = self.parse_input_line(lines[1])
        self.store_data_to_soldier_database(enemy_data, 'enemy')
