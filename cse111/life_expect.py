"""Playing around with data"""
#opening file
with open("life-expectancy.csv") as le_file:
    #Country Getter
    def get_country_data(country):
        past_first_line = False
        for line in le_file:
            if past_first_line == False:
                past_first_line = True
                continue
            line = line.strip()
            parts = line.split(",")
            if parts[0] == country:
                return parts