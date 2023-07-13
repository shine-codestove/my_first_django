from django.db import models, transaction
import csv


class PriceFile(models.Model):
    class Meta:
        db_table = 'price_file'

    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # 실제 save() 를 호출
        self.save_price_table(self.file.path)

    @transaction.atomic()
    def save_price_table(self, file_url):
        from myapp.models.price_table import PriceTable
        PriceTable.objects.all().delete()

        new_price_list = []

        with open(file_url, 'r') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
            area_row = rows[0][1:]
            # 각 행 순회
            for i, row in enumerate(rows[2:]):
                start = row[0]
                from_to_price = {'start': start}

                # 행의 각 열에 접근
                for j, price in enumerate(row[1:]):
                    end = area_row[j]
                    from_to_price['end'] = end
                    from_to_price['price'] = price
                    print(from_to_price)

                    price_table = PriceTable(start_area=start, end_area=end, price=int(price) if not price == '' else 0)
                    new_price_list.append(price_table)

        PriceTable.objects.bulk_create(new_price_list)
