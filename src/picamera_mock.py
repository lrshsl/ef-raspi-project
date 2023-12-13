from typing import Generator


class PiCamera:
    def start_preview(self):
        print('--< [MockPiCamera] Starting Preview >--')

    def capture_continuous(self, filename: str) -> Generator[str, None, None]:
        yield filename

    def capture(self, filename: str, format: str) -> None:
        print(f'--< [MockPiCamera] Capturing to {filename} >--')


class PiRGBArray:
    array: list

    def __init__(self, camera): pass
