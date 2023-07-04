# Bootcamp_ML  🦾✍💪
 데이터 엔지니어링 머신러닝-딥러닝 강의 파일, 복습파일

<br><br>
# Jupyter notebook 환경 설정
### 아나콘다 가상환경 설치 및 실행
**IN Anaconda prompt**
```
conda create -n ml python=3.10
...

conda activate ml

conda info -e  # 설치된 가상환경 확인
```

## 가상환경 내 라이브러리 설치
```
pip install notebook matplotlib pandas scikit-learn

# workspace 이동 및 주피터 노트북 실행
jupyter notebook
```



## Jupyter notebook 폰트 변경 방법

1. 로컬 C 드라이브 내 `.jupyter` 폴더를 찾는다.<br><br>
![image](https://github.com/aaingyunii/230629_ML_01/assets/31847834/d1f2de98-5c92-4e74-97bd-20289a65c1bd)
<br>
2. 해당 경로에 custom 폴더 생성 후 안에 원하는 폰트 설정의 css 파일을 생성한다.<br><br>
3. jupyter notebook 실행 or 새로고침 하여 폰트 변경 적용 확인
