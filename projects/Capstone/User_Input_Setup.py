#create unique lists of destination cities, days of the week, months, time blocks, and carriers
bay_dest = bay_raw.dest_city_name.unique().tolist()
day_of_week_select = bay_raw.day_of_week.unique().tolist()
month_select = bay_raw.month.unique().tolist()
time_blocks_select = bay_raw.dep_time_blk.unique().tolist()
carrier_select = bay_raw.carrier.unique().tolist()

#this creates a function to be run on the click of the submit button that will print out all of the users selections
def test(val):
    print "Submitted!"
    print "Destination City: ", destination.value
    print "Airline: ", airline.value
    print "Departure Month: ", month.value 
    print "Day of the Week: ", day_of_week.value
    print "Departure Time: ", time_of_day.value
#     predict_funct(val)


#creates user input drop down for destination
destination = Dropdown(
    options= bay_dest,
    value= bay_dest[0],
    description='Dest. City: ',
)

month = Dropdown(
    options=month_select,
    value= month_select[0],
    description='Month: ',
)

day_of_week = Dropdown(
    options=day_of_week_select,
    value= day_of_week_select[0],
    description='Day of the Week: ',
)

time_of_day = Dropdown(
    options= time_blocks_select,
    value= time_blocks_select[0],
    description='Hour of Flight: ',
)

airline = Dropdown(
    options=carrier_select,
    value= carrier_select[0],
    description='Airline: '
)


# Creates submit button and event for when buttons is clicked, which I set to the function test, made above
submit_button = Button(description="Submit Info")
submit_button.on_click(test)

#displays dropdowns and submit button
display(destination)
display(airline)
display(month)
display(day_of_week)
display(time_of_day)
    
display(submit_button)


#Print out the results and use if statements to make a recommendation on which airport to fly out of.
print "Based on your selection there is a " + str(round((sj_final_pred*100),2)) + "% chance of delay at the San Jose Airport."
print "Based on your selection there is a " + str(round((sf_final_pred*100),2)) + "% chance of delay at the San Francisco Airport."
print "Based on your selection there is a " + str(round((oak_final_pred*100),2)) + "% chance of delay at the Oakland Airport. \n"

if (sj_final_pred < oak_final_pred) & (sj_final_pred < sf_final_pred):
    print "I suggest you fly out of San Jose to avoid delays"
elif (sf_final_pred < oak_final_pred) & (sf_final_pred < sj_final_pred):
    print "I suggest you fly out of San Francisco to avoid delays"
else:
    print "I suggest you fly out of Oakland to avoid delays"



