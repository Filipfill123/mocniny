from dialog import SpeechCloudWS, Dialog, ABNF_INLINE
import random
import asyncio
import logging

class Mocniny(Dialog):
    async def main(self):
        HLAS = "Katerina210"
        logging.basicConfig("prdel jako kokot")
        await self.synthesize_and_wait(text="Dobrý den, jsem vaše virtuální mocnina Alžběta Druhá. Stiskněte tlačítko", voice=HLAS)
        while True:
            #self.sc.led_breath_slow()
            await asyncio.sleep(3600)

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(levelname)-10s %(message)s', level=logging.DEBUG)

    SpeechCloudWS.run(Mocniny, address="0.0.0.0", port=8888, static_path="./static", static_route="/(.*)")
