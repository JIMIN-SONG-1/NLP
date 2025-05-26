
import codecs
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter 

# 실습 환경에 미리 설치가 됨
# nltk.download('punkt') # 필요시 주석 해제하여 실행

def count_words(input_text):
    """
    input_text 내 단어들의 개수를 세는 함수
    :param input_text: 텍스트
    :return: dictionary, key: 단어, value: input_text 내 단어 개수
    """
    # 텍스트를 소문자로 변환하여 대소문자 구분을 없앱니다.
    processed_text = input_text.lower()

    # NLTK의 word_tokenize를 사용하여 단어 토큰을 만듭니다.
    words = word_tokenize(processed_text)

    # collections.Counter를 사용하여 각 단어의 개수를 효율적으로 셉니다.
    output_dict = Counter(words)

    # Counter 객체를 일반 파이썬 딕셔너리로 변환하여 반환합니다.
    return dict(output_dict)


def main():
    # 데이터 파일인 'text8_1m_part_aa.txt'을 불러옵니다.
    # 파일 경로가 'data/text8_1m_part_aa.txt'가 맞는지 확인.
    # 만약 'practice1' 폴더 안에 'data' 폴더가 있다면 옳은 경로.
    try:
        with codecs.open("/Users/jamie/Desktop/NLP-practice-main/practice1/data/text8_1m_part_aa.txt", "r", "utf-8") as html_f:
            text8_text = "".join(html_f.readlines())
    except FileNotFoundError:
        print("오류: 'data/text8_1m_part_aa.txt' 파일을 찾을 수 없습니다.")
        print("현재 스크립트 실행 위치에서 'data' 폴더와 파일의 경로가 맞는지 확인해주세요.")
        return {} # 오류 시 빈 딕셔너리 반환

    # 데이터 내 단어들의 개수를 세어봅시다.
    word_dict = count_words(text8_text)

    # 단어 개수를 기준으로 정렬하여 상위 10개의 단어를 출력합니다.
    top_words = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)[:10]
    print(top_words)

    return word_dict


if __name__ == "__main__":
    # NLTK 데이터가 아직 다운로드되지 않았다면 이 부분의 주석을 해제하고 실행하세요.
    # nltk.download('punkt')
    # nltk.download('stopwords') # 불용어 제거를 위해 필요할 수 있습니다.

    main()