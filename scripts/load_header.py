import csv
import datetime
import os
from proovitoo.models import Header


def run():
    with open(os.path.join('scripts', 'Header_data.csv')) as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)  # Advance past the header

        Header.objects.all().delete()

        for row in reader:
            header = Header(reg_code=str(row[0]),
                            create_date=datetime.date.today(),
                            name=str(row[1]),
                            search_string='',
                            autofill_string=str(row[0]) + ' - ' + str(row[1]))
            header.save()
