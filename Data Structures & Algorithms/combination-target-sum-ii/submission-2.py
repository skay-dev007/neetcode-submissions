class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = set()
        candidates = sorted(candidates)
        def rec(pos, curr_path, curr_sum):
            if curr_sum > target:
                return 
            if curr_sum == target:
                self.res.add(tuple(curr_path[:]))
            if pos == len(candidates):
                return 
            
            
            #not included 
            rec(pos+1,curr_path,curr_sum)
            #included 
            curr_path.append(candidates[pos])
            rec(pos+1, curr_path, curr_sum + candidates[pos])
            curr_path.pop()
        
        rec(0,[],0)
        return [list(ele) for ele in self.res]

        