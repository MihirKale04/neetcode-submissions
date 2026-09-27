class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupedAnagrams = defaultdict(list)

        for string in strs:
            charCount = [0] * 26
            for ch in string:
                charCount[ord(ch) - ord("a")] += 1
            groupedAnagrams[tuple(charCount)].append(string)
        return groupedAnagrams.values()

        