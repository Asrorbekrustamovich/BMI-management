from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from datetime import datetime

class BaseModel(models.Model):
    """
    Asosiy model, umumiy maydonlar bilan.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, role=None):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, role=role)
        user.set_password(password)  # This will call the overridden set_password method
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, role=None):
        user = self.create_user(username, password, role)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.TextField(unique=True)
    password = models.TextField()  # Password will be stored in plain text
    role = models.TextField()

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['role']

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    # Override set_password to store password in plain text
    def set_password(self, raw_password):
        self.password = raw_password  # Store the password directly without hashing

    # Override check_password to compare plain text passwords
    def check_password(self, raw_password):
        return self.password == raw_password

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

# class Role(models.Model):
#     name = models.TextField()

# class UserRole(models.Model):
#     role = models.ForeignKey(Role, on_delete=models.CASCADE)
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class Position(models.Model):
    position_name = models.TextField()

    def __str__(self):
        return self.position_name  # Return the position name as the string representation

class Staff(BaseModel):
    """
    Tashkilotdagi xodimni ifodalaydi.
    """
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='staff_profile')
    full_name = models.TextField(max_length=27, null=False, help_text="To'liq ismi.")
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    salary = models.IntegerField(help_text="Maoshi.")
    email = models.EmailField(help_text="Elektron pochta manzili.")
    phone = models.TextField(max_length=27, help_text="Telefon raqami.")

    def __str__(self):
            return self.full_name
class Department(models.Model):
    """
    Tashkilotdagi bo'limni ifodalaydi.
    """
    name = models.TextField(null=False, help_text="Bo'lim nomi.")
    manager = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True, related_name='managed_departments', help_text="Bo'lim boshlig'i.")

    def __str__(self):
        return self.name





class Announcement(BaseModel):
    """
    Foydalanuvchi tomonidan e'lon qilingan xabarni ifodalaydi.
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='announcements')
    commentary = models.TextField(help_text="Asosiy sharh.")

    def __str__(self):
        return f"{self.user.username} tomonidan e'lon qilingan xabar ({self.created_at} : {self.commentary})"

class Reply(BaseModel):
    """
    E'longa javobni ifodalaydi.
    """
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE, related_name='replies')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='replies')
    commentary = models.TextField(help_text="Javob matni.")

    def __str__(self):
        return f"{self.user.username} tomonidan javob ({self.created_at})"

class Accounting(BaseModel):
    """
    Xodim uchun hisob-kitob ma'lumotlarini ifodalaydi.
    """
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='accounting_records')
    month = models.TextField()
    year = models.IntegerField(help_text="Yil.")
    incentive_money = models.IntegerField(default=0, help_text="Rag'batlantirish puli.")
    money_withheld_from_salary = models.IntegerField(default=0, help_text="Maoshdan ushlab qolingan pul.")
    reason_for_withholding = models.TextField(blank=True, null=True, help_text="Ushlab qolinish sababi.")
    money_withheld_for_income_tax = models.IntegerField(default=0, help_text="Soliqqa tortilgan pul.")
    remaining_amount = models.IntegerField(help_text="Qolgan summa.")

    def save(self, *args, **kwargs):
        """
        Qolgan summani avtomatik hisoblash.
        """
        self.remaining_amount = (self.staff.salary + self.incentive_money) - \
                                (self.money_withheld_from_salary + self.money_withheld_for_income_tax)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.staff.full_name} uchun hisob-kitob ({self.month} {self.year})"

class LeaveRequest(BaseModel):
    """
    Xodimning ta'til so'rovini ifodalaydi.
    """
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='leave_requests')
    start_date = models.DateField(help_text="Ta'til boshlanish sanasi.")
    end_date = models.DateField(help_text="Ta'til tugash sanasi.")
    reason = models.TextField(help_text="Ta'til sababi.")
    status = models.CharField(
        max_length=27,
        choices=[('Kutilmoqda', 'Kutilmoqda'), ('Tasdiqlangan', 'Tasdiqlangan'), ('Rad etilgan', 'Rad etilgan')],
        default='Kutilmoqda',
        help_text="Ta'til so'rovi holati."
    )

    def __str__(self):
        return f"{self.staff.full_name} uchun ta'til so'rovi ({self.start_date} dan {self.end_date} gacha)"

class Document(BaseModel):
    """
    Xodimga tegishli hujjatni ifodalaydi.
    """
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='documents')
    title = models.TextField(help_text="Hujjat nomi.")
    file = models.FileField(upload_to='documents/', help_text="Hujjat faylini yuklang.")
    description = models.TextField(help_text="Hujjat tavsifi.")

    def __str__(self):
        return f"Hujjat: {self.title} ({self.staff.full_name} uchun)"

class Expense(BaseModel):
    """
    Xodim tomonidan qilingan xarajatni ifodalaydi.
    """
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='expenses')
    description = models.TextField(help_text="Xarajat tavsifi.")
    amount = models.IntegerField(help_text="Xarajat miqdori.")
    date = models.DateField(help_text="Xarajat sanasi.")
    status = models.CharField(
        max_length=27,
        choices=[('Kutilmoqda', 'Kutilmoqda'), ('Tasdiqlangan', 'Tasdiqlangan'), ('Rad etilgan', 'Rad etilgan')],
        default='Pending',
        help_text="Xarajat holati."
    )

    def __str__(self):
        return f"Xarajat: {self.staff.full_name} tomonidan ({self.description})"

class Feedback(BaseModel):
    """
    Xodim tomonidan berilgan fikr-mulohazani ifodalaydi.
    """
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='feedbacks')
    message = models.TextField(help_text="Fikr-mulohaza matni.")
    response = models.TextField(blank=True, null=True, help_text="Javob.")

    def __str__(self):
        return f"Fikr-mulohaza: {self.staff.full_name} tomonidan ({self.message})"