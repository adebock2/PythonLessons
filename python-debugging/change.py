class ChangeItForMe:
    def transact(self, cost, tender):
        tender = tender - cost

        d = -1
        for tender in range(tender, -1, -100):
            d = d + 1

        q = 0
        while tender >= 25:
            tender -= 25
            q += 1

        dd, tender = divmod(tender, 10)

        n = tender // 5
        if n > 0:
            tender -= n * 5

        return [tender, n, dd, q, d]

    def calculate(self, amount):
        # Calculate transaction
        return self.transact(0, amount)
