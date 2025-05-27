import pandas as pd
from gensim.models import Word2Vec

def load_data(filepath):
    data = pd.read_csv(filepath, delimiter=';', header=None, names=['sentence','emotion'])
    data = data['sentence']

    gensim_input = []
    for text in data:
        gensim_input.append(text.rstrip().split())
    return gensim_input

input_data = load_data("/Users/jamie/Desktop/250527/q4/emotions_train.txt")

# word2vec 모델을 학습하세요.
model = Word2Vec(sentences=input_data, vector_size=300, window=2, epochs=10)


# happy와 유사한 단어를 확인하세요.
try:
    similar_happy = model.wv.most_similar('happy', topn=10)
except KeyError:
    similar_happy = "단어 'happy'가 단어장에 없습니다."

print(f"Similar to 'happy': {similar_happy}")

# sad와 유사한 단어를 확인하세요.
try:
    similar_sad = model.wv.most_similar('sad', topn=10)
except KeyError:
    similar_sad = "단어 'sad'가 단어장에 없습니다."
print(f"Similar to 'sad': {similar_sad}")


# 단어 good과 bad의 임베딩 벡터 간 유사도를 확인하세요.
try:
    similar_good_bad = model.wv.similarity('good', 'bad')
except KeyError:
    similar_good_bad = "단어 'good' 또는 'bad' 중 하나 이상이 단어장에 없습니다."

print(f"Similarity between 'good' and 'bad': {similar_good_bad}")

# 단어 sad과 lonely의 임베딩 벡터 간 유사도를 확인하세요.
try:
    similar_sad_lonely = model.wv.similarity('sad', 'lonely')
except KeyError:
    similar_sad_lonely = "단어 'sad' 또는 'lonely' 중 하나 이상이 단어장에 없습니다."
print(f"Similarity between 'sad' and 'lonely': {similar_sad_lonely}")

# happy의 임베딩 벡터를 확인하세요.
# model.wv['단어'] : 특정 단어의 임베딩 벡터를 직접 가져옵니다.
try:
    wv_happy = model.wv['happy']
except KeyError:
    wv_happy = "단어 'happy'가 단어장에 없습니다."

print(f"Vector for 'happy': {wv_happy}")