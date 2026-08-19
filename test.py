from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights

#res = tavily_search("Best places in india to visit in 2026")

#print(res)
res = search_flights("Plan a 7 days Nepal  trip from Bangladesh")
print(res)