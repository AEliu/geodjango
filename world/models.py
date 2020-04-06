from django.db import models
from django.utils import timezone


# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=10)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '联系人'


class ConstructionUnit(models.Model):
    corp_name = models.CharField(max_length=200, null=False, unique=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    introduction = models.TextField(max_length=500)

    def __str__(self):
        return self.corp_name

    class Meta:
        verbose_name = '建设单位'


class DesignInstitute(models.Model):
    corp_name = models.CharField(max_length=200, null=False, unique=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    introduction = models.TextField(max_length=500)

    def __str__(self):
        return self.corp_name

    class Meta:
        verbose_name = '设计院'


class Address(models.Model):
    region = models.CharField(max_length=15)
    road = models.CharField(max_length=15)
    boundaries = models.TextField(max_length=300)

    def __str__(self):
        return self.region + ' ' + self.road

    class Meta:
        verbose_name = '地址'


class Department(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
    section = models.CharField(max_length=15)

    def __str__(self):
        return (self.name + ': ' + self.section)

    class Meta:
        verbose_name = '部门'


class Staff(models.Model):
    name = models.CharField(max_length=10)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField()
    section = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '部门参会人员'


class Expert(models.Model):
    name = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    section = models.CharField(max_length=50)
    title = models.CharField(max_length=15)
    intro = models.TextField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '专家'


class ExpertReview(models.Model):
    review_data = models.DateField()
    experts = models.ManyToManyField(
        Expert,
        through='ReviewCom'
    )
    staffs = models.ManyToManyField(Staff)

    def __str__(self):
        return str(self.review_data) + '专家评审会'

    class Meta:
        verbose_name = '专家评审会'


class ReviewCom(models.Model):
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE)
    review = models.ForeignKey(ExpertReview, on_delete=models.CASCADE)
    is_leader = models.BooleanField(default=False)

    def __str__(self):
        return str(self.review.review_data) + '专家评审会专家组成员'

    class Meta:
        verbose_name = '专家组成员'


class Commission(models.Model):
    com_date = models.DateField()
    session = models.IntegerField(verbose_name='规委会期数')
    notes = models.TextField('会议纪要', max_length=1000)
    grade = models.CharField('市级or 管委会？', max_length=15)

    def __str__(self):
        return str(self.com_date) + self.grade + '规委会'

    class Meta:
        verbose_name = '规委会'
        ordering = [
            '-com_date',
        ]


class Project(models.Model):
    name = models.CharField(max_length=50)
    apply_date = models.DateField(default=timezone.now)
    construction_unit = models.ForeignKey(ConstructionUnit, on_delete=models.CASCADE)
    institute = models.ForeignKey(DesignInstitute, on_delete=models.CASCADE)
    review = models.ForeignKey(ExpertReview, on_delete=models.CASCADE)
    commission = models.ForeignKey(Commission, on_delete=models.CASCADE)
    intro = models.TextField(max_length=500)
    addr = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '项目'
        ordering = [
            '-apply_date',
        ]

