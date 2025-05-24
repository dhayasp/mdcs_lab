import heapq
import time


class DataStreamScheduler:
    def __init__(self):
        self.queue = []  # Priority queue to store requests

    def schedule_request(self, request, priority):
        """Schedule a new request"""
        heapq.heappush(self.queue, (priority, time.time(),
                       request))  # Fixed parenthesis

    def process_requests(self):
        """Process requests in priority order"""
        while self.queue:
            priority, _, request = heapq.heappop(self.queue)
            print(f"Processing request: {request}")


# Example usage
if __name__ == "__main__":
    scheduler = DataStreamScheduler()
    scheduler.schedule_request("Data stream request 1", priority=3)
    scheduler.schedule_request("Data stream request 2", priority=1)
    scheduler.schedule_request("Data stream request 3", priority=2)
    scheduler.process_requests()
