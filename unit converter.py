cm = int(input('Enter the lenght in cm: '))
cm_to_m = cm/100
cm_to_inch = cm/0.394

print('Lenght {} is {:.3f} m or {:.3f} inch'.format(cm, cm_to_m, cm_to_inch))

kg = int(input('Enter the weight in kg: '))
kg_to_mg = kg * 1000000
kg_to_oz = kg/0.0283452
kg_to_lb = kg * 2.2046
print('Weight %.2f is %.2f mg, %.4f oz, or %.3f lbs' %(kg, kg_to_mg, kg_to_oz, kg_to_lb))
