# 데이터 관련 실습 정리

수업에서 작성한 파이썬 실습 파일을 모아둔 저장소입니다.
BMI 데이터를 그래프로 나타내는 실습과 Ridge 회귀로 월드컵 관련 득점 수를 예측하는 실습이 들어 있습니다.

## 파일

1. matplotlib.py : 무작위 키와 몸무게로 BMI를 계산하고 그래프 그리기
2. Ridge.py : Ridge 회귀로 득점 수 예측 및 오차 확인 
3. matplotlib_Ridge_설명.txt : 두 코드에 대한 설명
4. .gitignore : 데이터, 실행 결과, 개인 설정 파일 제외

## 실행

Python과 필요한 라이브러리를 설치한 뒤 실행합니다.

```bash
pip install -r requirements.txt
python matplotlib실습.py
python DS_Ridge.py
```

matplotlib 실습은 그래프 창을 닫으면 다음 그래프가 나옵니다.
무작위 데이터를 사용해서 실행할 때마다 결과가 달라집니다.

Ridge 실습은 같은 폴더에 master_reg.csv가 있어야 합니다.
이 저장소에는 원본 데이터가 포함되어 있지 않아서 데이터 없이 바로 실행할 수는 없습니다.
실행하면 worldcup_goal_predictions.csv에 예측 결과가 저장되고, 터미널에 평가 지표가 출력됩니다.