import time
import blockParameters
import block

class Blockchain():
    def __init__(self):
        self.blockchain = self.get_blockchain()

    def get_latest_block(self):
        return self.blockchain[-1]

    def generate_next_block(self,data):
        index = len(self.blockchain)
        prev_hash = self.get_latest_block().hash
        timestamp = int(time.time())
        #now to wrap all the fields as block parameters
        new_block_params = blockParameters.BlockParameters(index, prev_hash, timestamp, data)

        new_block = block.Block(new_block_params)
        self.blockchain.append(new_block)

    def get_blockchain(self):
        #a block chain is linear list hence a particular chain has a single origin block
        #and a block can only originate a single list, hence a chain can be refered to by its genesis block
        return [block.Block.get_genesis_block()]

    def recv_new_block(self, new_block):
        #whenever the need is to "recieve" a new block to be added in a chain
        #authentication is required that it's not a illicit block
        #a simple set of checks may include the following:
        prev_block = self.get_latest_block()

        if not new_block.has_valid_index(prev_block):
            print('Invalid index!')
            return
        if not new_block.has_valid_prev_hash(prev_block):
            print('Invalid previous hash!')
            return
        if not new_block.has_valid_hash():
            print('Invalid hash!')
            return
        #all checks are passed hence add it to blockchain
        self.blockchain.append(new_block)
