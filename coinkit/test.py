# -*- coding: cp936 -*-
from coinkit.keypair import BitcoinKeypair
class vb4(BitcoinKeypair):
        _pubkeyhash_version_byte = 70


verb4 = vb4();
print '��ַ:'+verb4.address()
print '˽Կ��'+verb4.private_key()
print '��Կ:\n'+verb4.public_key()
