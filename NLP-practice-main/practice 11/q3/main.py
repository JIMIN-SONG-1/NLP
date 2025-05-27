from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import nltk # NLTK 데이터를 다운로드하기 위해 임포트합니다.

# NLTK 'punkt' 및 'stopwords' 데이터를 다운로드합니다. 
# 이 코드는 한 번만 실행하면 되며, 이미 다운로드했다면 생략해도 됩니다.
try:
    nltk.data.find('corpora/stopwords')
except nltk.downloader.DownloadError:
    nltk.download('stopwords')
try:
    nltk.data.find('tokenizers/punkt')
except nltk.downloader.DownloadError:
    nltk.download('punkt')


test_sentences = [
    "i have looked forward to seeing this since i first saw it amoungst her work",
    "this is a superb movie suitable for all but the very youngest",
    "i first saw this movie when I was a little kid and fell in love with it at once",
    "i am sooo tired but the show must go on",
]

# 1. NLTK에서 기본적으로 제공되는 영어 stopword를 stopwords 변수에 저장하세요.
# set()을 사용하여 검색 속도를 높입니다.
stopwords = set(stopwords.words('english'))

print(f"기본 Stopwords 개수: {len(stopwords)}")
# print(f"기본 Stopwords 예시: {list(stopwords)[:10]}") # 너무 많으므로 일부만 출력

# 2. new_keywords 리스트에 저장되어 있는 신규 stopword들을 1번에서 정의한 stopwords 변수에 추가하여 updated_stopwords에 저장해주세요.
new_keywords = ['noone', 'sooo', 'thereafter', 'beyond', 'amoungst', 'among']
# 기존 stopword set에 새로운 키워드들을 추가합니다.
updated_stopwords = stopwords.union(new_keywords) 
# 또는 updated_stopwords = stopwords.copy(); updated_stopwords.update(new_keywords)

print(f"\n업데이트된 Stopwords 개수: {len(updated_stopwords)}")
# print(f"업데이트된 Stopwords 예시 (새로운 키워드 포함): {list(updated_stopwords)[-10:]}") # 일부만 출력

# 3. test_sentences 내 각 문장을 단어 기준으로 토큰화 해주세요. 
# 토큰화를 수행하면서 stopword에 해당되는 단어는 제거하고, 각 문장별 결과를 tokenized_word 리스트에 추가하세요.
tokenized_word = []

for sentence in test_sentences:
    # 문장을 소문자로 변환 (일관된 처리를 위해 권장)
    sentence = sentence.lower() 
    # word_tokenize를 통해 단어 토큰화 수행
    tokens = word_tokenize(sentence)
    
    # stopword에 해당되지 않는 단어만 필터링하여 리스트에 추가
    filtered_tokens = [word for word in tokens if word not in updated_stopwords]
    tokenized_word.append(filtered_tokens)

print(f"\n토큰화 및 Stopword 제거 결과:\n{tokenized_word}")

# 4. PorterStemmer를 사용하여 토큰화된 test_sentences가 들어 있는 tokenized_word의 첫 문장에 stemming을 수행하고 결과를 stemmed_sent 리스트에 추가하세요.
stemmed_sent = []
stemmer = PorterStemmer()

# tokenized_word의 첫 번째 문장(리스트)에 대해 stemming 수행
first_sentence_tokens = tokenized_word[0]
for word in first_sentence_tokens:
    stemmed_sent.append(stemmer.stem(word))

print(f"\n첫 번째 문장 Stemming 결과:\n{stemmed_sent}")