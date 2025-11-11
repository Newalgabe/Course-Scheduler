# Course Scheduler - Graph Coloring Project

## Table of Contents

1. [Overview](#overview)
2. [Quick Start](#quick-start)
3. [Theoretical Background](#theoretical-background)
4. [Installation](#installation)
5. [Usage Guide](#usage-guide)
6. [Project Structure](#project-structure)
7. [Algorithm Details](#algorithm-details)
8. [Examples](#examples)
9. [Requirements Checklist](#requirements-checklist)
10. [Testing](#testing)
11. [Troubleshooting](#troubleshooting)
12. [Performance & Limitations](#performance--limitations)
13. [Future Enhancements](#future-enhancements)
14. [References](#references)

---

## Overview

This project implements a **Course Scheduler** using **Graph Coloring** algorithms. The application helps schedule courses into time slots (colors) such that conflicting courses (courses that cannot be scheduled at the same time) are assigned to different time slots.

### Key Features

- ✅ Add courses dynamically
- ✅ Define conflicts between courses
- ✅ Automatic schedule generation using graph coloring
- ✅ Visual representation of time slots with colors
- ✅ Both text-based and GUI interfaces
- ✅ Validation of coloring correctness
- ✅ Statistics display (number of time slots used, courses scheduled)
- ✅ Support for unlimited courses and conflicts

---

## Quick Start

### Installation

No installation required! Just ensure you have Python 3.6 or higher.

**For GUI (Tkinter):**
- **Windows/macOS**: Tkinter is usually included with Python
- **Linux**: Install with `sudo apt-get install python3-tk`

### Running the Application

```bash
python main.py
```

Choose your interface:
- **1** for Text Interface
- **2** for GUI Interface

### Basic Workflow

1. **Add Courses**: Enter course names
2. **Add Conflicts**: Define which courses conflict with each other
3. **Generate Schedule**: Run the graph coloring algorithm
4. **View Results**: See the assigned time slots

### Run Demo

```bash
python demo.py
```

This will run 4 test cases demonstrating the algorithm.

---

## Theoretical Background

### Graph Representation

- **Vertices (Nodes)**: Represent courses
- **Edges**: Represent conflicts between courses (e.g., when the same student must attend both courses)

The graph uses an **Adjacency List** representation for efficient neighbor lookup.

### Graph Coloring Algorithm

**Graph Coloring** assigns a "color" (time slot) to each vertex (course) with the constraint that adjacent vertices (conflicting courses) cannot have the same color.

#### Greedy Algorithm

The project implements a **Greedy Algorithm** for graph coloring:

1. Sort vertices by degree (number of conflicts) in descending order
2. For each vertex, assign the smallest available color that is not used by any of its neighbors
3. This ensures a valid coloring, though not necessarily optimal (minimum number of colors)

#### Complexity

- **Time Complexity**: O(V + E), where V is the number of vertices and E is the number of edges
- **Space Complexity**: O(V + E)
- **Optimality**: The greedy algorithm does not guarantee the minimum number of colors, but provides a valid solution efficiently
- **Note**: Finding the minimum number of colors (chromatic number) is an NP-hard problem

---

## Installation

### Requirements

- Python 3.6 or higher
- Tkinter (for GUI, usually included with Python)

### Setup

1. Clone or download the project
2. No additional packages are required (uses only standard library)

### Platform Support

- **Windows**: ✅ Full support
- **macOS**: ✅ Full support
- **Linux**: ✅ Requires `python3-tk` package for GUI

---

## Usage Guide

### Running the Application

Run the main script to choose between interfaces:

```bash
python main.py
```

Or run interfaces directly:

**Text Interface:**
```bash
python text_interface.py
```

**GUI Interface:**
```bash
python gui_interface.py
```

### Text Interface

The text interface provides a menu-driven system:

```
==================================================
Course Scheduler - Graph Coloring
==================================================
1. Add course
2. Add conflict between courses
3. View all courses
4. View all conflicts
5. Generate schedule (Graph Coloring)
6. View schedule
7. Clear all data
0. Exit
==================================================
```

#### Step-by-Step Usage (Text Interface)

**Step 1: Add Courses**
```
Enter your choice: 1
Enter course name: CS101
Course 'CS101' added successfully!
```

**Step 2: Add Conflicts**
```
Enter your choice: 2
Available courses:
1. CS101
2. CS102
Enter first course number: 1
Enter second course number: 2
Conflict added between 'CS101' and 'CS102'
```

**Step 3: Generate Schedule**
```
Enter your choice: 5
Schedule generated successfully!
Number of time slots used: 2
```

**Step 4: View Schedule**
```
Enter your choice: 6
============================================================
COURSE SCHEDULE
============================================================
Course                          Time Slot       Color Code
------------------------------------------------------------
CS101                           0               ■
CS102                           1               ■
============================================================
Total time slots used: 2
Total courses scheduled: 2
```

### GUI Interface

The GUI interface provides:

- **Course Management Panel**: Add courses, view course list
- **Conflict Management**: Select courses from dropdowns and add conflicts
- **Schedule Display**: Color-coded table showing course assignments
- **Color Legend**: Visual representation of time slot colors
- **Statistics**: Number of time slots used and courses scheduled

#### GUI Features

- Intuitive interface with Entry fields and Comboboxes
- Color-coded time slots for easy visualization
- Real-time updates
- Clear all functionality
- Visual color legend

#### Step-by-Step Usage (GUI Interface)

1. **Add Course**: Type course name in "Course Name" field → Click "Add Course"
2. **Add Conflict**: Select Course 1 and Course 2 from dropdowns → Click "Add Conflict"
3. **Generate Schedule**: Click "Generate Schedule" button
4. **View Results**: Schedule automatically displayed in the table with color coding

---

## Project Structure

```
Project/
│
├── graph_coloring.py      # Core graph data structure and coloring algorithm
├── text_interface.py      # Text-based command-line interface
├── gui_interface.py       # GUI interface using Tkinter
├── main.py               # Main entry point (interface selector)
├── demo.py               # Demonstration script with test cases
├── README.md             # This comprehensive documentation
└── requirements.txt      # Project dependencies
```

### Core Modules

1. **`graph_coloring.py`**
   - Core graph data structure (`Graph` class)
   - Greedy coloring algorithm implementation
   - Validation functions
   - Helper functions for degree calculation and neighbor access

2. **`text_interface.py`**
   - Text-based command-line interface
   - Menu-driven system
   - Course and conflict management
   - Schedule display

3. **`gui_interface.py`**
   - Graphical user interface using Tkinter
   - Visual course management
   - Color-coded schedule display
   - Interactive conflict management

4. **`main.py`**
   - Main entry point
   - Interface selector (Text or GUI)

5. **`demo.py`**
   - Demonstration script
   - Multiple test cases
   - Algorithm validation

---

## Algorithm Details

### Graph Class

The `Graph` class provides:

- `add_vertex(vertex)`: Add a course to the graph
- `add_edge(vertex1, vertex2)`: Add a conflict between two courses
- `get_degree(vertex)`: Get number of conflicts for a course
- `get_neighbors(vertex)`: Get all conflicting courses
- `get_vertices_sorted_by_degree()`: Get courses sorted by number of conflicts

### Greedy Coloring Function

```python
def greedy_coloring(graph):
    """
    Greedy algorithm for graph coloring
    Returns a dictionary mapping vertices to colors (time slots)
    """
    # Sort vertices by degree (largest first)
    vertices_sorted = graph.get_vertices_sorted_by_degree()
    
    # Dictionary to store color assignment
    colors = {}
    
    # Assign colors to vertices
    for vertex in vertices_sorted:
        # Find used colors in neighbors
        used_colors = set()
        for neighbor in graph.get_neighbors(vertex):
            if neighbor in colors:
                used_colors.add(colors[neighbor])
        
        # Find the smallest available color
        color = 0
        while color in used_colors:
            color += 1
        
        colors[vertex] = color
    
    return colors
```

### Validation

The `validate_coloring()` function ensures:
- All vertices are colored
- No adjacent vertices have the same color
- The coloring is correct

### Algorithm Implementation Summary

1. **Graph Representation**: Adjacency List
   - Vertices: Courses
   - Edges: Conflicts between courses

2. **Coloring Algorithm**:
   - Sort vertices by degree (descending)
   - For each vertex, assign smallest available color
   - Ensure no adjacent vertices have same color
   - Return color assignment

3. **Complexity**:
   - **Time**: O(V + E)
   - **Space**: O(V + E)
   - **Optimality**: Not guaranteed (greedy approach)

---

## Examples

### Example 1: Simple Schedule

**Input:**
- Courses: CS101, CS102, MATH201
- Conflicts: CS101 <-> CS102, CS101 <-> MATH201

**Output:**
```
Course          Time Slot    Color Code
----------------------------------------
CS101           0            ■
CS102           1            ■
MATH201         1            ■

Total time slots used: 2
Total courses scheduled: 3
```

### Example 2: Complex Schedule

**Input:**
- Courses: CS101, CS102, MATH201, PHYS101, CHEM101, ENG101
- Conflicts:
  - CS101 <-> CS102
  - CS101 <-> MATH201
  - CS102 <-> PHYS101
  - MATH201 <-> CHEM101
  - PHYS101 <-> ENG101

**Output:**
```
Course          Time Slot    Color Code
----------------------------------------
CS101           0            ■
CS102           1            ■
MATH201         1            ■
PHYS101         0            ■
CHEM101         0            ■
ENG101          1            ■

Total time slots used: 2
Total courses scheduled: 6
```

**Explanation:**
- Time Slot 0: CS101, PHYS101, CHEM101 (no conflicts between them)
- Time Slot 1: CS102, MATH201, ENG101 (no conflicts between them)

### Example 3: Maximum Conflicts (Complete Graph)

**Input:**
- Courses: A, B, C, D
- Conflicts: All pairs conflict (complete graph)

**Output:**
- 4 time slots (one for each course)

### Example 4: No Conflicts

**Input:**
- Courses: A, B, C, D
- Conflicts: None

**Output:**
- 1 time slot (all courses can be scheduled together)

### Example 5: Bipartite Graph

**Input:**
- Courses: A, B, C, D
- Conflicts: A <-> C, A <-> D, B <-> C, B <-> D

**Output:**
- 2 time slots
  - Slot 0: A, B
  - Slot 1: C, D

---

## Requirements Checklist

### Main Requirements ✅

#### ✅ 1. Ввод данных: курсы, конфликты между ними
- ✅ Text Interface: `add_course()`, `add_conflict()` methods
- ✅ GUI Interface: Entry field for courses, Combobox for conflicts
- ✅ Unlimited courses and conflicts support
- ✅ Validation of input data

#### ✅ 2. Реализация жадного алгоритма раскраски графа
- ✅ `greedy_coloring()` function in `graph_coloring.py`
- ✅ Vertices sorted by degree (descending order)
- ✅ Assigns smallest available color to each vertex
- ✅ Ensures no adjacent vertices have same color
- ✅ O(V + E) time complexity

#### ✅ 3. Вывод результата — назначение слотов/цветов каждому курсу
- ✅ Text Interface: `view_schedule()` displays table with Course, Time Slot, Color Code
- ✅ GUI Interface: `display_schedule()` shows table with color-coded rows
- ✅ Both show assignment for each course

#### ✅ 4. Визуализация количества использованных цветов
- ✅ `get_color_count()` function calculates number of colors
- ✅ Text Interface: Shows "Total time slots used: X"
- ✅ GUI Interface: Shows "Time slots used: X" in info label
- ✅ Color legend in GUI shows all used time slots

### GUI Requirements ✅

- ✅ Форма для добавления курсов (Entry field)
- ✅ Установка конфликтов (Combobox widgets)
- ✅ Кнопка "Generate Schedule"
- ✅ Таблица расписания с цветовым кодированием ячеек

### Text Interface Requirements ✅

- ✅ Меню с опциями
- ✅ Раскраска в виде таблицы текста, где цвета представлены числами
- ✅ Возможность вводить любое количество курсов и конфликтов

### Theoretical Requirements ✅

- ✅ Graph Representation (Adjacency List)
- ✅ Graph Coloring Algorithm (Greedy)
- ✅ Complexity Analysis (O(V + E))

---

## Testing

### Demo Script

The `demo.py` script includes 4 test cases:

1. **Simple Conflict Graph**: Basic two-course conflict
2. **Complex Conflict Graph**: Multiple courses with various conflicts
3. **Complete Graph**: Maximum conflicts (all pairs conflict)
4. **No Conflicts**: All courses can be scheduled together

Run the demo:
```bash
python demo.py
```

### Manual Testing

1. ✅ Test with no courses (shows appropriate message)
2. ✅ Test with single course (assigned slot 0)
3. ✅ Test with multiple courses and no conflicts (all in slot 0)
4. ✅ Test with complex conflict graph
5. ✅ Test validation function

### Test Cases

**Test Case 1: Simple Conflict**
- Courses: A, B
- Conflicts: A <-> B
- Expected: 2 time slots ✅

**Test Case 2: Complete Graph**
- Courses: A, B, C
- Conflicts: A <-> B, A <-> C, B <-> C
- Expected: 3 time slots ✅

**Test Case 3: Bipartite Graph**
- Courses: A, B, C, D
- Conflicts: A <-> C, A <-> D, B <-> C, B <-> D
- Expected: 2 time slots ✅

**All test cases pass validation** ✅

---

## Troubleshooting

### Common Issues

#### Issue: "Please add courses first!"
**Solution:** Add at least one course before generating schedule

#### Issue: "Invalid course numbers!"
**Solution:** Use the numbers shown in the course list (Text Interface)

#### Issue: "A course cannot conflict with itself!"
**Solution:** Select two different courses for conflict

#### Issue: GUI not working
**Solution:**
- **Linux**: Install Tkinter: `sudo apt-get install python3-tk`
- **Windows/Mac**: Tkinter should be included with Python

#### Issue: Module import errors
**Solution:** Ensure all files are in the same directory and run from project root

### Output Interpretation

- **Time Slot**: The assigned time slot number (0, 1, 2, ...)
- **Color Code**: Visual representation (GUI uses colored cells, Text uses symbols)
- **Total time slots used**: Minimum number of different time periods needed
- **Total courses scheduled**: Number of courses successfully assigned

### Tips for Best Results

1. **Add all courses first** before adding conflicts
2. **Review conflicts** before generating schedule
3. **Check the schedule** to ensure it meets your requirements
4. **Use GUI for visual representation** - colors make it easier to see time slot assignments
5. **Text interface is faster** for bulk data entry

---

## Performance & Limitations

### Performance

- **Efficient**: O(V + E) time complexity
- **Scalable**: Handles hundreds of courses efficiently
- **Memory Efficient**: Uses adjacency list representation

### Limitations

1. **Not Optimal**: The greedy algorithm does not guarantee the minimum number of colors
2. **Order Dependency**: Different vertex orderings may yield different numbers of colors
3. **No Preprocessing**: Does not consider additional constraints (room availability, instructor schedules, etc.)
4. **No Export**: Currently displays results on screen only (no CSV/Excel export)

### Known Constraints

- The algorithm provides a valid but not necessarily optimal solution
- Finding the minimum number of colors (chromatic number) is NP-hard
- The greedy approach is efficient but may use more colors than necessary

---

## Future Enhancements

Potential improvements for future versions:

- [ ] Backtracking algorithm for optimal coloring
- [ ] Consider additional constraints (rooms, instructors)
- [ ] Export schedule to CSV/Excel
- [ ] Import courses from file
- [ ] Visualization of the conflict graph
- [ ] Comparison of different coloring strategies
- [ ] Save/load project functionality
- [ ] Undo/redo operations
- [ ] Schedule optimization suggestions

---

## References

1. **Graph Coloring** - [Wikipedia](https://en.wikipedia.org/wiki/Graph_coloring)
2. **Greedy Algorithm** - [GeeksforGeeks](https://www.geeksforgeeks.org/graph-coloring-set-2-greedy-algorithm/)
3. **NP-Completeness** - Introduction to Algorithms (CLRS)
4. **Graph Theory** - Various academic resources on graph algorithms

---

## License

This project is provided as-is for educational purposes.

## Author

Course Scheduler - Graph Coloring Project  
Created for educational purposes to demonstrate graph coloring algorithms.

---

## Project Status

**Status**: ✅ Complete and Functional  
**Testing**: ✅ All tests pass  
**Documentation**: ✅ Complete  
**Requirements**: ✅ All requirements met

---

**Note**: This project is designed for educational purposes to demonstrate the application of graph coloring algorithms in course scheduling problems.
