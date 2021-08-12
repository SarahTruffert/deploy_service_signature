from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA512
from Crypto.PublicKey import RSA
import base64
 
def sign(msg, privkey):
    """ Returns signature for a message and a key
    Args:
        msg (bytestr): message to sign
        key_pem (bytestr): private key in PEM format
    """

    k = RSA.import_key(privkey)
    signer = pkcs1_15.new(k)
    h = SHA512.new()
    h.update(msg)
    sig = signer.sign(h)
    return base64.b64encode(sig)

def verify(msg, sigb64, pubkey):
    """Verifies signature for a message

    Args:
        msg (bytestr): message
        sigb64 (bytestr): signature in base64
        pubkey (bytestr): public key in PEM format
    """

    sig = base64.decodebytes(sigb64)

    p = RSA.import_key(pubkey)
    verif = pkcs1_15.new(p)
    h = SHA512.new()
    h.update(msg)
    try:
        if verif.verify(h, sig) is None:
            return True
    except ValueError as e:
            return False
    return False