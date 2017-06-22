import hashlib
import os
import blockParameters

class Block():
    '''
    any block looks like
    |----BLOCK---|
    | index      |
    | prev_hash  |
    | timestamp  |
    | data       |
    | hash       |
    |____________|

    the parameters that are to be provided only requires the first 4 fields
    the hash is automatically calculated from the other four fields, hence whenever
    a new block is referenced from outside (other class or function) only the first
    four fields are to be provided
    '''
    def __init__(self,params):
        self.index = params.index
        self.prev_hash = params.prev_hash
        self.timestamp = params.timestamp
        self.data = params.data
        self.hash = self.calc_hash()

    def get_params(self):
        return blockParameters.BlockParameters(
            self.index,
            self.prev_hash,
            self.timestamp,
            self.data
        )

    @classmethod
    def get_genesis_block(cls):
        gen_params = blockParameters.BlockParameters.get_genesis_params()
        return cls(gen_params)

    def calc_hash(self):
        return hashlib.sha256(str(self.get_params()).encode()).hexdigest()

    def has_valid_hash(self):
        return self.hash == self.calc_hash()

    def has_valid_index(self, prev_block):
        return self.index == prev_block.index + 1

    def has_valid_prev_hash(self, prev_block):
        return self.prev_hash == prev_block.hash
