from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error, r2_score
def metrics(y_test, y_pred):
    return f'\n MAE: {round(mean_absolute_error(y_test, y_pred),3)}||MSE: {round(mean_squared_error(y_test, y_pred),3)}|| RMSE: {round((mean_squared_error(y_test, y_pred))**0.5,3)}|| MAPE: {round((mean_absolute_percentage_error(y_test, y_pred))**0.5 , 3)}|| R^2: {round(r2_score(y_test, y_pred),3)}'

from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import confusion_matrix,classification_report,roc_auc_score
import streamlit as st
from sklearn.model_selection import train_test_split
import pandas as pd
import pickle

st.set_page_config(page_title = "Предсказание")
st.title('Предсказание моделей')

df = pd.read_csv("df_filtered.csv")

def test_model(x, y, model,model_name, transformer = None):
    x = x if not transformer else transformer.fit_transform(x)
    
    x_tr, x_test, y_tr, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42
    )
    if model_name == "PolynomialRegression":
            p = PolynomialFeatures()
            X_test_p = p.fit_transform(x_test)
            y_pred = model.predict(X_test_p)
            return roc_auc_score(y_test,y_pred)
    else:
        y_pred = model.predict(x_test)
        return metrics(y_test, y_pred)

model_name = st.selectbox(
  'Выберите модель машинного обучения', 
  [None,
   "NearestNeighborsClassifier",
   "PolynomialRegression"]
)

def null(x): return x.empty if type(x) is pd.DataFrame else not x 

if model_name and not null(df):
    model = pickle.load(open(f'Labs/Lab1/{model_name}.pickle', 'rb'))
    column = "is_game_center_enabled"
    if column:
        st.markdown('Данные приняты, готовим предсказание')
    
        x, y = df.drop(column,axis=1), df[column]
        
        result = test_model(x,y,model,model_name)
    
        st.markdown('Готово!')
    
        st.markdown(
            f'''
            ### Результаты {model_name}:
            {result}
            '''
        )

    
