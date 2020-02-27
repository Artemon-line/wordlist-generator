from strgen import StringGenerator


class WordlistGenerator():
    def __init__(self, filename: str, amount: int, size: int):
        super().__init__()
        self.filename = filename
        self.amount = amount
        self.size = size
        print(f"""
============================================================================
                    Simple WordList Generator
============================================================================
            Will generate wordlist with parameters:
            Filename:   {self.filename}
            Amount:     {self.amount}
            Size:       {self.size}
============================================================================
        """)

    def generate(self):
        F = open(self.filename, 'w')
        for x in StringGenerator("[\w]{"+str(self.amount)+"}").render_list(self.size, unique=True):
            res = str(x)
            print(x)
            F.write(res + "\n")
            pass
        F.close()


if __name__ == "__main__":
    defaults = dict(name="wordlist.txt", amount="8", size="100")
    name = input(f"Filename: ({defaults['name']})") or defaults['name']
    amount = input(f"Amount: ({defaults['amount']}) ") or defaults['amount']
    size = input(f"Size: ({defaults['size']})") or defaults['size']
    wlgen = WordlistGenerator(name, int(amount), int(size))
    wlgen.generate()
