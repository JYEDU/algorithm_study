import pandas as pd

def solution(data, ext, val_ext, sort_by):
    '''
    data:  ["코드 번호(code)", "제조일(date)", "최대 수량(maximum)", "현재 수량(remain)"]
    ext: 비교 기준 요소
    val_ext: 비교 값 (해당 값보다 작아야 함)
    sort_by: 오름차순 정렬 기준 요소
    '''
    df=pd.DataFrame(data, columns=["code", "date", "maximum", "remain"])
    new_df = df[df[ext]<val_ext]
    new_df = new_df.sort_values(sort_by)
    return new_df.values.tolist()