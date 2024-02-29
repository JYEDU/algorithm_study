class Solution(object):
    def numberOfWeakCharacters(self, properties):
        """
        The Number of Weak Characters in the Game
        link: https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/description/

        :type properties: List[List[int]]
        :rtype: int
        """
        num_characters = len(properties)
        properties.sort(key=lambda x: (-x[0], x[1]))  # 공격력 내림차순, 방어력 오름차순 정렬
        
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