from csv import reader

class cache:
    def create_cache():
        
        x_path = []
        y_labels = []

        with open('src\imdb_meta\metadata.csv', 'r') as read_obj:
            csv_reader = reader(read_obj)
            
            for row in csv_reader:
                x_path = "src/imdb/" + str(row[0])
                dob = str(row[1]).split("-")[2]
                gender = str(row[2])
                y_labels = dob + "and" + gender

        return [x_path, y_labels]