# TEMPERATURE CONVERTER

temperature_celsius = float(input('\n Enter the temperature in Celsius : '))
temperature_fahrenheit = (1.8*temperature_celsius)+32
print(' Temperature in fahrenheit : '+str(temperature_fahrenheit))

if ( (temperature_fahrenheit > 68) and (temperature_fahrenheit < 98) ) :
    print('\n Turn ON the FAN\n')
elif temperature_fahrenheit > 98:
    print('\n Turn ON the AC\n')
else:
    print('\n Turn OFF the FAN and AC\n')