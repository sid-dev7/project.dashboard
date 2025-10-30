# Professional Project Dashboard

Fully static and professional dashboard showcasing:

- 10 projects with milestones
- Project timelines (Gantt chart)
- Cost overview
- Resource utilization
- Milestone tracking (Completed/Pending)

## Architecture
CSV Data -> Python scripts -> Plotly charts -> HTML Dashboard -> Deploy to S3

## Run Locally
1. Install dependencies: pip install pandas plotly flask
2. Run backend scripts:
   - python backend/process_data.py
   - python backend/generate_charts.py
3. Optional: preview with Flask: python backend/run_dashboard.py
4. Open dashboard at http://127.0.0.1:5000

## Deploy to AWS S3
- Upload frontend folder to your S3 bucket
- Enable static website hosting
