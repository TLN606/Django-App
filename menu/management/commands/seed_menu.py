from django.core.management.base import BaseCommand

from menu.models import Category, Dish

SAMPLE = {
    'Cơm': [
        ('Cơm tấm sườn bì chả', 45000),
        ('Cơm gà xối mỡ', 50000),
        ('Cơm chiên dương châu', 40000),
    ],
    'Bún - Phở': [
        ('Phở bò tái', 55000),
        ('Bún bò Huế', 50000),
        ('Bún chả Hà Nội', 52000),
    ],
    'Ăn vặt': [
        ('Bánh mì thịt nướng', 25000),
        ('Gỏi cuốn tôm thịt (2 cuốn)', 30000),
        ('Khoai tây chiên', 28000),
    ],
    'Đồ uống': [
        ('Trà đào cam sả', 35000),
        ('Cà phê sữa đá', 25000),
        ('Nước cam ép', 30000),
        ('Sinh tố bơ', 38000),
    ],
}


class Command(BaseCommand):
    help = 'Thêm dữ liệu mẫu cho thực đơn (chạy nhiều lần không bị trùng, không có ảnh).'

    def handle(self, *args, **options):
        created = 0
        for cat_name, dishes in SAMPLE.items():
            category, _ = Category.objects.get_or_create(name=cat_name)
            for name, price in dishes:
                _, new = Dish.objects.get_or_create(
                    category=category, name=name, defaults={'price': price}
                )
                created += new
        self.stdout.write(self.style.SUCCESS(f'Đã thêm {created} món mới.'))
