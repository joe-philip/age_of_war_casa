from itertools import permutations
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
            self.HEAVYCAVALRY: [self.MILITIA, self.FOOTARCHER, self.LIGHTCAVALRY],
            self.CAVALRYARCHER: [self.SPEARMEN, self.HEAVYCAVALRY],
            self.FOOTARCHER: [self.MILITIA, self.CAVALRYARCHER],
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

    def battle_result(self, own: tuple, enemy: tuple) -> bool | None:
        own_class, own_count = own
        enemy_class, enemy_count = enemy
        hierarchy = self.soldier_hierarchy()
        if enemy_class in hierarchy.get(own_class, []):
            own_count *= 2
        if own_class in hierarchy.get(enemy_class, []):
            enemy_count *= 2
        if own_count > enemy_count:
            return True
        elif own_count < enemy_count:
            return False
        return None

    def get_platoons(self, type: str) -> list:
        data = []
        for soldier_name, soldier_data in self.soldier_database.items():
            if (count := soldier_data.get(type, 0)) != 0:
                data.append((soldier_name, count))
        return list(filter(lambda x: x[1] != 0, data))

    def format_soldier_data(self, data: tuple) -> str:
        result = ''
        for soldier_name, count in data:
            result += f'{soldier_name}#{count};'
        return result[0:-1]

    def find_solution(self) -> str:
        own_platoons = self.get_platoons('own')
        enemy_platoons = self.get_platoons('enemy')
        army_combinations = tuple(permutations(own_platoons))
        for combination in army_combinations:
            results = []
            for i in range(len(combination)):
                results.append(
                    self.battle_result(
                        combination[i], enemy_platoons[i]
                    )
                )
            if results.count(True) >= 3:
                return self.format_soldier_data(combination)
        return "There is no chance of winning"


with open('input.txt', 'r') as handle:
    input_data = handle.read()
instance = AgeOfWar(input_data)
result = instance.find_solution()
print(result)
