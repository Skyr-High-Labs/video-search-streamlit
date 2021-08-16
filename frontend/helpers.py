from typing import Any
import Algorithmia

class AlgoHelper():
    def __init__(self, api_key) -> None:
        
        self.client = Algorithmia.client(api_key)
        self.algo = self.client.algo('videosearch/colabenvironment/5.0.5')
        self.algo.set_options(timeout=300)  # optional
    def __call__(self, input, *args: Any, **kwds: Any) -> Any:
        return self.algo.pipe(input).result


def addTimestampToYoutubeURL(url, seconds):
    return url + "&t=" + str(seconds)
