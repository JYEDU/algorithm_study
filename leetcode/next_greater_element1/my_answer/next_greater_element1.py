class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        answer=[]
        for i in nums1:
            ind=nums2.index(i)
            if ind==len(nums2)-1:
                answer.append(-1)
            else:
                check=[]
                for j in nums2[ind:]:
                    if i<j:
                        check.append(j)
                if len(check)==0:
                    answer.append(-1)   
                else:
                    answer.append(check[0])
        return answer