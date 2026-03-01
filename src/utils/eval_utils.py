from sklearn.metrics import f1_score,recall_score,precision_score
from src.config.artifacts import Classification_metrics
def get_classification_metrics(y_true,y_pred):
    f1 = f1_score(y_true,y_pred)
    recall = recall_score(y_true,y_pred)
    precision = precision_score(y_true,y_pred)
    classsify = Classification_metrics(f1=f1, precision=precision, recall=recall)  # ✅
    return classsify