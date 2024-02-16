import datetime as d
import hashlib as h

class Block:
  def __init__(self, index, timestamp, hash, data):
    self.index = index
    self.timestamp = timestamp
    self.phash = hash
    self.data = data
    self.hash = self.blockhash()
  def blockhash(self): 
    return h.blake2b((str(self.index)+str(self.timestamp)+str(self.phash)+str(self.data)).encode("utf-8")).hexdigest()
  @staticmethod 
  def genesis(): 
    return Block(0, d.datetime.now(), " ", "genesis block")
  @staticmethod 

  def nblock(pblock, data): 
    index = pblock.index + 1
    timestamp = d.datetime.now()
    phash = pblock.hash
    data = "Transaction bundle: {}".format(str(data))
    return Block(index, timestamp, phash, data)

blockchain = [Block.genesis()]
pblock = blockchain[-1]

transactions = ["from:A, to:B, amount:10", "from:C, to:D, amount:12", "from:A, to:C, amount:15", "from:C, to:B, amount:22", "from:B, to:A, amount:18"]
for i in transactions:
  blockchain.append(Block.nblock(blockchain[-1], i))
for i in blockchain:
  print("index: {}\ntimestamp: {}\nprevious hash: {}\ncurrent hash: {}\ndata: {}\n".format(i.index, i.timestamp, i.phash, i.hash, i.data))