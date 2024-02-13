import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def calculate_max_interviews(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        start_times = data.get('start_times', [])
        end_times = data.get('end_times', [])

        if len(start_times) != len(end_times):
            return JsonResponse({'error': 'start_times and end_times must have the same length'}, status=400)
        
        # we sort the interviews by end times
        interviews = sorted(zip(start_times, end_times), key=lambda x: x[1])
        max_interviews = 0
        last_end_time = -1

        for start_time, end_time in interviews:
            if start_time >= last_end_time:
                max_interviews += 1
                last_end_time = end_time

        return JsonResponse({'max_interviews': max_interviews}, status=200)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
