#!/bin/env python3.9

from argparse import ArgumentParser as ap


class PayloadGenerator:
    def __init__(self, length: int, outfile: str):
        self._length = length
        self._nop_slide = None
        self._outfile = outfile

        self.generate_nop_slide()

    def generate_nop_slide(self):
        self._nop_slide = b'\x90' * self._length

        print(repr(self._nop_slide)[2:-1])

    def _save_to_file(self):
        if self._outfile:
            with open(self._outfile) as f:
                f.write(self._nop_slide)


def get_args():
    parser = ap()
    parser.add_argument("-l", "--length", dest="length", type=int, required=True,
                        help="length of the nop slide")
    parser.add_argument("-o", "--outfile", dest="outfile", type=str, required=False,
                        help="file to dump payload to")
    parser.add_argument("-p", "--payload", dest="payload", type=str, required=False,
                        help="your custom payload in bytes, will be inserted after nop slide")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()

    pg = PayloadGenerator(args.length, args.outfile)
