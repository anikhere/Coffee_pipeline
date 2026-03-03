from sklearn.model_selection import GridSearchCV
from src.constants.constants import SCORE,CV
from src.utils.eval_utils import get_classification_metrics
import mlflow
import dagshub
def trainer(X_train,y_train,models,params,min_score=SCORE,X_test=None,y_test=None):

    # dagshub.init(repo_owner='tahaanik729', repo_name='Coffee_pipeline', mlflow=True)
    # mlflow.set_experiment('coffee_pipeline')
    report = {} 
    yaml_dict = {}
    for model_name,function in models.items():
        grid_search = GridSearchCV(estimator=function, param_grid=params[model_name],cv = CV,scoring ='accuracy')
        grid_search.fit(X_train,y_train)
        best_model = grid_search.best_estimator_
        y_best_pred = best_model.predict(X_train)
        y_test_pred = best_model.predict(X_test) if X_test is not None else None
        metrics = get_classification_metrics(y_test,y_test_pred) if y_test is not None else get_classification_metrics(y_train,y_best_pred)
        best_prams = grid_search.best_params_
        report[model_name] = {
            'best_model': best_model,
            'best_params': best_prams,
            'train_score': get_classification_metrics(y_train,y_best_pred),
            'test_score': metrics  
        }

        yaml_dict[model_name] = {
            'train_score': report[model_name]['train_score'].f1,
            'test_score': report[model_name]['test_score'].f1
        }
        # Track_mlflow (
        #     model=best_model,
        #     model_name=model_name,
        #     params=best_prams,
        #     train_metrics=report[model_name]['train_score'],
        #     test_metrics=metrics,
        #     )
    best_model_name = max(report, key=lambda x: report[x]['test_score'].f1)
    best_model = report[best_model_name]['best_model']
    if report[best_model_name]['test_score'].f1 < min_score:
        raise Exception(f"No model found with f1 score above {min_score}")
    return report,best_model,yaml_dict


# def Track_mlflow(model,model_name,params,train_metrics,test_metrics):
#     with mlflow.start_run(run_name=model_name):
#        mlflow.log_params(params)
#        mlflow.log_metric('train_f1',train_metrics.f1)
#        mlflow.log_metric('test_f1',test_metrics.f1)
#        mlflow.sklearn.log_model(model,model_name)


