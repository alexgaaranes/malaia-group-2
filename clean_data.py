import pandas as pd
import re

# Read data
try:
    liyab = pd.read_csv('liyab.csv')
except FileNotFoundError:
    print(f"Error: The file liyab.csv was not found. Please check the path.")
    liyab = pd.DataFrame()

if not liyab.empty:
    # Clean 'What was your role?'
    role_col = 'What was your role?'
    if role_col in liyab.columns:
        liyab['Cleaned Role'] = liyab[role_col].astype(str).str.lower().str.strip()
        role_map = {
            r'.*software engineer.*': 'Software Engineer',
            r'.*developer.*': 'Developer',
            r'.*analyst.*': 'Analyst',
            r'.*consultant.*': 'Consultant',
            r'.*engineer.*': 'Engineer',
            r'.*manager.*': 'Manager',
            r'.*specialist.*': 'Specialist',
            r'.*assistant.*': 'Assistant',
            r'.*associate.*': 'Associate',
            r'.*researcher.*': 'Researcher',
            r'.*teacher.*': 'Teacher',
            r'.*instructor.*': 'Instructor',
            r'.*professor.*': 'Professor',
            r'.*officer.*': 'Officer',
            r'.*designer.*': 'Designer',
            r'.*writer.*': 'Writer',
            r'.*editor.*': 'Editor',
            r'.*planner.*': 'Planner',
            r'.*coordinator.*': 'Coordinator',
            r'.*architect.*': 'Architect',
            r'.*auditor.*': 'Auditor',
            r'.*accountant.*': 'Accountant',
            r'.*supervisor.*': 'Supervisor',
            r'.*lead.*': 'Lead',
            r'.*head.*': 'Head',
            r'.*intern.*': 'Intern',
            r'.*trainee.*': 'Trainee'
        }
        temp_role_values = liyab['Cleaned Role'].copy()
        for pattern, standard_name in role_map.items():
            mask = temp_role_values.str.contains(pattern, regex=True, case=False, na=False)
            temp_role_values[mask] = standard_name
        liyab['Cleaned Role'] = temp_role_values

    # Clean 'Did you negotiate your job offer?'
    negotiate_col = 'Did you negotiate your job offer?'
    if negotiate_col in liyab.columns:
        liyab['Cleaned Negotiation'] = liyab[negotiate_col].astype(str).str.lower().str.strip()
        negotiate_map = {
            'yes': 'Yes',
            'no': 'No',
            'i tried but they did not budge': 'No'
        }
        liyab['Cleaned Negotiation'] = liyab['Cleaned Negotiation'].map(negotiate_map).fillna('No')

    # Save cleaned data
    liyab.to_csv('liyab_cleaned.csv', index=False)
    print("Cleaned data saved to liyab_cleaned.csv")
