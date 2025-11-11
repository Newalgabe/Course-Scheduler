"""
Text-based interface for Course Scheduler
"""

from graph_coloring import Graph, greedy_coloring, get_color_count, validate_coloring


class CourseSchedulerText:
    """Text-based interface for course scheduling"""
    
    def __init__(self):
        self.graph = Graph()
        self.coloring = {}
    
    def display_menu(self):
        """Display the main menu"""
        print("\n" + "="*50)
        print("Course Scheduler - Graph Coloring")
        print("="*50)
        print("1. Add course")
        print("2. Add conflict between courses")
        print("3. View all courses")
        print("4. View all conflicts")
        print("5. Generate schedule (Graph Coloring)")
        print("6. View schedule")
        print("7. Clear all data")
        print("0. Exit")
        print("="*50)
    
    def add_course(self):
        """Add a new course"""
        course = input("Enter course name: ").strip()
        if course:
            self.graph.add_vertex(course)
            print(f"Course '{course}' added successfully!")
        else:
            print("Invalid course name!")
    
    def add_conflict(self):
        """Add a conflict between two courses"""
        if len(self.graph.vertices) < 2:
            print("Please add at least 2 courses first!")
            return
        
        print("\nAvailable courses:")
        for i, course in enumerate(self.graph.vertices, 1):
            print(f"{i}. {course}")
        
        try:
            course1_idx = int(input("Enter first course number: ")) - 1
            course2_idx = int(input("Enter second course number: ")) - 1
            
            if 0 <= course1_idx < len(self.graph.vertices) and 0 <= course2_idx < len(self.graph.vertices):
                course1 = self.graph.vertices[course1_idx]
                course2 = self.graph.vertices[course2_idx]
                
                if course1 == course2:
                    print("A course cannot conflict with itself!")
                else:
                    self.graph.add_edge(course1, course2)
                    print(f"Conflict added between '{course1}' and '{course2}'")
            else:
                print("Invalid course numbers!")
        except ValueError:
            print("Invalid input! Please enter numbers.")
    
    def view_courses(self):
        """Display all courses"""
        if not self.graph.vertices:
            print("No courses added yet!")
            return
        
        print("\nCourses:")
        for i, course in enumerate(self.graph.vertices, 1):
            degree = self.graph.get_degree(course)
            print(f"{i}. {course} (Conflicts: {degree})")
    
    def view_conflicts(self):
        """Display all conflicts"""
        if not self.graph.vertices:
            print("No courses added yet!")
            return
        
        has_conflicts = False
        print("\nConflicts:")
        for vertex in self.graph.vertices:
            neighbors = self.graph.get_neighbors(vertex)
            if neighbors:
                has_conflicts = True
                for neighbor in neighbors:
                    # Print each conflict only once
                    if vertex < neighbor:
                        print(f"  {vertex} <-> {neighbor}")
        
        if not has_conflicts:
            print("  No conflicts defined yet!")
    
    def generate_schedule(self):
        """Generate schedule using graph coloring"""
        if not self.graph.vertices:
            print("Please add courses first!")
            return
        
        self.coloring = greedy_coloring(self.graph)
        
        if validate_coloring(self.graph, self.coloring):
            color_count = get_color_count(self.coloring)
            print(f"\nSchedule generated successfully!")
            print(f"Number of time slots used: {color_count}")
        else:
            print("Error: Invalid coloring generated!")
    
    def view_schedule(self):
        """Display the schedule"""
        if not self.coloring:
            print("Please generate schedule first!")
            return
        
        print("\n" + "="*60)
        print("COURSE SCHEDULE")
        print("="*60)
        print(f"{'Course':<30} {'Time Slot':<15} {'Color Code'}")
        print("-"*60)
        
        # Group courses by time slot
        slots = {}
        for course, slot in sorted(self.coloring.items()):
            if slot not in slots:
                slots[slot] = []
            slots[slot].append(course)
        
        # Display by time slot
        for slot in sorted(slots.keys()):
            courses = slots[slot]
            color_code = self._get_color_display(slot)
            for i, course in enumerate(courses):
                if i == 0:
                    print(f"{course:<30} {slot:<15} {color_code}")
                else:
                    print(f"{course:<30} {'':<15} {''}")
        
        print("="*60)
        print(f"Total time slots used: {len(slots)}")
        print(f"Total courses scheduled: {len(self.coloring)}")
    
    def _get_color_display(self, color_num):
        """Get a visual representation of the color"""
        colors = ['■', '■', '■', '■', '■', '■', '■', '■']
        if color_num < len(colors):
            return colors[color_num]
        return '■'
    
    def clear_data(self):
        """Clear all courses and conflicts"""
        confirm = input("Are you sure you want to clear all data? (yes/no): ").strip().lower()
        if confirm == 'yes':
            self.graph = Graph()
            self.coloring = {}
            print("All data cleared!")
        else:
            print("Operation cancelled.")
    
    def run(self):
        """Run the text interface"""
        while True:
            self.display_menu()
            try:
                choice = input("\nEnter your choice: ").strip()
                
                if choice == '0':
                    print("Thank you for using Course Scheduler!")
                    break
                elif choice == '1':
                    self.add_course()
                elif choice == '2':
                    self.add_conflict()
                elif choice == '3':
                    self.view_courses()
                elif choice == '4':
                    self.view_conflicts()
                elif choice == '5':
                    self.generate_schedule()
                elif choice == '6':
                    self.view_schedule()
                elif choice == '7':
                    self.clear_data()
                else:
                    print("Invalid choice! Please try again.")
                
                input("\nPress Enter to continue...")
            except KeyboardInterrupt:
                print("\n\nProgram interrupted. Goodbye!")
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                input("\nPress Enter to continue...")


if __name__ == "__main__":
    scheduler = CourseSchedulerText()
    scheduler.run()



