import hashlib
class Codec:
    hash_map = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        hash_value = hashlib.sha256(longUrl.encode()).hexdigest()
        url = "http://tinyurl.com/" + hash_value[0:8]
        self.hash_map[url] = longUrl
        return url

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.hash_map[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))