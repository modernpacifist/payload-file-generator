#!/bin/env python3.9

import binascii

from argparse import ArgumentParser as ap


class NopSlideGenerator:
    def __init__(self, length: int):
        self._length = length
        self._nop_slide = None

        self._generate_slide()

    def _generate_slide(self) -> bytes:
        self._nop_slide = b'\x90' * self._length

    def get_slide(self):
        return self._nop_slide


class PayloadInserter:
    def __init__(self, nop_slide: bytes, shellcode: bytes):
        self._nop_slide = nop_slide
        self._payload = shellcode
        self._comb_res = None

        self._insert_shellcode()
        self.print_nop()

    def _insert_shellcode(self):
        self._comb_res = self._nop_slide + self._payload

    def print_nop(self):
        # print(repr(self._comb_res)[2:-1])
        print((self._comb_res))


def get_args():
    parser = ap()
    parser.add_argument("-l", "--length", dest="length", type=int, required=True,
                        help="length of the nop slide")
    parser.add_argument("-p", "--payload", dest="payload", type=str, required=True,
                        help="your custom payload in bytes, will be inserted after nop slide")
    parser.add_argument("-o", "--outfile", dest="outfile", type=str, required=False,
                        help="save to file")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()

    nsg = NopSlideGenerator(args.length)
    nop_slide = nsg.get_slide()

    byte_payload = bytes(args.payload, "utf-8")

    hex = args.payload.replace("\\x", "")

    print(hex)
    # print(binascii.hexlify(hex))

    # PayloadInserter(nop_slide, bytes.fromhex(hex))

    # print(codecs.decode(str_payload, "hex_codec"))
