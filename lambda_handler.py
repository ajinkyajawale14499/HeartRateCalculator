import json

def lambda_handler(event, context):
    #lambda handler function
    age = event["age"]
    calculate_max_heart_rate(age)
    calculate_low_heart_rate_range(event,context)
    calculate_high_heart_rate_range(event,context)
    return {
        "low": round(low_heart_rate_range),
        "high":round(high_heart_rate_range)}
    
        
def calculate_max_heart_rate(age):
    # caculates maximum heart rate
    global max_heart_rate
    max_heart_rate = 220 - age
    return max_heart_rate
    
def calculate_low_heart_rate_range(event,context):
    # calculates the low heart rate range
    global low_heart_rate_range
    low_heart_rate_range = max_heart_rate * .7
    return low_heart_rate_range
    
def calculate_high_heart_rate_range(event,context):
    # calculates the high heart rate range
    global high_heart_rate_range
    high_heart_rate_range = max_heart_rate * .85
    return high_heart_rate_range  
