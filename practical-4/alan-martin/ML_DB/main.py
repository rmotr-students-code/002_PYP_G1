from db_methods import Database

if __name__ == "__main__":
    db = Database(name="Bike Inventory", 
                  filepath="bike_inventory.txt", 
                  delimiter="|",
                  fields=["id", "make", "model", "year", "cost"])
                  
    db.insert({"make": "Devinci",
                   "model": "wilson",
                   "year": 2014,
                   "cost": 3500
                   })
        
    db.insert({"make": "Giant",
                   "model": "Carbon",
                   "year": 2015,
                   "cost": 5000
                   })
                   
    db.insert({"make": "Norco",
                   "model": "Bigfoot",
                   "year": 2015,
                   "cost": 500
                   })
                   
    print db.count()
    
    print db.get({"year": 2014})