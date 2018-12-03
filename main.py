from Block import Block
import datetime

# Hand jam the first block


def create_genesis_block():
    return Block(0, datetime.datetime.now(), "Genesis Block", "0")

# all blocks after the first will be made here


def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = datetime.datetime.now()
    this_data = "Hey! I'm block " + str(this_index)
    this_signature = last_block.signature
    return Block(this_index, this_timestamp, this_data, this_signature)


def main():
    # Create the blockchain and add the genesis block
    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]

    # How many blocks after the genisis block
    blocks_going_in = 20

    # Adding to chain
    for i in range(blocks_going_in):
        block_to_add = next_block(previous_block)
        blockchain.append(block_to_add)
        previous_block = block_to_add
        # Tell everyone about it!
        print("Block #{} has been added to the chain!".format(
            block_to_add.index))
        print("This blocks signature is: {}\n".format(block_to_add.signature))


main()
