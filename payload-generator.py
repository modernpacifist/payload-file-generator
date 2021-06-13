#!/bin/env python3.9

import binascii

from argparse import ArgumentParser as ap


class NopSlideGenerator:
    def __init__(self, length: int):
        self._length = length
        self._nop_slide = None

        self._generate_slide()

    def _generate_slide(self) -> str:
        self._nop_slide = "\\x90" * self._length

    def get_slide(self):
        return self._nop_slide


class PayloadInserter:
    def __init__(self, nop_slide: str, payload: str, outfile: str):
        self._nop_slide = nop_slide
        self._payload = payload
        self._outfile = outfile
        self._comb_res = None

        self._insert_shellcode()

    def _insert_shellcode(self):
        self._comb_res = self._nop_slide + self._payload

    def get_combined_res(self):
        return self._comb_res


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

    pi = PayloadInserter(nop_slide, args.payload, args.outfile)
    res = pi.get_combined_res()
    print(res)

    if args.outfile:
        with open(args.outfile, "w+") as f:
            f.writelines(res)
