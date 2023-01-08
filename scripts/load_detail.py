import csv
from datetime import datetime
import os

from django.shortcuts import get_object_or_404

from proovitoo.models import Detail, Header


def run():
    with open(os.path.join('scripts', 'Detail_data.csv')) as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)  # Advance past the header

        Detail.objects.all().delete()

        for row in reader:
            h = get_object_or_404(Header, pk=row[0])
            print(row[2])
            if len(row[2]) == 0:
                pp=False
            else:
                pp=True
            print(pp)
            detail = Detail(reg_code=h,
                            shareholder_first_name = row[2],
                            shareholder_last_name = str(row[3]),
                            shareholder_company_name=row[5],
                            shareholder_company_reg_code = row[6],
                            capital = row[1],
                            id_code = row[4],
                            founder = True,
                            physical_person =pp,
                            autofill_string = row[7])

            detail.save()

