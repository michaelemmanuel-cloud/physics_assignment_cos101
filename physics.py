print("Welcome to my calculator,what do you want to calculate. The following are the options available;")
print('a - Area of circle')
print('b - velocity')
print('c - force')
print('d - power')
print('e - density')
print('f - Gravitational force')
print('g - Acceleration')

def a():
    radius = float(input("Enter  radius"))
    area =  22/7 *  radius
    print("Result;")
    print(area)

#calculate_area_of_circle


def b():
    displacement = float(input("Enter your displacement"))
    time = int(input("Enter Time"))
    velocity = displacement/time
    print("Result;")
    print(velocity)

#calculate_velocity

def c ():
    mass = float(input("Enter Mass"))
    acceleration = float(input("Enter Acceleration"))
    force = mass * acceleration
    print("Result;")
    print(force)

#calculate_force()

def d():
    work_done = float(input("Enter Work done"))
    time_taken = float(input("Enter the Time taken"))
    power = work_done / time_taken
    print("Result;")
    print(power)

#calculate_power()

def e():
    mass = float(input("Enter Mass of the Object"))
    velocity = float(input("Enter the Velocity"))
    density = mass * velocity
    print("Result;")
    print(density)

#calculate_density()

def f():
    mass = float(input("Enter mass"))
    gravity=float(input("Enter the gravity"))
    height = float(input("Enter the height"))
    gravitational_force = mass * gravity * height
    print("Result;")
    print(gravitational_force)

#calculate_gravitational_force()

def g():
    velocity = float(input("Enter the velocity"))
    distance = float(input("Enter the distance"))
    acceleration = velocity / distance
    print("Result;")
    print(acceleration)

#calculate_acceleration()

def main():
    option = input("Choose an option")
    if option == "a":
        print("To Calculate Area of a Circle")
        a()
    if option == "b":
        print("To Calculate Velocity")
        b()
    if option == "c":
        print("To Calculate Force")
        c()
    if option =="d":
        print("To Calculate Power")
        d()
    if option =="e":
       print("To Calculate Density")
       e()
    if option == "f":
       print("To Calculate Gravitational Force")
       f()
    if option == "g":
       print("To Calculate Acceleration")
       g()


if __name__ == "__main__":
    main()













