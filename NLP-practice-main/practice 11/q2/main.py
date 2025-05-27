import re

word_counter = dict()
regex = re.compile('[^a-zA-Z]') # 알파벳(a-z, A-Z)이 아닌 모든 문자를 찾기 위한 정규표현식

# 텍스트 파일을 소문자로 변환 및 숫자 및 특수기호를 제거한 딕셔너리를 만드세요.
with open('/Users/jamie/Desktop/250527/q2/text.txt', 'r') as f: # 'text.txt' 파일을 읽기 모드('r')로 엽니다.
    for line in f: # 파일의 각 줄을 순회합니다.
        # 1. 모든 리뷰를 소문자 처리
        lower_line = line.lower()
        
        # 2. 단어 내 알파벳을 제외한 모든 숫자 및 특수기호 제거
        # regex.sub('', 문자열)을 사용하여 알파벳이 아닌 모든 문자를 제거합니다.
        cleaned_line = regex.sub('', lower_line)
        
        # 3. 전처리가 완료된 단어와 단어의 빈도수를 word_counter 딕셔너리에 저장
        words = cleaned_line.split() # 공백을 기준으로 문자열을 단어 리스트로 분리합니다.
        for word in words: # 분리된 각 단어를 순회합니다.
            # 딕셔너리에 단어가 이미 있으면 해당 단어의 빈도수를 1 증가시키고,
            # 없으면 새로 추가하며 빈도수를 1로 초기화합니다.
            word_counter[word] = word_counter.get(word, 0) + 1


# 단어 "the"의 빈도수를 확인해 보세요.
# word_counter 딕셔너리에서 'the' 단어의 빈도수를 가져옵니다. 
# 만약 'the'가 딕셔너리에 없으면 기본값인 0을 반환합니다.
count = word_counter.get('the', 0) 

print(count)