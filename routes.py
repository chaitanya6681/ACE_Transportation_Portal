route1_stops=["Uppal","Boduppal","Ghatkesar"]
stop_coordinates=(17.39879,78.55384)
reg_passids={"ACEG001","ACEG002","ACEG003"}
bus_fleet={"Bus no":"TS33G6681","capacity":"45","driver":"Suresh"}
def display_routestops(route_stops):
    print("Root Stops:")
    for i in route_stops:
        print(i)
def add_stop(route_stops,new_stop):
    route_stops.append(new_stop)
def register_student_pass(passid_set,new_id):
    if new_id in passid_set:
        print("This pass id already exits")
    else:
        passid_set.add(new_id) 
def display_busdetails(bus_dict):
    print("Bus details:")
    for i in bus_dict:
        print(i,":",bus_dict[i])


display_busdetails(bus_fleet)
add_stop(route1_stops,"KPHB")
display_routestops(route1_stops)