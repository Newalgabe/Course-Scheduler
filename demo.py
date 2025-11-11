"""
Demo script to demonstrate the Graph Coloring algorithm
"""

from graph_coloring import Graph, greedy_coloring, get_color_count, validate_coloring


def demo_simple():
    """Simple demo with 3 courses"""
    print("="*60)
    print("Demo 1: Simple Conflict Graph")
    print("="*60)
    
    graph = Graph()
    
    # Add courses
    courses = ["CS101", "CS102", "MATH201"]
    for course in courses:
        graph.add_vertex(course)
    
    # Add conflicts
    graph.add_edge("CS101", "CS102")
    graph.add_edge("CS101", "MATH201")
    
    print("\nCourses:")
    for course in graph.vertices:
        print(f"  - {course}")
    
    print("\nConflicts:")
    for vertex in graph.vertices:
        for neighbor in graph.get_neighbors(vertex):
            if vertex < neighbor:
                print(f"  - {vertex} <-> {neighbor}")
    
    # Generate coloring
    coloring = greedy_coloring(graph)
    
    print("\nSchedule:")
    print(f"{'Course':<15} {'Time Slot':<15}")
    print("-"*30)
    for course in sorted(coloring.keys()):
        print(f"{course:<15} {coloring[course]:<15}")
    
    print(f"\nTime slots used: {get_color_count(coloring)}")
    print(f"Valid coloring: {validate_coloring(graph, coloring)}")
    print()


def demo_complex():
    """Complex demo with multiple courses"""
    print("="*60)
    print("Demo 2: Complex Conflict Graph")
    print("="*60)
    
    graph = Graph()
    
    # Add courses
    courses = ["CS101", "CS102", "MATH201", "PHYS101", "CHEM101", "ENG101"]
    for course in courses:
        graph.add_vertex(course)
    
    # Add conflicts
    conflicts = [
        ("CS101", "CS102"),
        ("CS101", "MATH201"),
        ("CS102", "PHYS101"),
        ("MATH201", "CHEM101"),
        ("PHYS101", "ENG101"),
    ]
    
    for course1, course2 in conflicts:
        graph.add_edge(course1, course2)
    
    print("\nCourses:")
    for course in graph.vertices:
        degree = graph.get_degree(course)
        print(f"  - {course} ({degree} conflicts)")
    
    print("\nConflicts:")
    conflicts_added = set()
    for vertex in graph.vertices:
        for neighbor in graph.get_neighbors(vertex):
            conflict_pair = tuple(sorted([vertex, neighbor]))
            if conflict_pair not in conflicts_added:
                conflicts_added.add(conflict_pair)
                print(f"  - {vertex} <-> {neighbor}")
    
    # Generate coloring
    coloring = greedy_coloring(graph)
    
    print("\nSchedule:")
    print(f"{'Course':<15} {'Time Slot':<15}")
    print("-"*30)
    for course in sorted(coloring.keys()):
        print(f"{course:<15} {coloring[course]:<15}")
    
    # Group by time slot
    slots = {}
    for course, slot in coloring.items():
        if slot not in slots:
            slots[slot] = []
        slots[slot].append(course)
    
    print("\nSchedule by Time Slot:")
    for slot in sorted(slots.keys()):
        courses = slots[slot]
        print(f"  Time Slot {slot}: {', '.join(courses)}")
    
    print(f"\nTime slots used: {get_color_count(coloring)}")
    print(f"Valid coloring: {validate_coloring(graph, coloring)}")
    print()


def demo_complete_graph():
    """Demo with complete graph (maximum conflicts)"""
    print("="*60)
    print("Demo 3: Complete Graph (Maximum Conflicts)")
    print("="*60)
    
    graph = Graph()
    
    # Add courses
    courses = ["A", "B", "C", "D"]
    for course in courses:
        graph.add_vertex(course)
    
    # Add all possible conflicts (complete graph)
    for i in range(len(courses)):
        for j in range(i + 1, len(courses)):
            graph.add_edge(courses[i], courses[j])
    
    print("\nCourses:")
    for course in graph.vertices:
        print(f"  - {course}")
    
    print("\nConflicts: All pairs conflict (complete graph)")
    
    # Generate coloring
    coloring = greedy_coloring(graph)
    
    print("\nSchedule:")
    print(f"{'Course':<15} {'Time Slot':<15}")
    print("-"*30)
    for course in sorted(coloring.keys()):
        print(f"{course:<15} {coloring[course]:<15}")
    
    print(f"\nTime slots used: {get_color_count(coloring)}")
    print(f"Expected: {len(courses)} (one slot per course)")
    print(f"Valid coloring: {validate_coloring(graph, coloring)}")
    print()


def demo_no_conflicts():
    """Demo with no conflicts"""
    print("="*60)
    print("Demo 4: No Conflicts")
    print("="*60)
    
    graph = Graph()
    
    # Add courses
    courses = ["CS101", "CS102", "MATH201", "PHYS101"]
    for course in courses:
        graph.add_vertex(course)
    
    # No conflicts added
    
    print("\nCourses:")
    for course in graph.vertices:
        print(f"  - {course}")
    
    print("\nConflicts: None")
    
    # Generate coloring
    coloring = greedy_coloring(graph)
    
    print("\nSchedule:")
    print(f"{'Course':<15} {'Time Slot':<15}")
    print("-"*30)
    for course in sorted(coloring.keys()):
        print(f"{course:<15} {coloring[course]:<15}")
    
    print(f"\nTime slots used: {get_color_count(coloring)}")
    print(f"Expected: 1 (all courses can be scheduled together)")
    print(f"Valid coloring: {validate_coloring(graph, coloring)}")
    print()


def main():
    """Run all demos"""
    print("\n" + "="*60)
    print("Course Scheduler - Graph Coloring Demo")
    print("="*60 + "\n")
    
    demo_simple()
    demo_complex()
    demo_complete_graph()
    demo_no_conflicts()
    
    print("="*60)
    print("All demos completed!")
    print("="*60)


if __name__ == "__main__":
    main()



