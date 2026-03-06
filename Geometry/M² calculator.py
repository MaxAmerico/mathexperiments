print('--- You have entered the Polygon Area Calculator! ---')

while True:
    print('Please choose one of the allowed polygons to measure:')
    
    # User choice
    choose_polygon = input('A. Rectangle. B. Triangle. C. Pentagon.').upper()

    if choose_polygon == 'A': 
        print('Great! Lets calculate the area of a rectangle.')
        length = float(input('What is the length of your rectangle? (meters): '))
        width = float(input('What is the width of your rectangle? (meters): '))
        area_r = length * width
        print(f'Your rectangle has an area of {area_r} m²')
        continue
        
    elif choose_polygon == 'B':
        print('Great! Lets calculate the area of a triangle.')
        base = float(input('What is the base of your triangle? (meters): '))
        height = float(input('What is the height of your triangle? (meters): '))
        area_t = (base * height) / 2
        print(f'Your triangle has an area of {area_t} m²')
        continue

    elif choose_polygon == 'C':
        print('Great! Lets calculate the area of your pentagon.')
        perimeter = float(input('What is the total perimeter? (meters): '))
        apothem = float(input('What is the value of the apothem? (meters): '))
        area_p = (perimeter * apothem) / 2
        print(f'Your pentagon has an area of {area_p} m²')
        continue
    
    else:
        print('Invalid option. Please try again.')
        break
