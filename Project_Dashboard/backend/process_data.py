import pandas as pd
import json

projects = pd.read_csv('../data/sample_data.csv')
projects['Milestones'] = projects['Milestones'].apply(json.loads)
for idx, row in projects.iterrows():
    completed = sum(1 for m in row['Milestones'] if m['status']=='Completed')
    total = len(row['Milestones'])
    projects.at[idx,'Milestone_Completion_%'] = round(completed/total*100,2)
projects.to_csv('../data/sample_data.csv', index=False)
