# Add Two Numbers

두 정수 X, Y의 임의의 자리에서 공통으로 나타나는 정수 k(0 ≤ k ≤ 9)들을 이용하여 만들 수 있는 가장 큰 정수를 두 수의 짝꿍이라 합니다(단, 공통으로 나타나는 정수 중 서로 짝지을 수 있는 숫자만 사용합니다). 

X, Y의 짝꿍이 존재하지 않으면, 짝꿍은 -1입니다. 

X, Y의 짝꿍이 0으로만 구성되어 있다면, 짝꿍은 0입니다.

두 정수 X, Y가 주어졌을 때, X, Y의 짝꿍을 return하는 solution 함수를 완성해주세요.



## Example 1:

<b>Input:</b> X="100", Y="2345"

<b>Output:</b> "-1"

<b>Explanation:</b> X, Y의 짝꿍은 존재하지 않습니다. 따라서 "-1"을 return합니다.

## Example 2:

<b>Input:</b> X="100", Y="203045"

<b>Output:</b> "0"

<b>Explanation:</b> X, Y의 공통된 숫자는 0으로만 구성되어 있기 때문에, 두 수의 짝꿍은 정수 0입니다. 따라서 "0"을 return합니다.

## Example 3:

<b>Input:</b> X="100", Y="123450"

<b>Output:</b> "10"

<b>Explanation:</b> X, Y의 짝꿍은 10이므로, "10"을 return합니다.

## Example 4:

<b>Input:</b> X="12321", Y="42531"

<b>Output:</b> "321"

<b>Explanation:</b> X, Y의 짝꿍은 321입니다. 따라서 "321"을 return합니다.

## Example 5:

<b>Input:</b> X="5525", Y="1255"

<b>Output:</b> "552"

<b>Explanation:</b> X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 2, 5, 5로 만들 수 있는 가장 큰 정수인 552입니다

## Example 6:

<b>Input:</b> X="3403", Y="13203"

<b>Output:</b> "330"

<b>Explanation:</b> X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 3, 0, 3으로 만들 수 있는 가장 큰 정수인 330입니다. 



## Constraints:

- 3 ≤ X, Y의 길이(자릿수) ≤ 3,000,000입니다.
- X, Y는 0으로 시작하지 않습니다.
- X, Y의 짝꿍은 상당히 큰 정수일 수 있으므로, 문자열로 반환합니다.

## Category
- 

## Reference
- [programmers](https://school.programmers.co.kr/learn/courses/30/lessons/131128)