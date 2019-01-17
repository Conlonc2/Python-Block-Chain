from Block import Block, Blockchain


def main():
    blockchain = Blockchain()

    for n in range(10):
        blockchain.mine(Block("Block " + str(n+1)))


main()
