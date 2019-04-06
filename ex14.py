from sys import argv

script, user_name, lucky = argv

prompt = ">>>> "

print(f"Lucky today? {lucky}")

print(f"Hi {user_name}, I am your {script} script")
print(f"Like {user_name}? ")
likes = input(prompt)

print("what computer you use?")
computer = input(prompt)

print(f"""
Like me ? - {likes}
Your computer is {computer}
""")
