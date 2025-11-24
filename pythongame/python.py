import json
from datetime import datetime

class Task:
	def __init__(self, description, due_date=None, priority="Medium"):
		self.description = description 
		self.due_date = due_date 
		self.priority = priority
		self.completed = False
	def mark_complete(self):
		self.completed = True
		
	def to_dict(self):
		return {
			"description": self.description,
			"due_date": self.due_date,
			"priority": self.priority,
			"completed": self.completed
		}
	@staticmethod
	def from_dict(data):
		task = Task(data["description"], data ["due_date"], data["priority"])
		task.completed = data["completed"]
		return task

class TaskManager:
	def __init__(self, filename="tasks.json"):
		self.file = filename
		self.tasks = []
		self.load_tasks()
		
	def add_task(self, description, due_date=None, priority="Medium"):
		if priority not in ["Low", "Medium", "High"]:
			raise ValueError("Priority must be Low, Medium, or High")
		task = Task(description, due_date, priority)
		self.tasks.append(task)
		self.save_tasks()
		
	def list_tasks(self, filter_completed=None, filter_priority=None):
		sorted_tasks = sorted(self.tasks, key=lambda t: t.priority == "High", reverse=True)
		for i, task in enumerate(sorted_tasks):
			status = "Done" if task.completed else "Pending"
			due = f" (Due: {task.due_date})" if task.due_date else ""
			priority = task.priority
			if (filter_completed is None or task.completed == filter_completed) and \
			(filter_priority is None or task.priority == filter_priority):
			 print(f"{i+1}. [{status}] {task.description}{due} - Priority: {priority}")
	
	def complete_task(self, index):
		if 0 <= index < len(self.tasks):
			self.tasks[index].mark_complete()
			self.save_tasks()
		else: 
			raise IndexError("Invalid task index")
	
	def delete_task(self, index):
		if 0 <= index < len(self.tasks):
			del self.tasks[index]
			self.save_tasks()
		else: 
			raise IndexError("Invalid task index")
	
	def save_tasks(self):
		data [task.to_dict() for task in self.tasks]
		with open(self.filename, "w") as f:
			json.dump(data, f, indent=4)
	
	def load_tasks(self):
		try: with open(self.filename, "r") as f:
			data = json.load(f)
			self.tasks = [Task.from_dict(item) for item in data]
		except FileNotFoundError:
			self.tasks = []
		except json.JSONDecodeError:
			print("Corrupted file - starting with empty tasks.")
			self.tasks = []

def main():
	manager = TaskManager()
	while True:
		print("\n--- Task Manager ---")
		print("1. Add Task\n2. List Tasks\n3. Complete Task\n4. Delete Task\n5. Filter Pending\n6. Filter by Priority\n7. Exit ")
		choice = input("Choose an option: ").strip()
		
	if choice == "1":
		desc = input("Description: ")
		due = input("Due date (YYYY-MM-DD, optional): ") or None
		prio = input("Priority (Low/Medium/High, default Medium): ") or "Medium"
		try:
			manager.add_task(desc, due, prio.capitalize())
			print("Task added!")
		except ValueError as e:
			print(f"Error: {e}")
	
	elif choice == "2":
		manager.list_tasks()
	
	elif choice == "3":
		manager.list_task()
		idx = int(input("Task number to complete: ")) - 1
		try: 
			manager.complete_task(idx)
			print("Task completed!")
		except (ValueError, IndexError) as e:
			print(f"Error: {e}")
	
	elif choice == "4":
		manager.list_tasks()
		idx = int(input("Task number to delete: ")) - 1
		try: 
			manager.delete_task(idx)
			print("Task deleted!")
		except (ValueError, IndexError) as e:
			print(f"Error: {e}")
		
	elif choice == "5":
		manager.list_tasks(filter_completed=False)
		
	elif choice == "6":
		prio = input("Priority to filter (Low/Medium/High): ").capitalize()
		manager.list_tasks(filter_priority=prio)
		
	elif choice == "7":
		print("Goodbye!")
		break
		
	else:
		print("Invalid choice - try again.")
		
if __name == "__main__":
	main()
