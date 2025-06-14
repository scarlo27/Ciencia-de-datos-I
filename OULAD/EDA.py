import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from db_context import get_mysql_engine
import numpy as np

# Configuración de conexión
DB_CONFIG = {
    "user": "sbrito",
    "password": "Sb40222538585",
    "host": "localhost",
    "port": 3306,
    "database": "oulad_db"
}

# Crear carpeta de salida si no existe
os.makedirs("output", exist_ok=True)

# Conexión
engine = get_mysql_engine(**DB_CONFIG)

# Cargar datos
df_students = pd.read_sql_query("SELECT * FROM studentinfo", engine)
df_assessments = pd.read_sql_query("SELECT * FROM assessments", engine)

# ------------------------------------
# Conversión de ordinales a categorías
# ------------------------------------
final_result_labels = ["Withdrawn", "Fail", "Pass", "Distinction"]
df_students["final_result_ord_label"] = pd.Categorical(
    [final_result_labels[i] if pd.notna(i) and i < len(final_result_labels) else None
     for i in df_students["final_result_ord"]],
    categories=final_result_labels,
    ordered=True
)

assessment_type_labels = ["CMA", "TMA", "Exam"]
df_assessments["assessment_type_label"] = pd.Categorical(
    [assessment_type_labels[i] if pd.notna(i) and i < len(assessment_type_labels) else None
     for i in df_assessments["assessment_type_ord"]],
    categories=assessment_type_labels,
    ordered=True
)

# ------------------------------------
# 1. Matriz de correlación
# ------------------------------------
# Selección numérica y cálculo de correlación
corr = df_students.select_dtypes(include="number").corr()

# Gráfico ajustado
plt.figure(figsize=(12, 10))
sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    annot_kws={"size": 8}
)
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.title("Matriz de Correlación - studentinfo", fontsize=14)
plt.tight_layout()
plt.savefig("OULAD\\Imagenes\\matriz_correlacion.png")
plt.clf()

# ------------------------------------
# 2. Matriz de confusión (simulada)
# ------------------------------------
y_true = df_students["final_result_ord"]
y_pred = df_students["final_result_ord"].sample(frac=1.0, random_state=1)
cm = confusion_matrix(y_true, y_pred, labels=[0, 1, 2, 3])
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=final_result_labels)
disp.plot()
plt.title("Matriz de Confusión (simulada)")
plt.tight_layout()
plt.savefig("OULAD\\Imagenes\\matriz_confusion.png")
plt.clf()

# ------------------------------------
# 3. Boxplot: IMD vs Resultado
# ------------------------------------
if "imd_band_ord" in df_students.columns:
    sns.boxplot(
        x="final_result_ord_label",
        y="imd_band_ord",
        data=df_students
    )
    plt.title("IMD Band vs Resultado Final")
    plt.tight_layout()
    plt.savefig("OULAD\\Imagenes\\boxplot_imd_vs_resultado.png")
    plt.clf()

# ------------------------------------
# 4. Campana de Gauss: promedio de notas
# ------------------------------------
df_scores = pd.read_sql_query("SELECT * FROM studentassessment", engine)
sns.histplot(
    df_scores["score"],
    kde=True,
    bins=30,
    color="skyblue",
    stat="count"
)

plt.xlabel("Puntaje del estudiante")
plt.ylabel("Cantidad de observaciones")
plt.title("Distribución de Calificaciones - Campana de Gauss")

# Reducir la densidad de etiquetas en el eje X
min_score = int(df_scores["score"].min())
max_score = int(df_scores["score"].max())
plt.xticks(np.arange(min_score, max_score + 1, 10))  # cada 10 puntos

plt.tight_layout()
plt.savefig("OULAD\\Imagenes\\campana_gauss_notas.png")
plt.clf()

# ------------------------------------
# 5. Gráfico de dispersión: peso vs fecha
# ------------------------------------

df_assessments = pd.read_sql_query("SELECT * FROM assessments", engine)

# Limpieza de columna 'date'
df_assessments["date"] = pd.to_numeric(df_assessments["date"], errors="coerce")
df_assessments = df_assessments.dropna(subset=["date"])
df_assessments["date"] = df_assessments["date"].astype(int)



# Filtrar evaluaciones con peso mayor a 0
df_assessments = df_assessments[df_assessments["weight"] > 0]

# Gráfico
sns.scatterplot(
    x="weight",
    y="date",
    hue="assessment_type", 
    data=df_assessments
)

# Ajustar eje Y 
min_date = df_assessments["date"].min()
max_date = df_assessments["date"].max()
plt.yticks(np.arange(min_date, max_date + 1, 30))

plt.xlabel("Peso (%)")
plt.ylabel("Día en la presentación del módulo")
plt.title("Dispersión: Peso vs Fecha de Evaluación")
plt.tight_layout()
plt.savefig("OULAD\\Imagenes\\dispersion_weight_vs_date.png")
plt.clf()

# ------------------------------------
# 6. Extra: Distribución de estudiantes por edad y género
# ------------------------------------
if "gender_ord" in df_students.columns and "age_band_ord" in df_students.columns:
    sns.countplot(x="age_band_ord", hue="gender_ord", data=df_students)
    plt.title("Distribución por Edad y Género")
    plt.tight_layout()
    plt.savefig("OULAD\\Imagenes\\distribucion_edad_genero.png")
    plt.clf()
