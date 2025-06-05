import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('us_presidents.csv')

# Display first rows
print(df.head())

# Clean columns
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Convert dates to datetime
df['birth_date'] = pd.to_datetime(df['birth_date'])
df['inauguration_date'] = pd.to_datetime(df['inauguration_date'])

# Q1: Average age at inauguration
df['age_at_inauguration'] = (df['inauguration_date'] - df['birth_date']).dt.days // 365
avg_age = df['age_at_inauguration'].mean()
print(f'Average age at inauguration: {avg_age:.2f} years')

# Q2: Political party with most years in office
party_years = df.groupby('party')['years_in_office'].sum().sort_values(ascending=False)
print(party_years)

# Q3: Most common birth states
birth_state_counts = df['birth_state'].value_counts()
print(birth_state_counts.head(10))

# Q4: Age at inauguration over time
sns.lineplot(data=df.sort_values('inauguration_date'), x='inauguration_date', y='age_at_inauguration')
plt.title('Presidents\' Age at Inauguration Over Time')
plt.xlabel('Inauguration Year')
plt.ylabel('Age at Inauguration')
plt.show()

# Q5: Presidents who served more than one term
multi_term = df[df['terms'] > 1]
print(f'{len(multi_term)} presidents served more than one term')
