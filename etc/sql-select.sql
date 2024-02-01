-- 평균 일일 대여 요금 구하기
-- link : https://school.programmers.co.kr/learn/courses/30/lessons/151136
-- 코드를 입력하세요
SELECT round(AVG(DAILY_FEE)) AS AVERAGE_FEE FROM CAR_RENTAL_COMPANY_CAR WHERE CAR_TYPE="SUV"

-- 재구매가 일어난 상품과 회원 리스트 구하기
-- link : https://school.programmers.co.kr/learn/courses/30/lessons/131536
-- 코드를 입력하세요
SELECT USER_ID, PRODUCT_ID FROM ONLINE_SALE GROUP BY USER_ID, PRODUCT_ID HAVING COUNT(*)>=2 ORDER BY USER_ID ASC, PRODUCT_ID DESC

-- 오프라인/온라인 판매 데이터 통합하기
-- link : https://school.programmers.co.kr/learn/courses/30/lessons/131537
-- 코드를 입력하세요
SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT 
FROM ONLINE_SALE
WHERE SALES_DATE BETWEEN "2022-03-01" AND "2022-03-31"
UNION ALL 
SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE, PRODUCT_ID, NULL AS USER_ID, SALES_AMOUNT 
FROM OFFLINE_SALE 
WHERE SALES_DATE BETWEEN "2022-03-01" AND "2022-03-31"
ORDER BY SALES_DATE ASC, PRODUCT_ID ASC, USER_ID ASC

-- 아픈 동물 찾기
-- link : https://school.programmers.co.kr/learn/courses/30/lessons/59036
-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION="Sick" ORDER BY ANIMAL_ID

-- 젊은 동물 찾기
-- link : https://school.programmers.co.kr/learn/courses/30/lessons/59037
-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION!="Aged" ORDER BY ANIMAL_ID

