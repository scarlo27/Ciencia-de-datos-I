# etl.py

import pandas as pd
from db_context import get_mysql_engine

# Configuración de conexión
DB_CONFIG = {
    "user": "sbrito",
    "password": "Sb40222538585",
    "host": "localhost",
    "port": 3306,
    "database": "oulad_db"
}

# Crear conexión
engine = get_mysql_engine(**DB_CONFIG)

# Tablas a cargar
tables = [
    "studentinfo",
    "assessments",
    "vle",
    "studentvle",
    "studentassessment",
    "courses",
    "studentregistration"
]

# Extraer tablas como DataFrames
dataframes = {}
for table in tables:
    print(f"Cargando tabla: {table}")
    df = pd.read_sql_table(table, con=engine)
    dataframes[table] = df

# -------------------------------------------------
# Conversión de columnas ordinales a categóricas
# -------------------------------------------------

# StudentInfo: ordinales
df_students = dataframes["studentinfo"]

ordinal_mappings = {
    "gender_ord": ["F", "M"],
    "region_ord": None, 
    "education_ord": None,
    "imd_band_ord": None,
    "age_band_ord": ["0-35", "35-55", "55<="],
    "disability_ord": ["N", "Y"],
    "final_result_ord": ["Withdrawn", "Fail", "Pass", "Distinction"]
}

for col, categories in ordinal_mappings.items():
    if col in df_students.columns and categories is not None:
        df_students[col] = pd.Categorical(
            df_students[col],
            categories=range(len(categories)),
            ordered=True
        )
        df_students[f"{col}_label"] = pd.Categorical(
            [categories[i] if pd.notna(i) and i < len(categories) else None for i in df_students[col]],
            categories=categories,
            ordered=True
        )

# Assessments: ordinales
df_assessments = dataframes["assessments"]

if "assessment_type_ord" in df_assessments.columns:
    assessment_types = ["CMA", "TMA", "Exam"]
    df_assessments["assessment_type_ord"] = pd.Categorical(
        df_assessments["assessment_type_ord"],
        categories=range(len(assessment_types)),
        ordered=True
    )
    df_assessments["assessment_type_label"] = pd.Categorical(
        [assessment_types[i] if pd.notna(i) and i < len(assessment_types) else None for i in df_assessments["assessment_type_ord"]],
        categories=assessment_types,
        ordered=True
    )

# Reasignar DataFrames convertidos
dataframes["studentInfo"] = df_students
dataframes["assessments"] = df_assessments

# Verifica
print("\nVerificación de columnas categóricas:")
print(df_students[["gender_ord", "gender_ord_label", "final_result_ord", "final_result_ord_label"]].head())
print(df_assessments[["assessment_type_ord", "assessment_type_label"]].head())
