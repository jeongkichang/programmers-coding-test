import heapq

def solution(jobs):
    # 요청 시점 순으로 정렬
    jobs.sort()
    # 현재 시간, 대기 시간, 완료된 작업 수
    current_time, total_waiting_time, completed_jobs = 0, 0, 0
    # 작업 대기열 (힙 사용)
    waiting_jobs = []
    job_index = 0
    num_jobs = len(jobs)

    while completed_jobs < num_jobs:
        # 현재 시간까지 요청된 모든 작업을 대기열에 추가
        while job_index < num_jobs and jobs[job_index][0] <= current_time:
            heapq.heappush(waiting_jobs, (jobs[job_index][1], jobs[job_index][0]))
            job_index += 1
        
        if waiting_jobs:
            # 대기열에서 소요 시간이 가장 짧은 작업을 가져옴
            job_duration, job_request_time = heapq.heappop(waiting_jobs)
            # 현재 시간을 업데이트 (작업이 끝난 시간)
            current_time += job_duration
            # 해당 작업의 요청부터 종료까지의 시간
            total_waiting_time += current_time - job_request_time
            completed_jobs += 1
        else:
            # 대기 중인 작업이 없으면, 다음 작업의 요청 시간으로 점프
            if job_index < num_jobs:
                current_time = jobs[job_index][0]
    
    # 평균 대기 시간을 계산 (소수점 이하 버림)
    return total_waiting_time // num_jobs
