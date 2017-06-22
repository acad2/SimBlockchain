#this is for the first block in the chain (genesis block)
GENESIS_INDEX = 0
GENESIS_PREV_HASH = '0'
GENESIS_TIMESTAMP = '0'
GENESIS_DATA = 'genesis'

class BlockParameters():
    #data is supposed to be in string format
    def __init__(self, index, prev_hash, timestamp, data):
        self.index = index
        self.prev_hash = prev_hash
        self.timestamp = timestamp
        self.data = data

    def __str__(self):
        return (str(self.index)+str(self.prev_hash)+str(self.timestamp) + self.data)

    @classmethod
    #method to return the parameters for the genesis block
    def get_genesis_params(cls):
        return cls(GENESIS_INDEX, GENESIS_PREV_HASH, GENESIS_TIMESTAMP, GENESIS_DATA)
