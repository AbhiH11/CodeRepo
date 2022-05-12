import pandas as pd
data = {
"calories" : [ 360, 456, 789],
    "duration" : [50,40,42]
}
var = pd.DataFrame(data, index= ["day1","day2","day3"])
print(var)