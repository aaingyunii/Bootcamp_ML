# Bootcamp_ML  🦾✍💪
 데이터 엔지니어링 머신러닝 강의 파일, 복습파일들을 저장한 `Repo`

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
2. 해당 경로에 custom 폴더 생성 후 안에 원하는 폰트 설정의 css 파일을 생성한다.<br><br>
3. jupyter notebook 실행 or 새로고침 하여 폰트 변경 적용 확인
<br><br>

# 아나콘다 가상환경 만들어서 쓰는 이유

1. **의존성 관리** 
: 프로젝트 별 독립 환경을 제공하여 패키지 의존성을 관리할 수 있습니다. 여러 프로젝트를 동시에 작업하거나 서로 다른 버전의 패키지를 사용해야 하는 경우, 가상환경을 통해 분리가 가능해집니다.

2. **시스템 호환성**
: 시스템 각각의 요구 사항에 맞는 환경을 구축할 수 있습니다.
Ex) 파이썬 버전이 서로 다른 프로젝트를 진행할 때 분리해서 맞는 환경을 구축해서 진행이 가능.

3. **격리와 안정성**
: 패키지의 설치와 관련된 파일 및 디렉토리를 프로젝트 디렉토리 내에 격리 시켜, 시스템 전체에 영향 없이 개별 프로젝트를 안정적으로 유지할 수 있도록 합니다.

4. **재현성**
: 가상환경을 생성하고 필요한 패키지를 설치하는 과정을 기록해 다른 사람이나 추가 작업을 위한 환경 재현을 쉽게 가능하게 합니다. 이를 통해 협업이나 배포 시에 유용하고, 코드의 이식성과 신뢰성을 향상 시킵니다.
<br>

### ✅ 아나콘다 가상 환경을 만드는 것은 프로젝트 관리, 의존성 관리, 시스템 호환성, 격리와 안정성, 그리고 재현성 을 위해 중요한 도구입니다.
<br><br>


## 아나콘다 가상환경 : matplot 그림 한글 폰트 적용

### 이동 :
`C:\Users\{사용자명}\anaconda3\envs\{가상환경_이름}\Lib\site-packages\matplotlib\mpl-data\`

### 편집
**`matplotlibrc` file** (메모장으로 열람) 
- **`font.family:  malgun gothic`** 으로 변경 or 다른 폰트로도 변경
    - +) font.family 앞 '#' 삭제!
<br>

**그러나,** 이렇게만 하면 '-'(마이너스)가 깨지기 떄문에

<br>

- **`axes.unicode_minus: False`** 로 변경!<br>
    - +) axes.unicode_minus 앞 '#' 삭제<br>
      
### 이것은 각 가상환경의 설정을 건든 것이고, anaconda 의 base를 변경하지 않았다.<br> 따라서 위 설정은 `가상환경 마다 matplotlib` 를 쓴다면 그때마다 설정하면 된다.

<br><br>

## Graphviz 설치 및 가상환경 설정
- 시각화 프로그램, `Diagram` 을 그리는데 사용.
- ex) DecisionTree가 진행되는 과정을 그릴 수 있다.

### [Graphviz](https://graphviz.org/download/) 사이트 접속 :
`graphviz-8.0.5 (64-bit) EXE installer` 다운로드

설치 완료 후
### cmd 관리자 권한으로 실행 : 
`dot -c` 실행


### 아나콘다 명령창에서 가상환경 접속 후 
`pip install graphviz`<br>
그 다음 `Jupyter notebook` 실행

