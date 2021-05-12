from backend.blockchain.block import Block


class Blockchain:
    """
    Blockchain: A public ledger of transactions
    Implemented as a list of blocks - data sets of transactions
    """
    def __init__(self):
        self.chain = [Block.genesis()]

    def Add_block(self, data):
        self.chain.append(Block.mine_block(self.chain[-1], data))

    def __repr__(self):
        return f'blockchain : {self.chain}'


def main():

    blockchain = Blockchain()
    blockchain.Add_block('one')
    blockchain.Add_block('two')

    print(blockchain)
    print(f'Blockchain.py __name__ : {__name__}')
    

if __name__ == '__main__':
    main()
