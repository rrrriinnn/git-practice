import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("master_reg.csv")

# 피처 타겟 분리
X = df.drop(columns=["team", "total_qual_goals", "log_qual_goals"])
y = df["log_qual_goals"]

# 가이드라인 기준 80/20 랜덤 분리
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# StandardScaler를 이용한 스케일링 진행
Scaledstandard = StandardScaler()
X_train_s = Scaledstandard.fit_transform(X_train)
X_test_s = Scaledstandard.transform(X_test)


# Ridge 모델 학습
model = Ridge(alpha=1.0)
model.fit(X_train_s, y_train)

# 전체 데이터에 대한 예측 실행
X_all_s = Scaledstandard.transform(X)
y_pred_all_log = model.predict(X_all_s)

# 로그(sqrt) 스케일 예측값을 원래 골 수(제곱)로 역변환
y_pred_all_goals = y_pred_all_log**2

# 결과용 데이터프레임
result = df[["team", "total_qual_goals"]].copy()

# 소수점 첫째 자리까지 반올림하여 대입
result["predicted_qual_goals"] = np.round(y_pred_all_goals, 1)

# 오차 계산
result["prediction_error"] = np.round(
    result["predicted_qual_goals"] - result["total_qual_goals"], 1
)

# 결과를 새로운 CSV 파일로 내보내기
outputfile = "worldcup_goal_predictions.csv"
result.to_csv(outputfile, index=False)
print("\n모든 국가의 예측 결과가 '{outputfile}' 파일로 저장되었습니다.")

# 모델 성능 검증 (Evaluation)
y_pred_test_log = model.predict(X_test_s)
y_pred_test_goals = y_pred_test_log**2
y_test_goals = y_test**2

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

rmse = np.sqrt(mean_squared_error(y_test_goals, y_pred_test_goals))
mae = mean_absolute_error(y_test_goals, y_pred_test_goals)
r2 = r2_score(y_test_goals, y_pred_test_goals)

print("========== MODEL EVALUATION ==========")
print(f"RMSE: {rmse:.2f}골 오차")
print(f"MAE: {mae:.2f}골 오차")
print(f"R² Score: {r2:.4f}")
print("======================================")
