from django.db import models


class Aulas(models.Model):
    titulo = models.TextField(blank=False, null=False)
    link = models.TextField(blank=False, null=False)
    material = models.FileField(upload_to="aulas/materiais", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Aulas"

    def __str__(self):
        return f'{self.id} - {self.titulo}'


    def popular_tabela_aulas(self):
        Aulas.objects.create(
            id=1,
            titulo='Sistema de Equações',
            link='pbFZW1eTnkk')
        Aulas.objects.create(
            id=2,
            titulo='Introdução ao Escalonamento',
            link='wvrMO_C-cdE')
        Aulas.objects.create(
            id=3,
            titulo='Pivô e Escalonamento',
            link='a_IfBj7Gdfs')
        Aulas.objects.create(
            id=4,
            titulo='Discussão de Sistema',
            link='ganCbJlJTbE')
        Aulas.objects.create(
            id=5,
            titulo='Resolução de Sistema com Escalonamento',
            link='eTEPbbhL2hM')
        Aulas.objects.create(
            id=6,
            titulo='Discussão de Sistema - Gauss',
            link='IQj37-tv5e4')
        Aulas.objects.create(
            id=7,
            titulo='Resolução de Sistema por Gauss',
            link='YXPuZFWGmyw')
        Aulas.objects.create(
            id=8,
            titulo='Vetores',
            link='0Gp1QgdhujE')
        Aulas.objects.create(
            id=9,
            titulo='Operações com vetores',
            link='z1DQ3vXvGLw')
        Aulas.objects.create(
            id=10,
            titulo='Combinação Linear de Vetores',
            link='eB7KJKV2k-E')
        Aulas.objects.create(
            id=11,
            titulo='Combinação Linear - Ex1',
            link='8peVbC0j6aI')
        Aulas.objects.create(
            id=12,
            titulo='Combinação Linear - Ex2',
            link='MYH54JuIj0Y')
        Aulas.objects.create(
            id=13,
            titulo='Combinação Linear - Ex3',
            link='7MVG47_THHg')
        Aulas.objects.create(
            id=14,
            titulo='Combinação Linear - Ex4',
            link='K6yWkn59-JI')
        Aulas.objects.create(
            id=15,
            titulo='Dependência Linear',
            link='1NQgheFnX9A')
        Aulas.objects.create(
            id=16,
            titulo='Dependência Linear - Ex 1',
            link='jA-6Xcw8__E')
        Aulas.objects.create(
            id=17,
            titulo='Dependência Linear - Ex 2',
            link='wgIGAY5nQk0')
        Aulas.objects.create(
            id=18,
            titulo='Dependência Linear - Ex 3',
            link='V7ysHtEi1q4')
        Aulas.objects.create(
            id=19,
            titulo='Dependência Linear - Ex 4',
            link='LigrD3eurZs')
        Aulas.objects.create(
            id=20,
            titulo='Espaço Vetorial - Ex1',
            link='e8kAs458cVI')
        Aulas.objects.create(
            id=21,
            titulo='Espaço Vetorial - Ex2',
            link='KXVCjPjgpq4')
        Aulas.objects.create(
            id=22,
            titulo='Subespaço Vetorial - Ex1',
            link='XxUWCQaVwKM')
        Aulas.objects.create(
            id=23,
            titulo='Subespaço Vetorial - Ex2',
            link='HnGwjpfp3Gc')
        Aulas.objects.create(
            id=24,
            titulo='Subespaço Vetorial - Ex3',
            link='j9XnjqEUUkQ')
        Aulas.objects.create(
            id=25,
            titulo='Subespaço Vetorial - Ex4',
            link='AtMFysEdlag')
        Aulas.objects.create(
            id=26,
            titulo='Subespaço Vetorial - Ex5',
            link='YAxsFPVv3ds')
        Aulas.objects.create(
            id=27,
            titulo='Subespaço Gerado - Ex.1',
            link='lqfAoCG1CMY')
        Aulas.objects.create(
            id=28,
            titulo='Subespaço Gerado - Ex.2',
            link='zE9g8XT2oMg')
        Aulas.objects.create(
            id=29,
            titulo='Subespaço Gerado - Ex.3',
            link='WQiEA4_PbbU')
        Aulas.objects.create(
            id=30,
            titulo='Base de um Espaço Vetorial',
            link='1s1d_z5iQbk')
        Aulas.objects.create(
            id=31,
            titulo='Como calcular uma base geradora',
            link='H_yOpYU7hTY')
        Aulas.objects.create(
            id=32,
            titulo='Extraindo a base geradora de um subespaço. Exercício 1',
            link='5dst5A_ch0k')
        Aulas.objects.create(
            id=33,
            titulo='Extraindo a base geradora de um subespaço. Exercício 2',
            link='5kAQ_r1yWXg')
        Aulas.objects.create(
            id=34,
            titulo='Extraindo a base geradora de um subespaço. Exercício 3',
            link='ELo65Qjv5Dg')
        Aulas.objects.create(
            id=35,
            titulo='Extraindo a base geradora de um subespaço. Exercício 4',
            link='FUOxfqt8zrM')
        Aulas.objects.create(
            id=36,
            titulo='Como extrair uma base geradora de um conjunto de vetores',
            link='shH9uTczXDI')
        Aulas.objects.create(
            id=37,
            titulo='Subespaço gerado a partir de um conjunto de vetores',
            link='ZRuJXCG2CpI')
        Aulas.objects.create(
            id=38,
            titulo='Mudança de base geradora',
            link='muA2fcZGQXs')
        Aulas.objects.create(
            id=39,
            titulo='Mudança de base sem uso de matriz inversa',
            link='U55o4HTmPF0')
        Aulas.objects.create(
            id=40,
            titulo='Mudança de base . Vetor com 3 componentes',
            link='Qta17OWjsFs')
        Aulas.objects.create(
            id=41,
            titulo='Dedução da Fórmula Matriz Mudança de base',
            link='4bc1We6Akkc')
        Aulas.objects.create(
            id=42,
            titulo='Mudança de Base de um Vetor com a Matriz Mudança de base',
            link='3F3E8DcivKg')
        Aulas.objects.create(
            id=43,
            titulo='Mudança de base demonstrado graficamente',
            link='9UozHl91Zdg')
        Aulas.objects.create(
            id=44,
            titulo='Introdução a Transformação Linear',
            link='O3rou_UUIIg')
        Aulas.objects.create(
            id=45,
            titulo='Transformação Linear',
            link='h96mnXdcsaI')
        Aulas.objects.create(
            id=46,
            titulo='Transformação Linear',
            link='ZB28kpo0VTQ')
        Aulas.objects.create(
            id=47,
            titulo='Propriedades da Transformação Linear',
            link='xYAbFnh4Rco')
        Aulas.objects.create(
            id=48,
            titulo='Propriedades da Transformação Linear',
            link='6EM6dBEGc-g')
        Aulas.objects.create(
            id=49,
            titulo='Dada imagem, ache a Transformação Linear',
            link='aera-zZlBMs')
        Aulas.objects.create(
            id=50,
            titulo='Como obter a lei de uma Transformação Linear',
            link='igvfXiYiwAY')
        Aulas.objects.create(
            id=51,
            titulo='Como obter a lei de uma Transformação Linear',
            link='inBnKDHEJ2s')


class Questoes(models.Model):
    questao = models.TextField(blank=False, null=False)
    alt1 = models.TextField(blank=False, null=False)
    alt2 = models.TextField(blank=False, null=False)
    alt3 = models.TextField(blank=False, null=False)
    alt4 = models.TextField(blank=False, null=False)
    resposta_correta = models.TextField(blank=False, null=False)
    aula_referente = models.ForeignKey(Aulas, default=None, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Qugitestão"
        verbose_name_plural = "Questões"

    def __str__(self):
        return f'{self.questao} {self.resposta_correta}'

