class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        print(candidates)
        def backtrack(sums: int,combinations: List[int], pos, fresh):
            print(combinations, sums, pos)
            if sums > target:
                print("exceeded")
                return
            if sums == target:
                print("appended")
                res.append(combinations.copy())
            for i in range(pos,len(candidates),1):
                if i > 0 and candidates[i] == candidates[i-1] and not fresh:
                    continue
                fresh = False
                combinations.append(candidates[i])
                backtrack(sums + candidates[i], combinations, i +1, True)
                combinations.pop()


        backtrack(0,[],0, True)

        return res