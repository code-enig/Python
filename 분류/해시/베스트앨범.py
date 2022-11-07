from collections import defaultdict
def solution(genres, plays):
    answer = []
    genre_song_dict = defaultdict(list)
    genre_dict = defaultdict(int)
    for i in range(len(plays)):
        genre_song_dict[genres[i]].append([i,plays[i]]) # 장르별 곡별 딕셔너리
        genre_dict[genres[i]] += plays[i] # 장르전체 재생 횟수 딕셔너리

    sorted_genres = sorted(genre_dict.items(), key = lambda x:-x[1]) # 재생 횟수 많은 순으로 정렬
    for genre,plays in sorted_genres:
        if len(genre_song_dict[genre]) == 1: # 곡이 1곡이라면
            answer.append(genre_song_dict[genre][0][0])
            continue
        best_songs = sorted(genre_song_dict[genre], key = lambda x : (-x[1],x[0]))
        print(best_songs)
        answer.extend([number for number, p in best_songs[:2]])
    return answer

genres, plays = ["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]

print(solution(genres, plays))