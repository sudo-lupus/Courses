# Defining Functions
def greeting(name, department):
    print("Welcome, " + name)
    print("You are part of " + department)

greeting("Lionel", "IT")

# Returning Values
# Example 1: Returning a single value
def area_triangle(base, height):
    return base * height / 2

area_a = area_triangle(5, 4)
area_b = area_triangle(7, 3)
sum = area_a + area_b

print("\nThe sum of both areas is " + str(sum) + "\n")


### Example 2: Returning multiple values
def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

seconds_1 = 3721
hours, minutes, seconds = convert_seconds(seconds_1)
print(f"{seconds_1} seconds =\n{hours} hours, {minutes} minutes, {seconds} seconds\n")

hours_mins_secs = list(convert_seconds(seconds_1))
print(f"{hours_mins_secs}\n")


# Example 3: 
def greeting_2(name):
    print("Welcome " + name)

result = greeting_2("Christine")
print(result)
print(type(result))