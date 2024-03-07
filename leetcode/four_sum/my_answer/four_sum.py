class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 초기 설정
        nums.sort()
        n = len(nums)
        result = []
        # 고정 포인터 1 설정
        for i in range(n - 3):
            # 중복 요소 건너뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 고정 포인터 2 설정
            for j in range(i + 1, n - 2):
                # 중복 요소 건너뛰기
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                # 남은 포인터에 대한 초기 설정 (왼쪽과 오른쪽)
                left = j + 1
                right = n - 1
                # 포인터가 만날 때까지 반복
                while left < right:
                    # 네 요소 합 계산
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    # 조건을 만족하면 결과 리스트에 추가
                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        # 왼쪽과 오른쪽 포인터의 중복 요소 건너뛰기
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        # 포인터 이동
                        left += 1
                        right -= 1
                    # 합이 목표값보다 작은 경우 왼쪽 포인터를 오른쪽으로 이동
                    elif total < target:
                        left += 1
                    # 합이 타겟보다 큰 경우 오른쪽 포인터를 왼쪽으로 이동
                    else:
                        right -= 1
        return result