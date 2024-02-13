# Optimal-job-interview-scheduling
A solution to calculate the maximum number of interviews a person can attend based on the given schedule.


## Task overview
The task is to develop a REST API endpoint that processes POST requests containing two lists: start times and end times of job interviews. The goal is to calculate the maximum number of non-overlapping interviews a person can attend, considering that transitioning from one interview to another requires no time if the next interview starts exactly at or after the previous one ends.


## Project Setup:
The project is structured using Django's framework, with a separate app (interview_scheduling) containing the views for the API endpoint.


## API Endpoint (views.py):
- The main functionality is implemented in the calculate_max_interviews view.
- This view is also decorated with @api_view(['POST']) to define it as a view that supports POST requests. While this may not be strictly necessary in Django, it's often used in Django REST Framework to define API views explicitly.
- The view expects a POST request with JSON data containing lists of start times and end times of job interviews.
- It calculates the maximum number of non-overlapping interviews a person can attend using an efficient algorithm.
- The algorithm iterates through the sorted interview times, keeping track of the current end time and updating the maximum count of interviews attended.
- Finally, it returns a JSON response containing the maximum number of interviews a person can attend without any overlap.


## Prerequisites
Install Django: "pip install django"


## Testing
1. Open Terminal and navigate to skai-labs-task-3/optimal_interview_scheduling/
2. Run command: python manage.py runserver
3. Open another Terminal and run command "python send_post_request.py"
4. Check the output and see the received response based on the data defined in the send_post_request.py file
