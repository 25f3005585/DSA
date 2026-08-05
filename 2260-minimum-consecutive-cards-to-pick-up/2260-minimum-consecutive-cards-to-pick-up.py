class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        n = len(cards)
        left = 0
        minimum = float("inf")
        hash_map = {}

        for right in range(n):
            hash_map[cards[right]] = hash_map.get(cards[right], 0) + 1

            while right - left + 1 != len(hash_map):
                minimum = min(right - left + 1,minimum)
                hash_map[cards[left]] -= 1

                if hash_map[cards[left]] == 0:
                    del hash_map[cards[left]]
                
                left +=1

        minimum = minimum if minimum != float("inf") else -1
        return minimum
        

            