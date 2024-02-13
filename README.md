# Optimal-job-interview-scheduling
A solution to calculate the maximum number of interviews a person can attend based on the given schedule.


## Task overview
The task is to develop a REST API endpoint that processes POST requests containing two lists: start times and end times of job interviews. The goal is to calculate the maximum number of non-overlapping interviews a person can attend, considering that transitioning from one interview to another requires no time if the next interview starts exactly at or after the previous one ends.


## Prerequisites
Install Django: "pip install django"


## Testing
1. Open Terminal and navigate to skai-labs-task-3/optimal_interview_scheduling/
2. Run command: python manage.py runserver
3. Open another Terminal and run command "python send_post_request.py"
4. Check the output and see the received response based on the data defined in the send_post_request.py file
