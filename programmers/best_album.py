    '''
    베스트앨범
    link : https://school.programmers.co.kr/learn/courses/30/lessons/42579
    '''

def solution(genres, plays):
    # 각 장르의 총 재생 횟수를 저장하는 딕셔너리 생성
    # genre : total number of plays
    total_plays_by_genre = {}

    # 각 장르별로 노래의 정보를 저장하는 딕셔너리 생성 
    # genre : (index, number of plays)
    songs_by_genre = {}

    # 입력으로 주어진 genres와 plays를 기반으로 딕셔너리 생성
    for i in range(len(genres)):
        genre = genres[i]
        play_count = plays[i]

        # total_plays_by_genre 업데이트
        if genre in total_plays_by_genre:
            total_plays_by_genre[genre] += play_count
        else:
            total_plays_by_genre[genre] = play_count

        # songs_by_genre 업데이트
        if genre in songs_by_genre:
            songs_by_genre[genre].append((i, play_count))
        else:
            songs_by_genre[genre] = [(i, play_count)]

    # total_plays_by_genre를 기준으로 장르 정렬
    sorted_genres = sorted(total_plays_by_genre.keys(), key=lambda x: total_plays_by_genre[x], reverse=True)

    # 결과를 저장할 리스트
    result = []

    # 각 장르별로 노래 정렬 후 결과에 추가
    for genre in sorted_genres:
        songs = sorted(songs_by_genre[genre], key=lambda x: (x[1], -x[0]), reverse=True)
        result.extend([song[0] for song in songs[:2]])  # 각 장르별로 최대 2개의 노래 추가

    return result