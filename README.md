# To-Do List with Priority Queue

A Python application that manages a to-do list using a **Min-Heap (Priority Queue)**. This ensures that tasks with the highest priority (lowest numerical value) are always processed first.

## features

- **Priority Management**: Tasks are ordered by priority level (1 = Highest, 3 = Lowest).
- **Time-Based Tie-Breaking**: If two tasks have the same priority, the one added earlier is processed first (FIFO for same-priority tasks).
- **Efficient Operations**: Uses Python's `heapq` module for $O(\log n)$ insertions and deletions.
- **Task Class**: Custom class with string representation and comparison logic.

## Logic Overview

The core logic relies on the Heap Data Structure.

- **Min-Heap Property**: In a min-heap, for any given node $I$, the value of $I$ is less than or equal to the values of its children. This means the smallest element (highest priority) is always at the root.
- **Comparison Logic (`__lt__`)**:
  - First, compare `priority` values.
  - If priorities are equal, compare `timestamp` values.
  - This ensures stability: `Task(priority=1, time=100) < Task(priority=1, time=101)`.

## Data Structure Analysis

| Operation | Description | Time Complexity |
| :--- | :--- | :--- |
| **Add Task** | Push a new task onto the heap. | $O(\log n)$ |
| **View Next** | Peek at the root of the heap (index 0). | $O(1)$ |
| **Complete Task** | Pop the root element and re-heapify. | $O(\log n)$ |
| **Sort/Display** | Create a sorted copy of the heap to view all. | $O(n \log n)$ |

## Usage

1. **Clone the repository** (if applicable) or download `todo_manager.py`.
2. **Run the script**:
   ```bash
   python todo_manager.py
   ```

### Example Code

```python
todo = PriorityToDoList()

# Add tasks
todo.add_task("Fix critical bug", 1)  # High Priority
todo.add_task("Write documentation", 3) # Low Priority

# Get next task
next_task = todo.view_next_task() 
# Output: Task(priority=1, description='Fix critical bug')

# Complete task
todo.complete_task()
```

## Implementation Details

The project is contained in `todo_manager.py`.

- **`Task` Class**: Stores `priority`, `description`, and `timestamp`. Implements `__lt__` for sorting.
- **`PriorityToDoList` Class**: Encapsulates the `min_heap` list and provides methods for interacting with the queue using `heapq`.

## Requirements

- Python 3.x
- Standard libraries: `heapq`, `time`
