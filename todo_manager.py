import heapq
import time

class Task:
    """
    Represents a task in the to-do list.
    
    Attributes:
        priority (int): The priority of the task. Lower numbers indicate higher priority.
        description (str): A description of the task.
        timestamp (float): The time the task was created. Used as a tie-breaker for tasks with the same priority.
    """
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        # Store the current time to handle ties in priority. 
        # If two tasks have the same priority, the one added first (smaller timestamp) will be popped first.
        self.timestamp = time.time()

    def __lt__(self, other):
        """
        Overloads the less-than operator (<) to compare two Task objects.
        This is crucial for the heapq module, which uses < to compare elements and maintain the heap property.
        """
        if self.priority == other.priority:
            # If priorities are equal, compare timestamps (First-In, First-Out for same priority)
            return self.timestamp < other.timestamp
        # Otherwise, compare based on priority (lower value means higher priority)
        return self.priority < other.priority

    def __repr__(self):
        """
        Returns a string representation of the Task, useful for printing.
        """
        return f"Task(priority={self.priority}, description='{self.description}')"

class PriorityToDoList:
    """
    Manages a list of tasks using a Min-Heap (Priority Queue).
    """
    def __init__(self):
        # Initialize an empty list to store the heap.
        # Python's heapq module operates on a regular list.
        self.min_heap = []

    def add_task(self, description, priority):
        """
        Adds a new task to the priority queue.
        
        Args:
            description (str): Description of the task.
            priority (int): Priority level (e.g., 1 for high, 3 for low).
        """
        new_task = Task(description, priority)
        # heapq.heappush(heap, item) pushes the value item onto the heap, maintaining the heap invariant.
        # This is an O(log n) operation.
        heapq.heappush(self.min_heap, new_task)
        print(f"Added: {new_task}")

    def view_next_task(self):
        """
        Peeks at the highest priority task without removing it.
        """
        if not self.min_heap:
            print("No tasks in the list.")
            return None
        
        # The smallest element (highest priority) is always at index 0 of the heap list.
        # This is an O(1) operation.
        next_task = self.min_heap[0]
        print(f"Next task up: {next_task}")
        return next_task

    def complete_task(self):
        """
        Removes and returns the highest priority task from the queue.
        """
        if not self.min_heap:
            print("No tasks to complete.")
            return None
        
        # heapq.heappop(heap) pops and returns the smallest item from the heap.
        # It also rearranges the remaining elements to maintain the heap property.
        # This is an O(log n) operation.
        completed_task = heapq.heappop(self.min_heap)
        print(f"Completed: {completed_task}")
        return completed_task

    def show_all_tasks(self):
        """
        Displays all tasks currently in the queue.
        Note: The order in the list `self.min_heap` is not necessarily sorted entirely,
        but it satisfies the heap property (parent <= children).
        To view them in sorted order without removing them, we make a copy and sort it.
        """
        if not self.min_heap:
            print("To-Do List is empty.")
            return

        print("\nCurrent To-Do List (Sorted by Priority):")
        # Creating a sorted copy for display purposes only. O(n log n).
        # We don't want to pop from the actual heap here.
        sorted_tasks = sorted(self.min_heap)
        for task in sorted_tasks:
            print(f"  - [{task.priority}] {task.description}")
        print()

def main():
    print("--- Priority Queue To-Do List Demo ---\n")
    todo = PriorityToDoList()

    # Adding tasks with different priorities
    # Priority 1: High, 2: Medium, 3: Low
    todo.add_task("Fix critical bug in production", 1)
    todo.add_task("Write documentation", 3)
    todo.add_task("Refactor codebase", 2)
    todo.add_task("Respond to emails", 2) # Same priority as Refactor, should act based on timestamp
    todo.add_task("Server maintenance", 1) # Another high priority task

    # Display current state
    todo.show_all_tasks()

    # View the next highest priority task
    todo.view_next_task()
    print("-" * 30)

    # Complete tasks one by one
    print("Completing tasks...")
    todo.complete_task() # Should be "Fix critical bug..." or "Server maintenance" depending on insertion order/tie-breaker? 
                         # Actually, standard binary heap doesn't guarantee stability for equal keys unless we handle it.
                         # Our Task class handles ties using timestamp, making it stable!
    
    todo.view_next_task()
    todo.complete_task()
    
    todo.show_all_tasks()

    todo.complete_task()
    todo.complete_task()
    todo.complete_task()
    
    # Try to complete from empty list
    todo.complete_task()

if __name__ == "__main__":
    main()
