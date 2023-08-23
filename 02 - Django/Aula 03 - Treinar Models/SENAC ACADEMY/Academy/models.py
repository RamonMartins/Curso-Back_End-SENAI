from django.db import models

class Aluno(models.Model):
    lista_sexo = [
        ("M", "Masculino"),
        ("F", "Feminino"),
    ]
    nome = models.CharField(max_length=50, verbose_name="Nome do Aluno")
    idade = models.IntegerField()
    data_de_nascimento = models.DateField()
    status = models.BooleanField(default=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    sexo = models.CharField(max_length=1, choices = lista_sexo)
    sobre_mim = models.TextField()
    email = models.EmailField(blank=True, null=True) #blank=True, null=True -> permite que o usuário deixe em branco este campo

    def __str__(self):
        return self.nome

class DadoPessoal(models.Model):
    cpf = models.CharField(max_length=14)
    rg = models.CharField(max_length=10)
    aluno = models.OneToOneField(Aluno, on_delete=models.CASCADE)

    def __str__(self):
        return self.cpf

class Professor(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.nome
    
class Curso(models.Model):
    nome = models.CharField(max_length=100)
    conteudo = models.TextField()
    carga_horaria = models.TimeField()
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE) # relacionamento 1 para muitos
    alunos = models.ManyToManyField(Aluno)

    def __str__(self):
        return self.nome