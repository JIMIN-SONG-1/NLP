# 단어가 key, 빈도수가 value로 구성된 딕셔너리 변수를 만드세요.
word_counter = dict()

with open('text.txt', 'r') as f:
    for line in f:
        # 줄 끝의 개행문자 제거 후 공백 기준으로 단어 분리
        words = line.rstrip().split()
        # 각 단어의 빈도수 카운트
        for word in words:
            word_counter[word] = word_counter.get(word, 0) + 1

# 텍스트 파일에 내 모든 단어의 총 빈도수를 구해보세요.
total = sum(word_counter.values())

# 텍스트 파일 내 100회 이상 발생하는 단어를 리스트 형태로 저장하세요.
up_five = [word for word, count in word_counter.items() if count >= 100]

print(total)
print(up_five)