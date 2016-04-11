# -*- coding: cp936 -*-
from coinkit.keypair import BitcoinKeypair
class vb4(BitcoinKeypair):

    # _pubkeyhash_version_byte=10

    def __init__(self,pubkey_byte):
        BitcoinKeypair._pubkeyhash_version_byte = pubkey_byte
        BitcoinKeypair.__init__(self)

verb4 = vb4(100);
count = 0;
while(verb4.address().upper().find('ZAO')<0):
    count=count+1
    print 'address    '+verb4.address()+'------'+str(count)+'  addressed searched!'
    verb4 = vb4(80);

print 'address    '+verb4.address()
print 'priv key   '+verb4.private_key()
print 'public_key '+verb4.public_key()
