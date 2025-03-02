import tweepy
import random
import os
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

# Twitter API 설정
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")

# Tweepy 인증
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# 📌 랜덤 글귀 데이터 (책에서 랜덤 선택)
quotes = {
    "세이노의 가르침": [
        "진정한 부자는 돈이 아니라 자유를 가진 사람이다.",
        "성공은 스스로를 믿는 사람의 것이다.",
        "작은 습관이 큰 변화를 만든다."
    ],
    "럭키 드로우": [
        "운이 따르는 사람은 포기하지 않는 사람이다.",
        "긍정적인 태도가 기회를 만든다.",
        "성공의 가장 큰 요소는 꾸준함이다."
    ],
    "인간관계론": [
        "진심 어린 관심이 사람을 움직인다.",
        "비판보다는 격려가 더 큰 변화를 만든다.",
        "인간관계에서 가장 중요한 것은 신뢰다."
    ],
    "성공대화론": [
        "말을 잘하는 것보다 중요한 것은 경청하는 것이다.",
        "설득의 핵심은 상대방을 이해하는 것이다.",
        "자신감 있는 말투가 신뢰를 만든다."
    ],
    "자기관리론": [
        "자기관리의 핵심은 작은 습관이다.",
        "꾸준함이 최고의 자산이다.",
        "목표를 시각화하면 동기부여가 지속된다."
    ]
}

# 📌 랜덤 해시태그 리스트
hashtags = [
    "#오늘의글귀", "#자기계발", "#성공습관", "#운명", "#인생조언",
    "#동기부여", "#성장", "#책속의한줄", "#행복", "#도전", "#긍정"
]

# 📌 랜덤 글귀 선택
def get_random_quote():
    book = random.choice(list(quotes.keys()))  # 랜덤 책 선택
    quote = random.choice(quotes[book])  # 랜덤 글귀 선택
    page_number = random.randint(10, 300)  # 랜덤 페이지 번호 생성
    hashtag = random.sample(hashtags, 2)  # 해시태그 2개 선택

    tweet_text = f"{quote}\n\n📌 출처 : P.{page_number} {book}\n🔗 https://thotsnap.tistory.com/\n{' '.join(hashtag)}"
    return tweet_text

# 📌 트윗 게시
def tweet_quote():
    tweet = get_random_quote()
    try:
        api.update_status(tweet)
        print(f"✅ 트윗 완료: {tweet}")
    except Exception as e:
        print(f"❌ 오류 발생: {e}")

# 실행
if __name__ == "__main__":
    tweet_quote()
