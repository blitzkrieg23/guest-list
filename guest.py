def guest_list(guests):
	for guest in guests:
		name,age,job = guest
		print(f"{name} is {age} years old and works as a {job}")

guest_list([('John', 21, "Doctor"), ("Bryan", 35, 'Teacher'), ('Jennifer', 24, "Data Engineer")])

"""
Output should match:
John is 21 years old and works as a Doctor
Bryan is 35 years old and works as a Teacher
Jennifer is 24 years old and works as a Data Engineer
"""