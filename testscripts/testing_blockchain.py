#this is the script to check the blockchain.py file
import unittest
from unittest.mock import MagicMock
import time
import sys,os

#import blockchain..py from src
cwd = os.getcwd()
srcpath = cwd+'/../src'
sys.path.insert(0,srcpath)
import blockchain

class TestBlockchain(unittest.TestCase):
    #need to check only generate_next_block and recv_new_block functions
    def test_generate_new_block(self):
        bchain = blockchain.Blockchain() #this is really a class object which actually contains the blockchain
        old_bchain_len = len(bchain.blockchain)

        data = "this is a new block's data"

        with self.subTest('add new block to blockchain'):
            bchain.generate_next_block(data)
            self.assertEqual(len(bchain.blockchain)-old_bchain_len,1)
            self.assertEqual(bchain.get_latest_block().data, data)

    def test_recv_new_block(self):
        bchain = blockchain.Blockchain()
        old_bchain_len = len(bchain.blockchain)

        #unit testing is really testing an outer layer of the application and hence in order
        #to make process of testing faster and also to ensure that testing does not seep into
        #a great depth but stays only in the outer layer, MOCKING helps, for example if there
        #is an API call in a function(say some HTTPS request), instead of dealing with actual
        #request we can just assume that the server is there to serve the application and
        #start testing the functionality, hence inn unittesting such API calls and onjects should
        #be mocked and tested. I don't want to instansiate the actual blocks to check the blockchian
        #functionality hence I can use MagicMock to mock the blocks and check functionality
        #this actually allows me to not bother making explicitly the blocks with valid/invalid values
        #I can just simulate if blocks are valid in valid by magicmock objects and
        #return value of check functions
        prev_block = MagicMock()
        new_block = MagicMock()
        with self.subTest('newly recieved block is valid and hence should be added'):
            new_block.has_valid_index = MagicMock(return_value=True)
            new_block.has_valid_prev_hash = MagicMock(return_value=True)
            new_block.has_valid_hash = MagicMock(return_value=True)

            bchain.blockchain = [prev_block]
            bchain.recv_new_block(new_block)
            self.assertEqual(len(bchain.blockchain)-old_bchain_len,1)

        with self.subTest('newly received block is invalid and hence should not be added'):
            #any one of them being false is enough to make new_block invalid
            new_block.has_valid_index = MagicMock(return_value=False)
            new_block.has_valid_prev_hash = MagicMock(return_value=False)
            new_block.has_valid_hash = MagicMock(return_value=False)

            bchain.blockchain = [prev_block]
            bchain.recv_new_block(new_block)
            self.assertEqual(len(bchain.blockchain)-old_bchain_len,0)
