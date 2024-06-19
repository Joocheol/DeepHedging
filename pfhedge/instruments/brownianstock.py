import torch


from pfhedge.instruments.stock import Stock

class BrownianStock(Stock):
    def __init__(self):
        super().__init__()

    def simulate(self):
        spot = torch.randn(1)
        self.register_buffer("spot", spot)
        

if __name__ == '__main__':
    a = BrownianStock()
    a.simulate()

    print(a.spot)


