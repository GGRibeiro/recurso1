from django.db import models


class Semestre(models.Model):
    nome = models.CharField(max_length=50)
    semestre = models.IntegerField(default=1)
    ects = models.IntegerField(default=1)
    estrelas = models.IntegerField(default=1)
    professores = models.CharField(max_length=50)

    def __str__(self):
        return f"Nome: {self.nome}, Semestre: {self.semestre}, ECTS: {self.ects}, Estrelas: {self.estrelas}, Professores: {self.professores}"




class Tarefa(models.Model):
    titulo = models.CharField(max_length=30)
    prioridade = models.IntegerField(default=1)
    concluida = models.BooleanField(default=False)
    criado = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.titulo[:20]

class Comentario(models.Model):
    nome = models.CharField(max_length=20)
    cidade = models.CharField(max_length=20)
    pais = models.CharField(max_length=20)
    data = models.DateField(auto_now_add=True)
    titulo = models.CharField(max_length=20)
    comentario = models.TextField(max_length=255)
    def __str__(self):
        return self.nome

            #f"Nome: {self.nome}, cidade {self.cidade}, pais {self.pais}, data: {self.data}, comentario: {self.comentario}"

















class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"


class Flight(models.Model):
    origin = models.ForeignKey(Airport,
                               on_delete=models.CASCADE,
                               related_name="departures")
    destination = models.ForeignKey(Airport,
                                    on_delete=models.CASCADE,
                                    related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"


class Passenger(models.Model):
    name = models.CharField(max_length=20)
    flights = models.ManyToManyField(
        Flight,
        blank=True,
        related_name='passengers'
    )

    def __str__(self):
        return self.name







