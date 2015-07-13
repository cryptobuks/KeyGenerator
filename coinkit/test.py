# -*- coding: cp936 -*-
from coinkit.keypair import BitcoinKeypair
class vb4(BitcoinKeypair):
	_pubkeyhash_version_byte = 80

verb4 = vb4(); 
print '地址:'+verb4.address();
print '私钥：'+verb4.private_key()
print '公钥:\n'+verb4.public_key()
