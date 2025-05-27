from gensim.models import FastText
import pandas as pd

# Emotions dataset for NLP 데이터셋을 불러오는 load_data() 함수입니다.
def load_data(filepath):
    data = pd.read_csv(filepath, delimiter=';', header=None, names=['sentence','emotion'])
    data = data['sentence']

    gensim_input = []
    for text in data:
        # 단어를 소문자로 변환하고 토큰화합니다.
        gensim_input.append(text.lower().rstrip().split())

    return gensim_input

# dummy 데이터셋을 사용하거나, 실제 파일 경로를 지정하세요.
input_data = load_data("/Users/jamie/Desktop/250527/q5/emotions_train.txt")

# fastText 모델을 학습하세요.
# sentences: 학습 데이터, vector_size: 임베딩 벡터의 차원, window: 단어 문맥의 길이,
# min_count: 단어의 최소 발생 빈도, epochs: 학습 횟수
model = FastText(sentences=input_data, vector_size=100, window=3, min_count=1, epochs=10) # min_count를 1로 변경하여 모든 단어가 포함되도록 함


# day와 유사한 단어 10개를 확인하세요.
try:
    similar_day = model.wv.most_similar('day', topn=10)
except KeyError:
    similar_day = "단어 'day'가 단어장에 없습니다. (데이터셋에 충분히 등장하지 않음)"

print(f"Similar to 'day': {similar_day}")

# night와 유사한 단어 10개를 확인하세요.
try:
    similar_night = model.wv.most_similar('night', topn=10)
except KeyError:
    similar_night = "단어 'night'가 단어장에 없습니다. (데이터셋에 충분히 등장하지 않음)"

print(f"Similar to 'night': {similar_night}")

# elllllllice의 임베딩 벡터를 확인하세요.
# fastText는 OOV(미등록 단어) 문제에 강하므로, 단어장에 없어도 벡터를 생성할 수 있습니다.
try:
    wv_elice = model.wv['elllllllice']
except KeyError:
    # fastText는 OOV에 강하므로 KeyError가 발생할 일은 거의 없으나, 예외 처리로 방어
    wv_elice = "단어 'elllllllice'의 벡터를 가져올 수 없습니다. (매우 특이한 상황)"

print(f"Vector for 'elllllllice': {wv_elice}")