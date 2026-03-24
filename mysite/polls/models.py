from django.db import models


# Model que representa uma pergunta (tabela no banco)
class Question(models.Model):
    # Campo de texto da pergunta (VARCHAR com limite de 200 caracteres)
    question_text = models.CharField(max_length=200)

    # Data e hora de publicação da pergunta
    # O texto "date published" é usado como label no Django Admin
    pub_date = models.DateTimeField("date published")

    # Define como o objeto será exibido (ex: no admin ou shell)
    def __str__(self):
        return self.question_text


# Model que representa uma escolha/opção vinculada a uma pergunta
class Choice(models.Model):
    # Chave estrangeira para Question (relação 1:N)
    # on_delete=models.CASCADE → se a pergunta for deletada, as escolhas também serão
    # related_name="choices" → permite acessar via question.choices.all()
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="choices"
    )

    # Texto da escolha (ex: "Sim", "Não")
    choice_text = models.CharField(max_length=200)

    # Número de votos da escolha (default = 0)
    votes = models.IntegerField(default=0)

    # Representação textual da escolha
    def __str__(self):
        return self.choice_text