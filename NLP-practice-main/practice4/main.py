from gensim.models.fasttext import FastText
import gensim


def compute_similarity(model, word1, word2):
    """
    word1과 word2의 similarity를 구하는 함수
    :param model: fastText model
    :param word1: 첫 번째 단어
    :param word2: 두 번째 단어
    :return: model에 따른 word1과 word2의 cosine similarity
    """
    # <ToDo>: model에 따른 word1과 word2의 cosine similarity를 계산하세요.
    try:
        # FastText 모델도 Word2Vec과 마찬가지로 .wv.similarity() 메서드를 사용합니다.
        similarity = model.wv.similarity(word1, word2)
    except KeyError as e:
        print(f"Error: Word '{e}' not found in the model's vocabulary. FastText can handle OOV, but sometimes this error occurs if the word is severely malformed or very rare.")
        similarity = None
    return similarity


def get_word_by_calculation(model, word1, word2, word3):
    """
    단어 벡터들의 연산 결과 추론하는 함수
    연산: word1 - word2 + word3
    :param model: fastText model
    :param word1: 첫 번째 단어로 연산의 시작
    :param word2: 두 번째 단어로 빼고픈 단어
    :param word3: 세 번째 단어로 더하고픈 단어
    :return: 벡터 계산 결과에 가장 알맞는 단어
    """
    # <ToDo>: model을 이용하여 word1 - word2 + word3 결과에 가장 근접한 단어를 찾으세요.
    try:
        # FastText 모델도 Word2Vec과 마찬가지로 .wv.most_similar() 메서드를 사용합니다.
        results = model.wv.most_similar(positive=[word1, word3], negative=[word2], topn=1)
        output_word = results[0][0] # (단어, 유사도) 튜플 리스트에서 단어만 추출
    except KeyError as e:
        print(f"Error: One of the words '{e}' is not in the vocabulary for calculation. FastText can handle OOV, but for vector arithmetic, it's better if the base words are known.")
        output_word = None
    return output_word


def get_similar_word_from_oov(model, word1):
    """
    단어가 Out of Vocabulary(OOV)인 경우 그와 유사한 단어를 추론하여 찾는 함수
    만약 단어가 OOV가 아닌 경우 원래 단어를 반환함
    :param model: fastText model
    :param word1: 입력 단어
    :return: 알맞은 단어
    """
    # <ToDo>: model을 이용하여 word1의 단어를 찾으세요. 만약 model의 사전에 없는 단어라면 근접한 단어를 찾으세요.
    # FastText는 OOV 단어에 대해서도 벡터를 생성할 수 있습니다.
    # 특정 단어가 모델의 어휘집에 있는지 확인하려면 `model.wv.key_to_index`를 사용할 수 있습니다.
    
    # 단어가 어휘집에 있다면 그대로 반환
    if word1 in model.wv.key_to_index:
        output_word = word1
    else:
        # 단어가 어휘집에 없다면, 해당 단어의 벡터를 기반으로 가장 유사한 단어를 찾습니다.
        # FastText는 서브워드 정보를 활용하여 OOV 단어의 벡터를 생성합니다.
        # gensim 4.0.0부터 .wv.most_similar()는 OOV 단어도 자동으로 벡터화하여 처리합니다.
        # 따라서 별도의 OOV 처리 로직 없이 바로 most_similar을 호출할 수 있습니다.
        try:
            # 해당 단어 자체의 벡터를 구한 후, 이 벡터와 가장 유사한 단어를 찾습니다.
            # OOV 단어는 `model.wv[word1]`처럼 직접 벡터를 얻을 수 있습니다.
            # 그리고 이 벡터와 가장 유사한 단어를 `most_similar`로 찾을 수 있습니다.
            # 하지만 더 간단하게는 `model.wv.most_similar(word1, topn=1)`을 사용해도 OOV 처리됩니다.
            # 여기서는 명확한 OOV 처리 로직을 위해 해당 단어의 벡터를 먼저 얻고, 그 벡터와 가장 유사한 단어를 찾도록 구현합니다.
            word_vector = model.wv[word1] # OOV여도 FastText는 벡터를 생성
            similar_words = model.wv.most_similar(positive=[word_vector], topn=1)
            output_word = similar_words[0][0]
        except Exception as e: # 단어 형태가 너무 이상하여 벡터 생성조차 안되는 경우
            print(f"Error processing OOV word '{word1}': {e}")
            output_word = None

    return output_word


def main():
    # 학습된 fasttext model의 경로를 적습니다.
    model_path = '/Users/jamie/Desktop/NLP-practice-main/practice4/pratice4_data/fasttext_model'
    
    # 학습된 fasttext model을 불러옵니다.
    # 파일이 해당 경로에 있는지 다시 한번 확인해주세요!
    try:
        model = FastText.load(model_path)
    except Exception as e:
        print(f"Error loading FastText model from {model_path}: {e}")
        print("Please ensure the 'fasttext_model' file exists in the specified 'data' directory.")
        return # 모델 로드 실패 시 함수 종료

    # 두 단어의 유사도를 찾습니다.
    word1 = "이순신"
    word2 = "원균"
    word1_word2_sim = compute_similarity(model, word1, word2)
    print("{}와/과 {} 유사도: {}".format(word1, word2, word1_word2_sim))
    
    # '대통령'에서 '현대'를 뺀 후 '고대'를 더하면 어떤 단어가 나올까요?
    word1 = "대통령"
    word2 = "현대"
    word3 = "고대"
    cal_result = get_word_by_calculation(model, word1, word2, word3)
    print("{} - {} + {}: {}".format(word1, word2, word3, cal_result))
    
    # '컴퓨터'라는 단어를 fasttext가 알고 있는지 확인합니다.
    oov_word_known = "컴퓨터"
    oov_word_result_known = get_similar_word_from_oov(model, oov_word_known)
    if oov_word_known == oov_word_result_known:
        print("단어 '{}'는 fastText가 알고 있음".format(oov_word_known))
    else:
        print("{}와 근접한 단어: {}".format(oov_word_known, oov_word_result_known))
    
    # '캄퓨터'라는 단어는 오타이지만 사람은 '컴퓨터'임을 알 수 있습니다. 
    # 이를 기계도 알게 만들려면 fasttext를 어떻게 사용하면 될까요?
    oov_word_typo = "캄퓨터"
    oov_word_result_typo = get_similar_word_from_oov(model, oov_word_typo)
    if oov_word_typo == oov_word_result_typo:
        print("단어 '{}'는 fastText가 알고 있음".format(oov_word_typo))
    else:
        print("{}와 근접한 단어: {}".format(oov_word_typo, oov_word_result_typo))

    # 최종 반환 값은 실습 가이드에 맞춰 수정합니다.
    return word1_word2_sim, cal_result, oov_word_result_typo


if __name__ == "__main__":
    main()