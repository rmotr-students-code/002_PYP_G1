from database_ import *

def main():
    database = Database(name='Players',
                        filepath='/home/ubuntu/workspace/practical-4/brendan-paulo/database.txt', 
                        delimiter='|',
                        fields=['Id', 'Ranking', 'First_Name', 'Last_Name',
                                'Country', 'Prize_Money'])

    database.insert_db({'Id': '1',
                        'Ranking': '1',
                        'First_Name': 'Roger',
                        'Last_Name': 'Federer',
                        'Country': 'Switzerland',
                        'Prize_Money': '$1000000'})

    database.insert_db({"Id": '0',
                        "Ranking": '2',
                        "First_Name": 'Roger',
                        "Last_Name": 'Emery',
                        "Country": 'Straya',
                        "Prize_Money": '90000000'
    })

    database.insert_db({"Id": '0',
                        "Ranking": '4',
                        "First_Name": 'DA',
                        "Last_Name": 'GAawG',
                        "Country": 'Straya',
                        "Prize_Money": '1'
    })

    print database.count_db()
    print database.query_db({'Id': '1'})
    print database.get_db({'First_Name': 'DA'})
    database.update_db({'Id': '2'}, {'First_Name': 'Santi'}, True) #NOT WORKING FOR ID
    # database.remove_db({'Country': 'Switzerland'}, True)

main()