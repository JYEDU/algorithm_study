class Solution(object):
    def numberOfWeakCharacters(self, properties):
        """
        :type properties: List[List[int]]
        :rtype: int
        """
        num_characters = len(properties)
        # 공격력 내림차순, 방어력 오름차순 정렬
        properties.sort(key=lambda x: (-x[0], x[1]))
        
        max_defense = float('-inf')
        weak_count = 0
        
        for i in range(num_characters):
            _, defense_i = properties[i]
            # 이전 캐릭터보다 방어력이 작은 경우, 약한 캐릭터로 간주
            if defense_i < max_defense:
                weak_count += 1
            else:
                max_defense = defense_i
        
        return weak_count