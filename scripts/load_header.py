import csv
from datetime import datetime
import os
from proovitoo.models import Header


def run():
    with open(os.path.join('scripts','Header_data.csv')) as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)  # Advance past the header

        Header.objects.all().delete()

        for row in reader:
            header = Header(reg_code=str(row[1]),
                            create_date=datetime.strptime(row[2],'%d.%m.%Y').date(),
                            name=str(row[0]),
                            search_string=row[3],
                            autofill_string=str(row[1]) + ' - ' + str(row[0]))
            header.save()
