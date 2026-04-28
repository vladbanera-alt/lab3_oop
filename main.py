class Block:

    #клас описує будівельний блок

    def __init__(self, name, material, hardness, weight, is_solid):
    #ініціалізація об'єкта блоку
        self.name = name
        self.material = material
        self.hardness = hardness
        self.weight = weight
        self.is_solid = is_solid

    def __repr__(self):
    #повертає текстове представлення блоку
        return (f"Назва={self.name}, Матеріал={self.material}, "
                f"Твердість={self.hardness}, Вага={self.weight}, "
                f"Твердий={self.is_solid}")

    def __eq__(self, other):
        #порівняння 2 об'єктів
        if not isinstance(other, Block):
            return False

        return (
            self.name == other.name and
            self.material == other.material and
            self.hardness == other.hardness and
            self.weight == other.weight and
            self.is_solid == other.is_solid
        )


class Program:

    @staticmethod
    def calculate_variant(nzk):
        #визначення варіанту
        return nzk % 11

    @staticmethod
    def create_blocks():
    #створює список блоків
        return [
            Block("Stone", "rock", 5, 10, True),
            Block("Glass", "sand", 1, 3, False),
            Block("Wood", "organic", 3, 5, True),
            Block("Iron", "metal", 7, 15, True),
            Block("Leaves", "organic", 1, 2, False),
        ]

    @staticmethod
    def sort_blocks(blocks):
    #сортування блоків за твердістю та вагою
        return sorted(blocks, key=lambda b: (b.hardness, -b.weight))

    @staticmethod
    def find_block(blocks, target):
    #пошук ідентичного блоку
        for block in blocks:
            if block == target:
                return block
        return None

    @staticmethod
    def main():
        try:
            #мій номер залікової книжки
            nzk = 5202


            variant = Program.calculate_variant(nzk)
            print(f"C11 (варіант) = {variant}")


            if variant != 10:
                print("Ця програма реалізує тільки варіант 10")
                return


            blocks = Program.create_blocks()


            sorted_blocks = Program.sort_blocks(blocks)

            print("\nВідсортовані блоки:")
            for block in sorted_blocks:
                print(block)


            target_block = Block("Wood", "organic", 3, 5, True)


            found_block = Program.find_block(sorted_blocks, target_block)

            print("\nРезультат пошуку:")
            if found_block:
                print(found_block)
            else:
                print("Об'єкт не знайдено")

        except Exception as error:
            print("Виникла помилка:", error)


#вхід
if __name__ == "__main__":
    Program.main()
