from typing import Any
import Algorithmia
import Secrets

class AlgoHelper():
    def __init__(self) -> None:
        
        self.client = Algorithmia.client(Secrets.ECHO_ALGORITHMIA_API_KEY)
        self.algo = self.client.algo('videosearch/colabenvironment/5.0.5')
        self.algo.set_options(timeout=300)  # optional
    def __call__(self, input, *args: Any, **kwds: Any) -> Any:
        return self.algo.pipe(input).result


def addTimestampToYoutubeURL(url, seconds):
    return url + "&t=" + str(seconds)
