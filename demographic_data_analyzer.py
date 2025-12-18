import pandas as pd

def calculate_demographic_data(print_data=True):
    # Cargar el dataset
    df = pd.read_csv('adult.data.csv')  # Asegúrate de tener el CSV en la misma carpeta

    # 1. Número de personas de cada raza
    race_count = df['race'].value_counts()

    # 2. Edad media de los hombres
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Porcentaje de personas con Bachelors
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 4. Porcentaje de personas con educación avanzada ganando >50K
    advanced_education = ['Bachelors', 'Masters', 'Doctorate']
    higher_education = df[df['education'].isin(advanced_education)]
    higher_education_rich = round((higher_education['salary'] == '>50K').mean() * 100, 1)

    # 5. Porcentaje de personas sin educación avanzada ganando >50K
    lower_education = df[~df['education'].isin(advanced_education)]
    lower_education_rich = round((lower_education['salary'] == '>50K').mean() * 100, 1)

    # 6. Número mínimo de horas trabajadas por semana
    min_work_hours = df['hours-per-week'].min()

    # 7. Porcentaje de personas que trabajan el mínimo de horas y ganan >50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage_min_workers = round((num_min_workers['salary'] == '>50K').mean() * 100, 1)

    # 8. País con mayor porcentaje de personas que ganan >50K
    country_salary = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack().fillna(0)
    country_salary['>50K'] = country_salary.get('>50K', 0) * 100  # convertir a porcentaje
    highest_earning_country = country_salary['>50K'].idxmax()
    highest_earning_country_percentage = round(country_salary['>50K'].max(), 1)

    # 9. Ocupación más popular para quienes ganan >50K en India
    india_high_income = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_high_income['occupation'].value_counts().idxmax()

    # Mostrar resultados
    if print_data:
        print("Número de personas por raza:\n", race_count)
        print("Edad media de los hombres:", average_age_men)
        print("Porcentaje con Bachelors:", percentage_bachelors)
        print("Porcentaje con educación avanzada ganando >50K:", higher_education_rich)
        print("Porcentaje sin educación avanzada ganando >50K:", lower_education_rich)
        print("Número mínimo de horas trabajadas por semana:", min_work_hours)
        print("Porcentaje de ricos que trabajan el mínimo:", rich_percentage_min_workers)
        print("País con mayor porcentaje de ricos:", highest_earning_country, highest_earning_country_percentage)
        print("Ocupación más popular para ricos en India:", top_IN_occupation)

    # Retornar resultados como diccionario
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage_min_workers': rich_percentage_min_workers,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

# Si se ejecuta directamente, mostrar resultados
if __name__ == "__main__":
    calculate_demographic_data()

