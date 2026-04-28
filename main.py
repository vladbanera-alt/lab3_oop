class Block:

    def __init__(self, name, material, hardness, weight, isSolid):
        self.name = name
        self.material = material
        self.hardness = hardness
        self.weight = weight
        self.isSolid = isSolid

    def __repr__(self):
        return (f"Назва блоку={self.name}, Матеріал={self.material}, "
                f"Твердість={self.hardness}, Вага={self.weight}, "
                f"Надійний={self.isSolid})")

    def __eq__(self, other):

        if not isinstance(other, Block):
            return False

        return (
            self.name == other.name and
            self.material == other.material and
            self.hardness == other.hardness and
            self.weight == other.weight and
            self.isSolid == other.isSolid
        )


class Program:


    @staticmethod
    def main():
        try:
            nzk = 5202
            c11 = nzk % 11

            print(f"C11 = {c11}")

            if c11 != 10:
                print("Wrong variant")
                return

            blocks = [
                Block("Stone", "rock", 5, 10, True),
                Block("Glass", "sand", 1, 3, False),
                Block("Wood", "organic", 3, 5, True),
                Block("Iron", "metal", 7, 15, True),
                Block("Leaves", "organic", 1, 2, False),
            ]

            blocksSorted = sorted(blocks, key=lambda b: (b.hardness, -b.weight))

            print("\nSorted blocks:")
            for b in blocksSorted:
                print(b)

            target = Block("Wood", "organic", 3, 5, True)

            found = None
            for b in blocksSorted:
                if b == target:
                    found = b
                    break

            print("\nSearch result:")
            print(found if found else "Not found")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    Program.main()
