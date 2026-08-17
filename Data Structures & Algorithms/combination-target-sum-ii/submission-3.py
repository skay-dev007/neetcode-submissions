class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        candidates = sorted(candidates)
        def rec(pos, curr_path, curr_sum):
            if curr_sum > target:
                return 
            if curr_sum == target:
                self.res.append(curr_path[:])
    
            for i in range(pos,len(candidates)):
                if i > pos and candidates[i] == candidates[i-1]:
                    continue 

                curr_path.append(candidates[i])
                rec(i+1, curr_path, curr_sum + candidates[i])
                curr_path.pop()
        
        rec(0,[],0)
        return [list(ele) for ele in self.res]

        