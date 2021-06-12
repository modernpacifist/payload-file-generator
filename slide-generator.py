#!/bin/env python3.9

from argparse import ArgumentParser as ap


class PayloadGenerator:
    def __init__(self, length: int, outfile: str):
        self._length: int = length
        self._nop_ramp: str = None
        self._outfile: str = outfile

        self.generate_nop_ramp()

    def generate_nop_ramp(self):
        self._nop_ramp = repr(b'\x90' * self._length)[2:-1]

        print(self._nop_ramp)

    # def _get_ramp(self):
        # if self._outfile:
            # with open(self._outfile) as f:
                # f.write(self._nop_ramp)


def get_args():
    parser = ap()
    parser.add_argument("-l", "--length", dest="length", type=int, required=True,
                        help="length of the nop slide")
    parser.add_argument("-o", "--outfile", dest="outfile", type=str, required=False,
                        help="file to dump payload to")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()

    pg = PayloadGenerator(args.length, args.outfile)
