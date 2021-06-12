#!/bin/env python3.9

from argparse import ArgumentParser as ap


class NopSlideGenerator:
    def __init__(self, length: int):
        self._length = length

    def generate_slide(self) -> bytes:
        return b'\x90' * self._length


class PayloadGenerator:
    def __init__(self, nop_slide: str):
        self._nop_slide = nop_slide

    def print_nop(self):
        return repr(self._nop_slide)[2:-1]

        # self._generate_nop_slide()
        # self._get_nop_slide()

    # def _generate_nop_slide(self):
        # self._nop_slide = b'\x90' * self.length

    # def _get_nop_slide(self):
        # print(repr(self._nop_slide)[2:-1])


def get_args():
    parser = ap()
    parser.add_argument("-l", "--length", dest="length", type=int, required=True,
                        help="length of the nop slide")
    parser.add_argument("-p", "--payload", dest="payload", type=str, required=False,
                        help="your custom payload in bytes, will be inserted after nop slide")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()

    nsg = NopSlideGenerator(args.length)

    nop_slide = nsg.generate_slide()

    pg = PayloadGenerator(nop_slide)
    print(pg.print_nop())
