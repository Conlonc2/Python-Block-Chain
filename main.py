from Block import Block, Blockchain


def main():
    blockchain = Blockchain()

    how_many_blocks = int(input("How many blocks do you want to mine?: "))

    for n in range(how_many_blocks):
        blockchain.mine(Block("Block " + str(n+1)))


main()
