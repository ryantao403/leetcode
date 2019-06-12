#
# @lc app=leetcode id=726 lang=python3
#
# [726] Number of Atoms
#
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        self.pos = 0
        lookup = self.process(formula)
        keys = sorted(list(lookup.keys()))
        return "".join(map(lambda key: key+(str(lookup[key]) if lookup[key] >1 else ""), keys))

    def process(self, formula):
        lookup = collections.defaultdict(int)
        while self.pos < len(formula):
            if formula[self.pos] == "(":
                self.pos += 1
                temp_lookup = self.process(formula)

                i, j = self.pos, self.pos+1
                while j < len(formula) and formula[j].isdigit():
                    j += 1
                factor = int(formula[i:j])

                for element in temp_lookup:
                    lookup[element] += temp_lookup[element] * factor
                self.pos = j
            elif formula[self.pos] == ")":
                self.pos += 1
                return lookup
            elif formula[self.pos].isupper():
                i, j = self.pos, self.pos+1
                while j < len(formula) and formula[j].islower():
                    j += 1
                elem = formula[i:j]
                self.pos = j
                if self.pos < len(formula) and formula[self.pos].isdigit():
                    i, j = self.pos, self.pos+1
                    while j < len(formula) and formula[j].isdigit():
                        j += 1
                    count = int(formula[i:j])
                    lookup[elem] += count
                    self.pos = j
                else:
                    lookup[elem] += 1
        return lookup

            

