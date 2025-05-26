from gensim.models.word2vec import Word2Vec


def compute_similarity(model, word1, word2):
    """
    word1과 word2의 similarity를 구하는 함수
    :param model: word2vec model
    :param word1: 첫 번째 단어
    :param word2: 두 번째 단어
    :return: model에 따른 word1과 word2의 cosine similarity
    """
    try:
        # model.wv.similarity() 메서드를 사용하여 두 단어의 유사도를 계산합니다.
        similarity = model.wv.similarity(word1, word2)
    except KeyError as e:
        # 모델의 어휘집에 없는 단어가 있을 경우 오류를 처리합니다.
        print(f"Error: Word '{e}' not found in the model's vocabulary.")
        similarity = None # 단어가 없으면 None을 반환
    return similarity


def get_word_by_calculation(model, word1, word2, word3):
    """
    단어 벡터들의 연산 결과 추론하는 함수
    연산: word1 - word2 + word3
    :param model: word2vec model
    :param word1: 첫 번째 단어로 연산의 시작
    :param word2: 두 번째 단어로 빼고픈 단어
    :param word3: 세 번째 단어로 더하고픈 단어
    :return: 벡터 계산 결과에 가장 알맞는 단어
    """
    try:
        # positive 인자에는 더할 단어들을, negative 인자에는 뺄 단어들을 리스트로 전달합니다.
        # topn=1은 가장 유사한 단어 하나만 반환하도록 합니다.
        results = model.wv.most_similar(positive=[word1, word3], negative=[word2], topn=1)
        # most_similar는 (단어, 유사도) 튜플의 리스트를 반환하므로, 첫 번째 튜플의 단어만 추출합니다.
        output_word = results[0][0]
    except KeyError as e:
        # 계산에 사용되는 단어 중 모델의 어휘집에 없는 단어가 있을 경우 오류를 처리합니다.
        print(f"Error: One of the words '{e}' is not in the vocabulary for calculation.")
        output_word = None # 단어가 없으면 None을 반환
    return output_word


def main():
    # 학습된 word2vec model을 불러옵니다.
    model = Word2Vec.load('/Users/jamie/Desktop/NLP-practice-main/practice3/data/w2v_model')
    
    # 두 단어의 유사도를 찾습니다.
    word1 = "이순신"
    word2 = "원균"
    word1_word2_sim = compute_similarity(model, word1, word2)
    print("{}와/과 {} 유사도: {}".format(word1, word2, word1_word2_sim))
    
    # '대한민국'에서 '서울'을 뺀 후 '런던'을 더하면 어떤 단어가 나올까요?
    word1 = "대한민국"
    word2 = "서울"
    word3 = "런던"
    cal_result = get_word_by_calculation(model, word1, word2, word3)
    print("{} - {} + {}: {}".format(word1, word2, word3, cal_result))

    return word1_word2_sim, cal_result


if __name__ == "__main__":
    main()
