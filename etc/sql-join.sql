-- 주문량이 많은 아이스크림들 조회하기
-- link : https://school.programmers.co.kr/learn/courses/30/lessons/133027
-- 코드를 입력하세요
SELECT A.FLAVOR
FROM FIRST_HALF A LEFT JOIN JULY B ON A.FLAVOR=B.FLAVOR
GROUP BY FLAVOR
ORDER BY SUM(A.TOTAL_ORDER+B.TOTAL_ORDER) DESC
LIMIT 3

-- 없어진 기록 찾기
-- link : https://school.programmers.co.kr/learn/courses/30/lessons/59042
-- 코드를 입력하세요
SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_OUTS O
LEFT JOIN ANIMAL_INS I ON O.ANIMAL_ID = I.ANIMAL_ID
WHERE I.ANIMAL_ID IS NULL
ORDER BY O.ANIMAL_ID;

