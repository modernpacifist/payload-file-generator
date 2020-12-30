class PayloadFileGenerator:
    def __init__(self, filename: str, nop_slide_length: int, payload: str):
        self.filename = filename
        self.nop_slide_length = nop_slide_length
        self.payload = payload
        self.nop_slide = None
        self._generate_nop_slide()

    def _generate_nop_slide(self):
        self.nop_slide = b"\x90" * self.nop_slide_length

    def generate_payload_file(self):
        with open(f"{self.filename}.payload", "wb") as f:
            f.write(self.nop_slide + bytes(self.payload, "utf-8"))
