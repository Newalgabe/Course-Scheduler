"""
GUI interface for Course Scheduler using Tkinter
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from graph_coloring import Graph, greedy_coloring, get_color_count, validate_coloring


class CourseSchedulerGUI:
    """GUI interface for course scheduling"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Course Scheduler - Graph Coloring")
        self.root.geometry("900x700")
        
        self.graph = Graph()
        self.coloring = {}
        
        # Color palette for time slots
        self.color_palette = [
            '#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A',
            '#98D8C8', '#F7DC6F', '#BB8FCE', '#85C1E2',
            '#F8B739', '#6C5CE7', '#A29BFE', '#FD79A8'
        ]
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the user interface"""
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(2, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="Course Scheduler", 
                                font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Left panel - Input
        left_panel = ttk.LabelFrame(main_frame, text="Course Management", padding="10")
        left_panel.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)
        
        # Course input
        ttk.Label(left_panel, text="Course Name:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.course_entry = ttk.Entry(left_panel, width=20)
        self.course_entry.grid(row=0, column=1, pady=5, padx=5)
        
        ttk.Button(left_panel, text="Add Course", 
                  command=self.add_course).grid(row=0, column=2, pady=5, padx=5)
        
        # Course list
        ttk.Label(left_panel, text="Courses:").grid(row=1, column=0, columnspan=3, 
                                                     sticky=tk.W, pady=(10, 5))
        self.course_listbox = tk.Listbox(left_panel, height=8, width=30)
        self.course_listbox.grid(row=2, column=0, columnspan=3, pady=5, sticky=(tk.W, tk.E))
        
        scrollbar1 = ttk.Scrollbar(left_panel, orient="vertical", 
                                   command=self.course_listbox.yview)
        scrollbar1.grid(row=2, column=3, sticky=(tk.N, tk.S))
        self.course_listbox.configure(yscrollcommand=scrollbar1.set)
        
        # Conflict selection
        ttk.Label(left_panel, text="Select courses with conflicts:").grid(row=3, column=0, 
                                                                          columnspan=3, 
                                                                          sticky=tk.W, 
                                                                          pady=(10, 5))
        
        conflict_frame = ttk.Frame(left_panel)
        conflict_frame.grid(row=4, column=0, columnspan=3, pady=5)
        
        ttk.Label(conflict_frame, text="Course 1:").grid(row=0, column=0, padx=5)
        self.conflict_course1 = ttk.Combobox(conflict_frame, width=15, state="readonly")
        self.conflict_course1.grid(row=0, column=1, padx=5)
        
        ttk.Label(conflict_frame, text="Course 2:").grid(row=0, column=2, padx=5)
        self.conflict_course2 = ttk.Combobox(conflict_frame, width=15, state="readonly")
        self.conflict_course2.grid(row=0, column=3, padx=5)
        
        ttk.Button(conflict_frame, text="Add Conflict", 
                  command=self.add_conflict).grid(row=0, column=4, padx=5)
        
        # Conflicts list
        ttk.Label(left_panel, text="Conflicts:").grid(row=5, column=0, columnspan=3, 
                                                       sticky=tk.W, pady=(10, 5))
        self.conflict_listbox = tk.Listbox(left_panel, height=6, width=30)
        self.conflict_listbox.grid(row=6, column=0, columnspan=3, pady=5, sticky=(tk.W, tk.E))
        
        scrollbar2 = ttk.Scrollbar(left_panel, orient="vertical", 
                                   command=self.conflict_listbox.yview)
        scrollbar2.grid(row=6, column=3, sticky=(tk.N, tk.S))
        self.conflict_listbox.configure(yscrollcommand=scrollbar2.set)
        
        # Buttons
        button_frame = ttk.Frame(left_panel)
        button_frame.grid(row=7, column=0, columnspan=3, pady=10)
        
        ttk.Button(button_frame, text="Generate Schedule", 
                  command=self.generate_schedule).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Clear All", 
                  command=self.clear_data).pack(side=tk.LEFT, padx=5)
        
        # Right panel - Schedule
        right_panel = ttk.LabelFrame(main_frame, text="Schedule", padding="10")
        right_panel.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)
        right_panel.columnconfigure(0, weight=1)
        right_panel.rowconfigure(1, weight=1)
        
        # Schedule info
        self.info_label = ttk.Label(right_panel, text="No schedule generated yet.", 
                                   font=('Arial', 10))
        self.info_label.grid(row=0, column=0, pady=5)
        
        # Schedule table
        schedule_frame = ttk.Frame(right_panel)
        schedule_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        schedule_frame.columnconfigure(0, weight=1)
        schedule_frame.rowconfigure(0, weight=1)
        
        # Treeview for schedule
        columns = ('Course', 'Time Slot', 'Color')
        self.schedule_tree = ttk.Treeview(schedule_frame, columns=columns, show='headings', 
                                          height=15)
        
        for col in columns:
            self.schedule_tree.heading(col, text=col)
            self.schedule_tree.column(col, width=150, anchor=tk.CENTER)
        
        scrollbar3 = ttk.Scrollbar(schedule_frame, orient="vertical", 
                                   command=self.schedule_tree.yview)
        scrollbar3.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.schedule_tree.configure(yscrollcommand=scrollbar3.set)
        self.schedule_tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Color legend
        legend_frame = ttk.LabelFrame(right_panel, text="Time Slot Colors", padding="5")
        legend_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=10)
        
        self.legend_canvas = tk.Canvas(legend_frame, height=50)
        self.legend_canvas.pack(fill=tk.BOTH, expand=True)
    
    def add_course(self):
        """Add a new course"""
        course = self.course_entry.get().strip()
        if not course:
            messagebox.showwarning("Warning", "Please enter a course name!")
            return
        
        if course in self.graph.vertices:
            messagebox.showinfo("Info", f"Course '{course}' already exists!")
            return
        
        self.graph.add_vertex(course)
        self.update_course_list()
        self.course_entry.delete(0, tk.END)
        messagebox.showinfo("Success", f"Course '{course}' added successfully!")
    
    def add_conflict(self):
        """Add a conflict between two courses"""
        course1 = self.conflict_course1.get()
        course2 = self.conflict_course2.get()
        
        if not course1 or not course2:
            messagebox.showwarning("Warning", "Please select both courses!")
            return
        
        if course1 == course2:
            messagebox.showwarning("Warning", "A course cannot conflict with itself!")
            return
        
        self.graph.add_edge(course1, course2)
        self.update_conflict_list()
        messagebox.showinfo("Success", f"Conflict added between '{course1}' and '{course2}'")
    
    def update_course_list(self):
        """Update the course listbox and comboboxes"""
        # Update listbox
        self.course_listbox.delete(0, tk.END)
        for course in self.graph.vertices:
            degree = self.graph.get_degree(course)
            self.course_listbox.insert(tk.END, f"{course} ({degree} conflicts)")
        
        # Update comboboxes
        self.conflict_course1['values'] = self.graph.vertices
        self.conflict_course2['values'] = self.graph.vertices
    
    def update_conflict_list(self):
        """Update the conflict listbox"""
        self.conflict_listbox.delete(0, tk.END)
        conflicts_added = set()
        
        for vertex in self.graph.vertices:
            neighbors = self.graph.get_neighbors(vertex)
            for neighbor in neighbors:
                # Add each conflict only once
                conflict_pair = tuple(sorted([vertex, neighbor]))
                if conflict_pair not in conflicts_added:
                    conflicts_added.add(conflict_pair)
                    self.conflict_listbox.insert(tk.END, f"{vertex} <-> {neighbor}")
    
    def generate_schedule(self):
        """Generate schedule using graph coloring"""
        if not self.graph.vertices:
            messagebox.showwarning("Warning", "Please add courses first!")
            return
        
        self.coloring = greedy_coloring(self.graph)
        
        if validate_coloring(self.graph, self.coloring):
            color_count = get_color_count(self.coloring)
            self.display_schedule()
            self.info_label.config(
                text=f"Schedule generated! Time slots used: {color_count} | "
                     f"Courses scheduled: {len(self.coloring)}"
            )
            messagebox.showinfo("Success", 
                              f"Schedule generated successfully!\n"
                              f"Time slots used: {color_count}")
        else:
            messagebox.showerror("Error", "Invalid coloring generated!")
    
    def display_schedule(self):
        """Display the schedule in the treeview"""
        # Clear existing items
        for item in self.schedule_tree.get_children():
            self.schedule_tree.delete(item)
        
        # Add schedule items
        for course in sorted(self.coloring.keys()):
            slot = self.coloring[course]
            color = self.get_color_for_slot(slot)
            self.schedule_tree.insert('', tk.END, values=(course, slot, '■'), 
                                     tags=(f'slot{slot}',))
            # Tag items for color coding
            self.schedule_tree.tag_configure(f'slot{slot}', background=color)
        
        # Update legend
        self.update_legend()
    
    def get_color_for_slot(self, slot):
        """Get color for a time slot"""
        return self.color_palette[slot % len(self.color_palette)]
    
    def update_legend(self):
        """Update the color legend"""
        self.legend_canvas.delete("all")
        
        if not self.coloring:
            return
        
        unique_slots = sorted(set(self.coloring.values()))
        slot_width = 60
        x = 10
        
        for slot in unique_slots:
            color = self.get_color_for_slot(slot)
            # Draw colored rectangle
            self.legend_canvas.create_rectangle(x, 10, x + 40, 30, fill=color, outline='black')
            # Draw slot number
            self.legend_canvas.create_text(x + 20, 20, text=str(slot))
            # Draw label
            self.legend_canvas.create_text(x + 20, 40, text=f"Slot {slot}")
            x += slot_width
    
    def clear_data(self):
        """Clear all data"""
        if messagebox.askyesno("Confirm", "Are you sure you want to clear all data?"):
            self.graph = Graph()
            self.coloring = {}
            self.course_listbox.delete(0, tk.END)
            self.conflict_listbox.delete(0, tk.END)
            self.schedule_tree.delete(*self.schedule_tree.get_children())
            self.info_label.config(text="No schedule generated yet.")
            self.legend_canvas.delete("all")
            self.conflict_course1.set('')
            self.conflict_course2.set('')
            messagebox.showinfo("Success", "All data cleared!")


def main():
    """Main function to run the GUI"""
    root = tk.Tk()
    app = CourseSchedulerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()



