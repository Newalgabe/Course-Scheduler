"""
Main entry point for Course Scheduler
Allows user to choose between text and GUI interfaces
"""

import sys


def main():
    """Main function to choose interface"""
    print("="*50)
    print("Course Scheduler - Graph Coloring")
    print("="*50)
    print("Choose interface:")
    print("1. Text Interface")
    print("2. GUI Interface (Tkinter)")
    print("0. Exit")
    print("="*50)
    
    while True:
        choice = input("\nEnter your choice: ").strip()
        
        if choice == '0':
            print("Goodbye!")
            sys.exit(0)
        elif choice == '1':
            from text_interface import CourseSchedulerText
            scheduler = CourseSchedulerText()
            scheduler.run()
            break
        elif choice == '2':
            try:
                import tkinter as tk
                from gui_interface import CourseSchedulerGUI
                root = tk.Tk()
                app = CourseSchedulerGUI(root)
                root.mainloop()
                break
            except ImportError:
                print("Error: Tkinter is not available on this system!")
                print("Please use the text interface instead.")
                continue
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()



