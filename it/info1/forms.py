from django.forms import Form
from django import forms


class CreateNameForm(Form):
    firstname = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Арсен'}))
    secondname = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Енсегенов'}))  
class CreateBirthForm(Form):
    date_of_birth = forms.DateField(required=True,
                               widget=forms.DateInput(attrs={'class': 'form-control',  'type': 'date'}))
    place_of_birth = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Сартогай'}))
    
class CreateInfoForm(Form):
    specialization = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Бакалавр по специальности Математика '}))
    orga_of_education = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'КазНУ им. Аль-Фараби'}))
    
    year_of_graduation = forms.IntegerField(required=True,
                               widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                 'placeholder': '2008', 'type':'number'}))
    
class CreateWorkForm(Form):
    organization = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Декан '}))
    address = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Алматы Менеджмент Университет, ул.Розыбакиева, 227'}))
    
class CreatePracticeForm(Form):
    experience = forms.IntegerField(required=True,
                               widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '15 год '}))
    
class CreateCriminalForm(Form):
    criminal_record = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Да. В 2015 году я был осужден за кражу в крупном размере и получил условный срок на 2 года. Суд был проведен в г. Москва или Нет '}))
    
class CreateMedicineForm(Form):
    medicine_number = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'АА 12345678  '}))

    
class CreateMasterForm(Form):
    master_degree = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' КазНу им Аль-Фараби, магистр математики 2010 или Нет '}))
    
class CreateDoctorForm(Form):
    doctor_profile = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'PhD, по специальности "Информационные системы", 2015 г. или Нет  '}))
    
class CreatePhdForm(Form):
    phd_record = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Yes or No   '}))

class CreateProfessorForm(Form):
    docent_professor = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'КазНИТУ им. К.И.Сатпаева, 6D070400 – Вычислительная техника и программное обеспечение, 2019г или Нет  '})) 
class CreateSportForm(Form):
    sport_degree = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '«Заслуженный тренер», 2015 или Нет  '}))
class CreateSubjectForm(Form):
    subject_of_teaching = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ИТ-стартап 1 (ideation/validation), ИТ-стартап 2 (запуск проекта, MVP, Web проект), Лаборатория Start-up '}))