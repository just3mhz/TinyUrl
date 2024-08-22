from base64 import b64encode
from base64 import b64decode


_std_alphabet = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
_alphabet = b'TQqtblDjGXwF7kEJi4<CvYshLda8uBV0c9AfUZRpPox6M>yHz3WgmINenrSK15O2'

_encode_translation = bytes.maketrans(_std_alphabet, _alphabet)
_decode_translation = bytes.maketrans(_alphabet, _std_alphabet)


def encode(value: int) -> str:
    bytes_ = value.to_bytes(length=8, byteorder='big')
    bytes_ = bytes_.lstrip(b'\0')
    return b64encode(bytes_)\
        .strip(b'=')\
        .translate(_encode_translation)\
        .decode()


def decode(value: str) -> int:
    return int.from_bytes(b64decode(value.translate(_decode_translation) + '=='))
