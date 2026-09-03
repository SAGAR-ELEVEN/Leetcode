class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
           
        g.sort()  # sort children by greed factor
        s.sort()  # sort cookies by size
    
        i = 0  # pointer for children (g)
        j = 0  # pointer for cookies (s)
        content_children = 0
    
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                # This cookie satisfies this child!
                content_children += 1
                i += 1  # move to next child
                j+= 1  # move to next cookie
            else:
                # Cookie too small for this child, try a bigger cookie
                j += 1
    
        return content_children

        #satisfaction = 0
        #for i in g:
            #for j in s:
                #if s[j] >= g[i]:
                    #satisfaction += 1
        #return satisfaction