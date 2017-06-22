#this is the script to check the block.py file
import unittest
import time
import sys,os

#import block.py and blockParameters.py from src
cwd = os.getcwd()
srcpath = cwd+'/../src'
sys.path.insert(0,srcpath)
import block,blockParameters

class TestBlock(unittest.TestCase):
    #In a blockchain timestamp and data of a block are really quite independent
    #of other blocks hence we need to test the other fields of the block
    def test_valid_index(self):
        prev_block = create_block(0, '0', int(time.time()), 'first block')

        with self.subTest('valid index'):
            new_block = create_block(1, '0', int(time.time()), 'second block')
            self.assertTrue(new_block.has_valid_index(prev_block))
        with self.subTest('invalid index'):
            new_block = create_block(2, '0', int(time.time()), 'second block')
            self.assertFalse(new_block.has_valid_index(prev_block))
    def test_prev_hash(self):
        prev_block = create_block(0, '0', int(time.time()), 'first block')
        prev_hash = prev_block.hash

        with self.subTest('valid previous hash'):
            new_block = create_block(1, prev_hash, int(time.time()), 'second block')
            self.assertTrue(new_block.has_valid_prev_hash(prev_block))
        with self.subTest('invalid previous hash'):
            new_block = create_block(1, '0', int(time.time()), 'second block')
            self.assertFalse(new_block.has_valid_prev_hash(prev_block))
    def test_hash(self):
        with self.subTest('valid hash'):
            new_block = create_block(0, '0', int(time.time()), 'first block')
            self.assertTrue(new_block.has_valid_hash())
        with self.subTest('invalid hash'):
            new_block = create_block(0, '0', int(time.time()), 'first block')
            #tampering the hash
            new_block.hash = "tampered hash"
            self.assertFalse(new_block.has_valid_hash())

def create_block(index, prev_hash, timestamp, data):
    new_block_params = blockParameters.BlockParameters(
        index, prev_hash, timestamp, data
    )
    new_block = block.Block(new_block_params)
    return new_block

if __name__ == '__main__':
    unittest.main()
