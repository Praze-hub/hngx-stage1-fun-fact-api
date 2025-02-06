
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view

def get_math_properties(number):
    properties = []
    is_prime = number > 1 and all(number % i !=0 for i in range(2, int(number ** 0.5) + 1))
    is_perfect = sum(i for i in range(1, number) if number % 1 == 0) == number
    digit_sum = sum(int(digit) for digit in str(number))
    
    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")
        
    if is_prime:
        properties.append("prime")
        
    num_digits  = len(str(number))
    if sum(int(digit) ** num_digits for digit in str(number)) == number:
        properties.append("armstrong")
        
    return is_prime, is_perfect, properties, digit_sum

@api_view(['GET'])
def number_fact(request, number):
    url = f"http://numbersapi.com/{number}/math"
    response = requests.get(url)
    
    if response.status_code == 200:
        is_prime, is_perfect, properties, digit_sum = get_math_properties(number)
        return Response({
            "number": number,
            "is_prime": is_prime,
            "is_perfect": is_perfect,
            "properties": properties,
            "digit_sum": digit_sum,
            "fun fact": response.text
        })
    else:
        return Response({"error": "Could not retrieve fact"}, status=400)
    
    
    