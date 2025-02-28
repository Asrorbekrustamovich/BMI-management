from django.db import models
from datetime import datetime

class BaseModel(models.Model):
    """
    Base model with common fields.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Role(models.Model):
    name=models.TextField()
    def __str__(self):
        return super().__str__()
class CustomUser(models.Model):
    """
    Custom user model without Django's built-in authentication.
    """
    username = models.TextField(unique=True)
    password = models.TextField()  # Password stored in plain text (for demonstration)
    role =models.ForeignKey(Role,on_delete=models.CASCADE,default=3)
    def __str__(self):
        return self.username

    def set_password(self, raw_password):
        """
        Manually set the password (stored in plain text for demonstration).
        """
        self.password = raw_password

    def check_password(self, raw_password):
        """
        Manually check the password (plain text comparison).
        """
        return self.password == raw_password

    def __str__(self):
        return self.username

class Department(models.Model):
    Department_name=models.TextField(null=True,blank=True)
    def __str__(self):
        return self.Department_name
    
class Position(models.Model):
    position_name = models.TextField()
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    def __str__(self):
        return self.position_name

class Staff(BaseModel):
    """
    Represents a staff member in the organization.
    """
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='staff_profile')
    full_name = models.TextField(max_length=27, null=False, help_text="Full name.")
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    salary = models.IntegerField(help_text="Salary.")
    email = models.EmailField(help_text="Email address.")
    phone = models.TextField(max_length=27, help_text="Phone number.")

    def __str__(self):
        return self.full_name
class Announcement(BaseModel):
    """
    Represents an announcement made by a user.
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='announcements')
    commentary = models.TextField(help_text="Main commentary.")

    def __str__(self):
        return f"{self.user.username} tomonidan e'lon qilingan xabar ({self.created_at} : {self.commentary})"
class Accounting(BaseModel):
    """
    Represents accounting records for a staff member.
    """
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='accounting_records')
    month = models.TextField()
    year = models.IntegerField(help_text="Year.")
    incentive_money = models.IntegerField(default=0, help_text="Incentive money.")
    money_withheld_from_salary = models.IntegerField(default=0, help_text="Money withheld from salary.")
    reason_for_withholding = models.TextField(blank=True, null=True, help_text="Reason for withholding.")
    money_withheld_for_income_tax = models.IntegerField(default=0, help_text="Money withheld for income tax.")
    remaining_amount = models.IntegerField(help_text="Remaining amount.")

    def save(self, *args, **kwargs):
        """
        Automatically calculate the remaining amount.
        """
        self.remaining_amount = (self.staff.salary + self.incentive_money) - \
                                (self.money_withheld_from_salary + self.money_withheld_for_income_tax)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.staff.full_name} uchun hisob-kitob ({self.month} {self.year})"
class LeaveRequest(BaseModel):
    """
    Represents a leave request by a staff member.
    """
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='leave_requests')
    start_date = models.DateField(help_text="Start date of leave.")
    end_date = models.DateField(help_text="End date of leave.")
    reason = models.TextField(help_text="Reason for leave.")
    status = models.CharField(
        max_length=27,
        choices=[('Kutilmoqda', 'Kutilmoqda'), ('Tasdiqlangan', 'Tasdiqlangan'), ('Rad etilgan', 'Rad etilgan')],
        default='Kutilmoqda',
        help_text="Leave request status."
    )

    def __str__(self):
        return f"{self.staff.full_name} uchun ta'til so'rovi ({self.start_date} dan {self.end_date} gacha)"
class Document(BaseModel):
    """
    Represents a document associated with a staff member.
    """
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='documents')
    title = models.TextField(help_text="Document title.")
    file = models.FileField(upload_to='documents/', help_text="Upload document file.")
    description = models.TextField(help_text="Document description.")

    def __str__(self):
        return f"Hujjat: {self.title} ({self.staff.full_name} uchun)"
class Expense(BaseModel):
    """
    Represents an expense made by a staff member.
    """
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='expenses')
    description = models.TextField(help_text="Expense description.")
    amount = models.IntegerField(help_text="Expense amount.")
    date = models.DateField(help_text="Expense date.")
    status = models.CharField(
        max_length=27,
        choices=[('Kutilmoqda', 'Kutilmoqda'), ('Tasdiqlangan', 'Tasdiqlangan'), ('Rad etilgan', 'Rad etilgan')],
        default='Pending',
        help_text="Expense status."
    )

    def __str__(self):
        return f"Xarajat: {self.staff.full_name} tomonidan ({self.description})"
class Message(models.Model):
    sender = models.ForeignKey(CustomUser, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomUser, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)    
    class Meta:
        db_table = 'message'

    def __str__(self):
        return f"Message from {self.sender} to {self.receiver} at {self.timestamp}"