

import matplotlib.pyplot as plt
from sklearn.metrics import (confusion_matrix,
                             ConfusionMatrixDisplay,
                             recall_score,
                             accuracy_score,
                             precision_score,
                             f1_score)

# confusion matrix 시각화
def plot_confusion_matrix(y, pred, title=None):
    """
    confusion matrix 시각화
    [parameter]
        y: ndarray - 정답
        pred: ndarray - 모델 추정한 label
        title: str - 그래프의 제목
    """
    cm = confusion_matrix(y,pred)
    disp = ConfusionMatrixDisplay(cm)
    disp.plot(cmap="Greys")
    
    if title :
        plt.title(title)
    plt.show()
    
def print_metrics_classification(y,pred,title = None):
    """
    분류 결과에 대한 평가지표를 출력하는 함수.
    출력 내용 : accuracy, recall, precision, f1 score
    [parameter]
        y: ndarray - 정답
        pred: ndarray - 모델 추정한 label
        title: str - 그래프의 제목
    """
    if title:
        print(f"================={title}=================")
    print("정확도 Accuracy : ", accuracy_score(y, pred))
    print("재현율 Recall : ", recall_score(y, pred))
    print("정밀도 Precision : ", precision_score(y, pred))
    print("F-1 Score : ", f1_score(y, pred))
