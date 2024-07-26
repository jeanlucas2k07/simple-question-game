import os
import random

again = True

while again:
    os.system('cls')

    perguntas = [
        ['Qual foi o primeiro time a ser campeão continental do mundo?', 'Vasco da Gama', 'Real Madrid', 'Flamengo', 'Villa Real', 'a'],
        ['Quem foi o primeiro presidente do Brasil?', 'Getúlio Vargas', 'Juscelino Kubitschek', 'Deodoro da Fonseca', 'Pedro II', 'c'],
        ['Qual é o maior planeta do sistema solar?', 'Terra', 'Marte', 'Júpiter', 'Saturno', 'c'],
        ['Quem pintou a Mona Lisa?', 'Pablo Picasso', 'Leonardo da Vinci', 'Vincent van Gogh', 'Michelangelo', 'b'],
        ['Quantos elementos químicos naturais a Terra possui?', '110', '92', '118', '102', 'b'],
        ['Qual é o número atômico do carbono?', '6', '8', '12', '14', 'a'],
        ['Quem escreveu a peça de teatro "Romeu e Julieta"?', 'William Shakespeare', 'Charles Dickens', 'Jane Austen', 'Mark Twain', 'a'],
        ['Em que país podemos encontrar a Torre Eiffel?', 'Inglaterra', 'Itália', 'França', 'Espanha', 'c'],
        ['Qual é o maior rio do mundo em volume de água?', 'Rio Amazonas', 'Rio Nilo', 'Rio Mississipi', 'Rio Yangtze', 'a'],
        ['Quem descobriu a penicilina?', 'Alexander Fleming', 'Louis Pasteur', 'Marie Curie', 'Albert Einstein', 'a'],
        ['Qual é a capital do Canadá?', 'Toronto', 'Montreal', 'Vancouver', 'Ottawa', 'd'],
        ['Quem foi o primeiro astronauta a pisar na Lua?', 'Buzz Aldrin', 'Neil Armstrong', 'Yuri Gagarin', 'Alan Shepard', 'b'],
        ['Qual é o metal mais caro do mundo?', 'Ouro', 'Platina', 'Ródio', 'Irídio', 'c'],
        ['Quem escreveu o livro "A Menina que Roubava Livros"?', 'Stephen King', 'J.K. Rowling', 'Markus Zusak', 'Harper Lee', 'c'],
        ['Quantos países formam o Reino Unido?', '1', '2', '3', '4', 'd'],
        ['Qual é a cor do cavalo branco de Napoleão?', 'Branco', 'Preto', 'Cinza', 'Marrom', 'a'],
        ['Qual é a cidade mais populosa do mundo?', 'Tóquio', 'Nova York', 'Xangai', 'Pequim', 'a'],
        ['Em que ano a Segunda Guerra Mundial começou?', '1914', '1939', '1941', '1945', 'b'],
        ['Qual é o nome completo de Van Gogh?', 'Vincent Willem van Gogh', 'Vincent van der Woodsen', 'Vincent van Halen', 'Vincent van Dyke', 'a'],
        ['Qual é a capital da Austrália?', 'Sydney', 'Melbourne', 'Canberra', 'Brisbane', 'c'],
        ['Quem é o autor de "O Pequeno Príncipe"?', 'Antoine de Saint-Exupéry', 'Voltaire', 'Victor Hugo', 'Jules Verne', 'a'],
        ['Qual é a maior ilha do mundo?', 'Ilha de Java', 'Ilha de Borneo', 'Ilha de Sumatra', 'Groenlândia', 'd'],
        ['Qual é o maior deserto do mundo?', 'Deserto do Saara', 'Deserto de Gobi', 'Deserto do Atacama', 'Deserto da Arábia', 'a'],
        ['Qual é a velocidade da luz no vácuo?', '300.000 km/s', '150.000 km/s', '500.000 km/s', '1.000.000 km/s', 'a'],
        ['Qual é o animal terrestre mais rápido?', 'Guepardo', 'Antílope', 'Lebre', 'Lobo', 'a'],
        ['Quem escreveu "O Pequeno Príncipe"?', 'Antoine de Saint-Exupéry', 'Voltaire', 'Victor Hugo', 'Jules Verne', 'a'],
        ['Qual é a capital do Brasil?', 'Rio de Janeiro', 'São Paulo', 'Brasília', 'Salvador', 'c'],
        ['Qual é o metal líquido à temperatura ambiente?', 'Ferro', 'Cobre', 'Mercúrio', 'Zinco', 'c'],
        ['Qual é a maior cordilheira do mundo?', 'Cordilheira dos Andes', 'Cordilheira do Himalaia', 'Cordilheira do Atlas', 'Cordilheira dos Apalaches', 'a'],
        ['Quem descobriu a América?', 'Cristóvão Colombo', 'Amerigo Vespucci', 'Vasco da Gama', 'Fernão de Magalhães', 'a'],
        ['Qual é o maior oceano do mundo?', 'Oceano Índico', 'Oceano Atlântico', 'Oceano Ártico', 'Oceano Pacífico', 'd'],
        ['Qual é o símbolo químico do ouro?', 'Au', 'Ag', 'Fe', 'Cu', 'a'],
        ['Qual é o segundo planeta do sistema solar a partir do Sol?', 'Mercúrio', 'Vênus', 'Terra', 'Marte', 'b'],
        ['Qual é o maior mamífero terrestre?', 'Elefante africano', 'Baleia azul', 'Rinoceronte branco', 'Girafa', 'b'],
        ['Qual é a capital da Argentina?', 'Santiago', 'Montevidéu', 'Lima', 'Buenos Aires', 'd'],
        ['Qual é o primeiro livro da Bíblia?', 'Gênesis', 'Êxodo', 'Levítico', 'Números', 'a'],
        ['Quantos elementos químicos a tabela periódica possui?', '108', '118', '128', '138', 'b'],
        ['Quem foi o primeiro presidente dos Estados Unidos?', 'Thomas Jefferson', 'George Washington', 'Abraham Lincoln', 'John Adams', 'b'],
        ['Qual é o nome da famosa operação militar que resultou no desembarque das forças aliadas na Normandia, durante a Segunda Guerra Mundial?', 'Operação Neptuno', 'Operação Marte', 'Operação Overlord', 'Operação Tempestade', 'c'],
        ['Quem foi o primeiro ser humano a viajar para o espaço?', 'Neil Armstrong', 'Yuri Gagarin', 'Buzz Aldrin', 'Alan Shepard', 'b'],
        ['Quem escreveu "Os Lusíadas"?', 'Fernando Pessoa', 'Luís Vaz de Camões', 'Eça de Queirós', 'Miguel de Cervantes', 'b'],
        ['Qual é o maior estado brasileiro em área territorial?', 'Amazonas', 'Minas Gerais', 'Bahia', 'São Paulo', 'a'],
        ['Qual é o ácido encontrado no vinagre?', 'Ácido acético', 'Ácido sulfúrico', 'Ácido cítrico', 'Ácido fórmico', 'a'],
        ['Quantos anos tem um século?', '50 anos', '75 anos', '100 anos', '200 anos', 'c'],
        ['Qual é a capital do México?', 'Cidade do México', 'Guadalajara', 'Monterrey', 'Puebla', 'a'],
        ['Qual é o maior porto marítimo do Brasil?', 'Porto de Santos', 'Porto de Rio de Janeiro', 'Porto de Paranaguá', 'Porto de Salvador', 'a'],
        ['Quem pintou "A Persistência da Memória", conhecido como "Os Relógios Derretidos"?', 'Pablo Picasso', 'Salvador Dalí', 'Vincent van Gogh', 'Henri Matisse', 'b'],
        ['Qual é a capital do Japão?', 'Tóquio', 'Osaka', 'Quioto', 'Nagoya', 'a'],
        ['Qual é a primeira letra do alfabeto grego?', 'Alfa', 'Beta', 'Gama', 'Delta', 'a'],
        ['Quantos ossos tem o corpo humano adulto?', '206', '196', '216', '226', 'a'],
        ['Qual é o segundo maior país do mundo em área territorial?', 'China', 'Estados Unidos', 'Canadá', 'Brasil', 'c']
    ]
    alternativas = ['a', 'b', 'c', 'd']
    perguntas_respondidas = list()

    acertos = 0

    print('='*20, 'Questionário Conhecimentos Gerais', '='*20)
    nome = input('Por favor, digite seu nome: ')

    os.system('cls')
    p = 0

    for pergunta in range(10):
        random.shuffle(perguntas)
        print('='*20, 'Questionário Conhecimentos Gerais', '='*20)

        if perguntas_respondidas != []:
            for i in perguntas_respondidas:
                if i == perguntas[pergunta]:
                    pergunta += 1

        resposta_certa = perguntas[pergunta][5]
        
        print(f'{nome},',perguntas[pergunta][0])

        print('A)', perguntas[pergunta][1])
        print('B)', perguntas[pergunta][2])
        print('C)', perguntas[pergunta][3])
        print('D)', perguntas[pergunta][4])

        resposta = input(f'Qual a alternativa correta? | Acertos: {acertos} | Pergunta {p+1} de {10}\n').lower().strip()

        if resposta == resposta_certa or resposta == perguntas[pergunta][alternativas.index(resposta_certa)+1].lower():
            print('Acertou!')
            acertos += 1
        else:
            print(f'Você errou!\nA resposta certa era a alternativa {resposta_certa}')

        perguntas_respondidas.append(perguntas[pergunta])
        p += 1
        input('='*75)

        os.system('cls')


    print('='*20, 'Questionário Conhecimentos Gerais', '='*20)

    if acertos == 10:
        print('Parabéns Alberto Áinstéin, você acerotu todas!', end=' ')
    else:
        print(f'Sua pontução foi de {acertos} pontos.\n')

    print('='*35, 'FIM', '='*35)

    dnv = input('Quer jogar de novo? (S/N)').lower().strip()

    if dnv == 'n':
        again = False
    else:
        continue