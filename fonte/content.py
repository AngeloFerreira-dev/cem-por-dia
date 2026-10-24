# 100 frases por dia — conteúdo.
# Cada dia tem 10 ondas de 10 frases. Cada onda usa um "molde" (padrão de frase do método
# de frases do Mikkel): você aprende o molde uma vez e troca só a peça final.
# Item: (peça em inglês, peça em português, emoji da cena). [a|o] = forma feminina|masculina.
# mod = como a cena desenha o sentido (querer, precisar, gostar, passado, futuro...).

from base import W, FREE

DAYS = [
 dict(n=1, name='Sobrevivência', tag='O básico para não travar em lugar nenhum', waves=[
  W('Cumprimentos', FREE, FREE, 'talk', 'street', [
    ('Hello!', 'Olá!', '👋'), ('Good morning!', 'Bom dia!', '🌅'), ('Good night!', 'Boa noite!', '🌙'),
    ('Thank you very much.', 'Muito [obrigada|obrigado].', '🙏'), ("You're welcome.", 'De nada.', '😊'),
    ('Excuse me.', 'Com licença.', '🙋'), ("I'm sorry.", 'Desculpa.', '😔'), ('See you later!', 'Até mais!', '🚶'),
    ('Nice to meet you.', 'Prazer em te conhecer.', '🤝'), ('How are you?', 'Como você está?', '🙂')]),
  W('Eu quero...', 'I want {x}.', 'Eu quero {x}.', 'want', 'cafe', [
    ('a coffee', 'um café', '☕'), ('some water', 'água', '💧'), ('a sandwich', 'um sanduíche', '🥪'),
    ('a pizza', 'uma pizza', '🍕'), ('an ice cream', 'um sorvete', '🍦'), ('a new phone', 'um celular novo', '📱'),
    ('a ticket', 'um ingresso', '🎟️'), ('to go home', 'ir para casa', '🏠'), ('to sleep', 'dormir', '🛏️'),
    ('to learn English', 'aprender inglês', '📚')]),
  W('Eu preciso...', 'I need {x}.', 'Eu preciso {x}.', 'need', 'street', [
    ('a taxi', 'de um táxi', '🚕'), ('help', 'de ajuda', '🆘'), ('a doctor', 'de um médico', '🩺'),
    ('a charger', 'de um carregador', '🔌'), ('money', 'de dinheiro', '💵'), ('a pen', 'de uma caneta', '🖊️'),
    ('to rest', 'descansar', '🛋️'), ('to call my mom', 'ligar para minha mãe', '📞'),
    ('to go to the bank', 'ir ao banco', '🏦'), ('to find a pharmacy', 'encontrar uma farmácia', '💊')]),
  W('Eu gosto de...', 'I like {x}.', 'Eu gosto {x}.', 'like', 'park', [
    ('music', 'de música', '🎵'), ('dogs', 'de cachorros', '🐶'), ('the beach', 'da praia', '🏖️'),
    ('chocolate', 'de chocolate', '🍫'), ('rainy days', 'de dias de chuva', '🌧️'), ('reading books', 'de ler livros', '📚'),
    ('cooking', 'de cozinhar', '🍳'), ('playing video games', 'de jogar videogame', '🎮'),
    ('this city', 'desta cidade', '🏙️'), ('travelling', 'de viajar', '✈️')]),
  W('Eu não gosto de...', "I don't like {x}.", 'Eu não gosto {x}.', 'dislike', 'street', [
    ('the cold', 'do frio', '🥶'), ('spiders', 'de aranhas', '🕷️'), ('waking up early', 'de acordar cedo', '⏰'),
    ('traffic', 'de trânsito', '🚦'), ('onions', 'de cebola', '🧅'), ('loud noise', 'de barulho alto', '📢'),
    ('waiting in line', 'de esperar na fila', '🧍'), ('Mondays', 'de segunda-feira', '📅'),
    ('horror movies', 'de filmes de terror', '👻'), ('spicy food', 'de comida apimentada', '🌶️')]),
  W('Eu estou...', "I'm {x}.", 'Eu estou {x}.', 'state', 'home', [
    ('tired', '[cansada|cansado]', '😩'), ('hungry', 'com fome', '🤤'), ('thirsty', 'com sede', '🥤'),
    ('happy', 'feliz', '😄'), ('sad', 'triste', '😢'), ('cold', 'com frio', '🥶'), ('hot', 'com calor', '🥵'),
    ('sick', '[doente|doente]', '🤒'), ('lost', '[perdida|perdido]', '🧭'), ('late', '[atrasada|atrasado]', '⏰')]),
  W('Onde fica...?', 'Where is {x}?', 'Onde {x}?', 'where', 'street', [
    ('the bathroom', 'fica o banheiro', '🚻'), ('the station', 'fica a estação', '🚉'), ('the exit', 'fica a saída', '🚪'),
    ('the hotel', 'fica o hotel', '🏨'), ('the supermarket', 'fica o supermercado', '🛒'), ('the hospital', 'fica o hospital', '🏥'),
    ('the bus stop', 'fica o ponto de ônibus', '🚏'), ('my bag', 'está minha bolsa', '👜'),
    ('my phone', 'está meu celular', '📱'), ('the key', 'está a chave', '🔑')]),
  W('Pode me dar...?', 'Can I have {x}, please?', 'Pode me dar {x}, por favor?', 'ask', 'cafe', [
    ('the menu', 'o cardápio', '📋'), ('the bill', 'a conta', '🧾'), ('a glass of water', 'um copo de água', '💧'),
    ('a bag', 'uma sacola', '🛍️'), ('a fork', 'um garfo', '🍴'), ('a napkin', 'um guardanapo', '🧻'),
    ('some bread', 'um pouco de pão', '🍞'), ('some sugar', 'um pouco de açúcar', '🍬'),
    ('the wifi password', 'a senha do wifi', '📶'), ('a smaller size', 'um tamanho menor', '👕')]),
  W('Eu não consigo...', "I can't {x}.", 'Eu não consigo {x}.', 'cant', 'home', [
    ('find my key', 'achar minha chave', '🔑'), ('hear you', 'te ouvir', '👂'), ('see', 'enxergar', '👓'),
    ('understand', 'entender', '🧩'), ('open the door', 'abrir a porta', '🚪'), ('sleep', 'dormir', '😴'),
    ('find the hotel', 'encontrar o hotel', '🏨'), ('pay by card', 'pagar com cartão', '💳'),
    ('carry this bag', 'carregar essa mala', '🧳'), ('eat all this', 'comer tudo isso', '🍝')]),
  W('Você pode...?', 'Can you {x}?', 'Você pode {x}?', 'ask', 'street', [
    ('help me', 'me ajudar', '🤝'), ('repeat that, please', 'repetir, por favor', '🔁'),
    ('speak more slowly', 'falar mais devagar', '🐢'), ('take a photo', 'tirar uma foto', '📸'),
    ('call a taxi', 'chamar um táxi', '🚕'), ('show me on the map', 'me mostrar no mapa', '🗺️'),
    ('write it down', 'escrever isso', '✍️'), ('open the window', 'abrir a janela', '🪟'),
    ('close the door', 'fechar a porta', '🚪'), ('wait a minute', 'esperar um minuto', '⏱️')]),
 ]),
 dict(n=2, name='Casa e rotina', tag='Seu dia a dia, da hora que acorda até dormir', waves=[
  W('Todo dia eu...', 'I {x} every day.', 'Eu {x} todo dia.', 'routine', 'home', [
    ('wake up at seven', 'acordo às sete', '⏰'), ('take a shower', 'tomo banho', '🚿'), ('brush my teeth', 'escovo os dentes', '🪥'),
    ('have breakfast', 'tomo café da manhã', '🥞'), ('go to work', 'vou para o trabalho', '💼'), ('walk the dog', 'passeio com o cachorro', '🐕'),
    ('cook dinner', 'faço o jantar', '🍳'), ('read the news', 'leio as notícias', '📰'),
    ('drink a lot of water', 'bebo muita água', '💧'), ('go to bed at eleven', 'vou dormir às onze', '🛏️')]),
  W('Estou ... agora', "I'm {x} right now.", 'Estou {x} agora.', 'now', 'home', [
    ('cooking', 'cozinhando', '🥘'), ('eating', 'comendo', '🍽️'), ('watching TV', 'vendo TV', '📺'), ('working', 'trabalhando', '💻'),
    ('studying', 'estudando', '📚'), ('cleaning the house', 'limpando a casa', '🧹'), ('washing the dishes', 'lavando a louça', '🧽'),
    ('listening to music', 'ouvindo música', '🎧'), ('driving', 'dirigindo', '🚗'), ('talking on the phone', 'falando no telefone', '📞')]),
  W('Você quer...?', 'Do you want {x}?', 'Você quer {x}?', 'offer', 'home', [
    ('some tea', 'um chá', '🍵'), ('something to eat', 'algo para comer', '🍪'), ('to watch a movie', 'ver um filme', '🍿'),
    ('to go out tonight', 'sair hoje à noite', '🌃'), ('a cup of coffee', 'uma xícara de café', '☕'), ('to sit down', 'sentar', '🪑'),
    ('more rice', 'mais arroz', '🍚'), ('to play a game', 'jogar um jogo', '🎲'), ('to come with me', 'vir comigo', '🚶'),
    ('a piece of cake', 'um pedaço de bolo', '🍰')]),
  W('Vamos...!', "Let's {x}!", 'Vamos {x}!', 'together', 'park', [
    ('eat', 'comer', '🍽️'), ('go home', 'para casa', '🏠'), ('order a pizza', 'pedir uma pizza', '🍕'),
    ('watch a movie', 'assistir um filme', '🎬'), ('take a walk', 'dar uma volta', '🌳'), ('go to the park', 'ao parque', '🏞️'),
    ('clean the kitchen', 'limpar a cozinha', '🧹'), ('have lunch together', 'almoçar juntos', '🥗'),
    ('start', 'começar', '🏁'), ('dance', 'dançar', '💃')]),
  W('Onde você colocou...?', 'Where did you put {x}?', 'Onde você colocou {x}?', 'where', 'home', [
    ('the keys', 'as chaves', '🔑'), ('my glasses', 'meus óculos', '👓'), ('the remote control', 'o controle remoto', '🎛️'),
    ('the towel', 'a toalha', '🧺'), ('the scissors', 'a tesoura', '✂️'), ('my wallet', 'minha carteira', '👛'),
    ('the umbrella', 'o guarda-chuva', '☂️'), ('my headphones', 'meus fones', '🎧'), ('the milk', 'o leite', '🥛'),
    ('my shoes', 'meus sapatos', '👟')]),
  W('Eu tenho que...', 'I have to {x}.', 'Eu tenho que {x}.', 'must', 'home', [
    ('do the laundry', 'lavar a roupa', '🧺'), ('pay the bills', 'pagar as contas', '💸'), ('go to the supermarket', 'ir ao supermercado', '🛒'),
    ('wake up early', 'acordar cedo', '⏰'), ('take out the trash', 'levar o lixo para fora', '🗑️'), ('feed the cat', 'dar comida para o gato', '🐈'),
    ('finish my homework', 'terminar meu dever de casa', '📝'), ('call the plumber', 'ligar para o encanador', '🔧'),
    ('leave now', 'sair agora', '🚪'), ('water the plants', 'regar as plantas', '🪴')]),
  W('Não tem...', "There's no {x}.", 'Não tem {x}.', 'none', 'home', [
    ('coffee', 'café', '☕'), ('toilet paper', 'papel higiênico', '🧻'), ('bread', 'pão', '🍞'), ('sugar', 'açúcar', '🍬'),
    ('time', 'tempo', '⌛'), ('signal here', 'sinal aqui', '📶'), ('soap', 'sabão', '🧼'), ('electricity', 'luz', '💡'),
    ('food in the fridge', 'comida na geladeira', '🥡'), ('hot water', 'água quente', '🌡️')]),
  W('Este é meu...', 'This is my {x}.', FREE, 'present', 'home', [
    ('mother', 'Esta é minha mãe.', '👩'), ('father', 'Este é meu pai.', '👨'), ('brother', 'Este é meu irmão.', '👦'),
    ('sister', 'Esta é minha irmã.', '👧'), ('grandmother', 'Esta é minha avó.', '👵'), ('grandfather', 'Este é meu avô.', '👴'),
    ('husband', 'Este é meu marido.', '🤵'), ('wife', 'Esta é minha esposa.', '👰'), ('best friend', 'Este é meu melhor amigo.', '🤜'),
    ('boss', 'Este é meu chefe.', '👔')]),
  W('Posso...?', 'Can I {x}?', 'Posso {x}?', 'ask', 'home', [
    ('come in', 'entrar', '🚪'), ('sit here', 'sentar aqui', '🪑'), ('use your phone', 'usar seu celular', '📱'),
    ('turn on the light', 'acender a luz', '💡'), ('turn off the TV', 'desligar a TV', '📺'), ('take a shower', 'tomar banho', '🚿'),
    ('borrow your pen', 'pegar sua caneta emprestada', '🖊️'), ('ask you something', 'te perguntar uma coisa', '❓'),
    ('go to the bathroom', 'ir ao banheiro', '🚻'), ('help you', 'te ajudar', '🤝')]),
  W('Ela está...', "She's {x}.", 'Ela está {x}.', 'she', 'home', [
    ('sleeping', 'dormindo', '😴'), ('at work', 'no trabalho', '💼'), ('in the kitchen', 'na cozinha', '🍳'),
    ('on the phone', 'no telefone', '📞'), ('in the shower', 'no banho', '🚿'), ('at home', 'em casa', '🏠'),
    ('angry', 'brava', '😠'), ('busy', 'ocupada', '⏳'), ('outside', 'lá fora', '🌳'), ('on her way', 'a caminho', '🚗')], actor='👩'),
 ]),
 dict(n=3, name='Cidade e viagem', tag='Chegar, se locomover e se virar em outro país', waves=[
  W('Como eu chego...?', 'How do I get to {x}?', 'Como eu chego {x}?', 'go', 'street', [
    ('the airport', 'ao aeroporto', '✈️'), ('the city center', 'ao centro', '🏙️'), ('the museum', 'ao museu', '🏛️'),
    ('the beach', 'à praia', '🏖️'), ('the train station', 'à estação de trem', '🚆'), ('this address', 'neste endereço', '📍'),
    ('the subway', 'ao metrô', '🚇'), ('the stadium', 'ao estádio', '🏟️'), ('the park', 'ao parque', '🏞️'),
    ('the old town', 'à cidade velha', '🏰')]),
  W('Tem ... aqui perto?', 'Is there {x} near here?', 'Tem {x} aqui perto?', 'where', 'street', [
    ('a pharmacy', 'uma farmácia', '💊'), ('an ATM', 'um caixa eletrônico', '🏧'), ('a restaurant', 'um restaurante', '🍽️'),
    ('a hotel', 'um hotel', '🏨'), ('a bus stop', 'um ponto de ônibus', '🚏'), ('a gas station', 'um posto de gasolina', '⛽'),
    ('a hospital', 'um hospital', '🏥'), ('a bakery', 'uma padaria', '🥐'), ('a supermarket', 'um supermercado', '🛒'),
    ('a bookstore', 'uma livraria', '📖')]),
  W('Eu gostaria de...', "I'd like {x}.", 'Eu gostaria {x}.', 'want', 'hotel', [
    ('a room for two nights', 'de um quarto para duas noites', '🛏️'), ('a window seat', 'de um assento na janela', '🪟'),
    ('a one-way ticket', 'de uma passagem só de ida', '🎫'), ('a return ticket', 'de uma passagem de ida e volta', '🔄'),
    ('to check in', 'de fazer o check-in', '🛎️'), ('to check out', 'de fazer o check-out', '🧳'),
    ('a table for four', 'de uma mesa para quatro', '🍽️'), ('to rent a car', 'de alugar um carro', '🚙'),
    ('a map of the city', 'de um mapa da cidade', '🗺️'), ('to book a tour', 'de reservar um passeio', '🚌')]),
  W('Direções', FREE, FREE, 'talk', 'street', [
    ('Turn left.', 'Vire à esquerda.', '⬅️'), ('Turn right.', 'Vire à direita.', '➡️'), ('Go straight ahead.', 'Siga em frente.', '⬆️'),
    ("It's on the corner.", 'Fica na esquina.', '↪️'), ("It's next to the bank.", 'Fica ao lado do banco.', '🏦'),
    ("It's across the street.", 'Fica do outro lado da rua.', '🚸'), ("It's far from here.", 'Fica longe daqui.', '🔭'),
    ("It's very close.", 'Fica bem perto.', '📍'), ('Take the second street.', 'Pegue a segunda rua.', '2️⃣'),
    ('Stop here, please.', 'Pare aqui, por favor.', '🛑')]),
  W('Hoje está...', "It's {x} today.", 'Hoje está {x}.', 'weather', 'park', [
    ('sunny', 'ensolarado', '☀️'), ('raining', 'chovendo', '🌧️'), ('cold', 'frio', '🥶'), ('hot', 'quente', '🔥'),
    ('windy', 'ventando', '🌬️'), ('cloudy', 'nublado', '☁️'), ('snowing', 'nevando', '❄️'), ('beautiful', 'lindo', '🌈'),
    ('foggy', 'com neblina', '🌫️'), ('very humid', 'muito úmido', '💦')]),
  W('Eu vou pegar...', "I'm going to take {x}.", 'Eu vou pegar {x}.', 'go', 'street', [
    ('the bus', 'o ônibus', '🚌'), ('the train', 'o trem', '🚆'), ('the subway', 'o metrô', '🚇'), ('a taxi', 'um táxi', '🚕'),
    ('an Uber', 'um Uber', '🚗'), ('the ferry', 'a balsa', '⛴️'), ('a plane', 'um avião', '✈️'), ('my bike', 'minha bicicleta', '🚲'),
    ('the next flight', 'o próximo voo', '🛫'), ('the last train', 'o último trem', '🚉')]),
  W('A que horas...?', 'What time does {x}?', 'A que horas {x}?', 'time', 'street', [
    ('the train leave', 'sai o trem', '🚆'), ('the store open', 'abre a loja', '🏪'), ('the store close', 'fecha a loja', '🔒'),
    ('the show start', 'começa o show', '🎭'), ('the museum close', 'fecha o museu', '🏛️'), ('the flight arrive', 'chega o voo', '🛬'),
    ('the bus come', 'vem o ônibus', '🚌'), ('breakfast start', 'começa o café da manhã', '🥐'),
    ('the party start', 'começa a festa', '🎉'), ('the class end', 'termina a aula', '🎓')]),
  W('Quanto custa...?', 'How much is {x}?', 'Quanto custa {x}?', 'price', 'shop', [
    ('this shirt', 'esta camisa', '👕'), ('the ticket', 'o ingresso', '🎟️'), ('a coffee', 'um café', '☕'), ('the room', 'o quarto', '🛏️'),
    ('this bag', 'esta bolsa', '👜'), ('the taxi to the airport', 'o táxi até o aeroporto', '🚕'), ('one night', 'uma noite', '🌙'),
    ('that watch', 'aquele relógio', '⌚'), ('a bottle of water', 'uma garrafa de água', '💧'), ('the tour', 'o passeio', '🚌')]),
  W('... não funciona', "The {x} doesn't work.", '{x} não funciona.', 'broken', 'hotel', [
    ('air conditioning', 'O ar-condicionado', '❄️'), ('shower', 'O chuveiro', '🚿'), ('TV', 'A TV', '📺'), ('wifi', 'O wifi', '📶'),
    ('elevator', 'O elevador', '🛗'), ('key card', 'O cartão da porta', '💳'), ('light', 'A luz', '💡'), ('phone', 'O telefone', '☎️'),
    ('heater', 'O aquecedor', '🔥'), ('lock', 'A fechadura', '🔒')]),
  W('Perguntas de viagem', FREE, FREE, 'ask', 'hotel', [
    ('Do you speak Portuguese?', 'Você fala português?', '🗣️'), ('Can I pay by card?', 'Posso pagar com cartão?', '💳'),
    ('Is it far?', 'É longe?', '🔭'), ('Is breakfast included?', 'O café da manhã está incluído?', '🥐'),
    ('Where can I buy a ticket?', 'Onde posso comprar um ingresso?', '🎟️'),
    ('Can you recommend a restaurant?', 'Você pode recomendar um restaurante?', '🍽️'),
    ('How long does it take?', 'Quanto tempo demora?', '⏳'), ('Is this seat free?', 'Este lugar está livre?', '💺'),
    ('Can I leave my bag here?', 'Posso deixar minha mala aqui?', '🧳'), ('What do you recommend?', 'O que você recomenda?', '👍')]),
 ]),
 dict(n=4, name='Trabalho e compras', tag='Escritório, lojas, dinheiro e problemas do dia', waves=[
  W('Estou procurando...', "I'm looking for {x}.", 'Estou procurando {x}.', 'search', 'shop', [
    ('a jacket', 'uma jaqueta', '🧥'), ('a gift for my mom', 'um presente para minha mãe', '🎁'),
    ('something cheaper', 'algo mais barato', '🏷️'), ('size medium', 'tamanho médio', '👕'), ('a job', 'um emprego', '💼'),
    ('an apartment', 'um apartamento', '🏢'), ('my friend', '[minha amiga|meu amigo]', '👫'), ('the manager', 'o gerente', '👔'),
    ('a charger', 'um carregador', '🔌'), ('black shoes', 'sapatos pretos', '👞')]),
  W('Tem isso em...?', 'Do you have this in {x}?', 'Vocês têm isso em {x}?', 'ask', 'shop', [
    ('blue', 'azul', '🔵'), ('red', 'vermelho', '🔴'), ('black', 'preto', '⚫'), ('white', 'branco', '⚪'), ('green', 'verde', '🟢'),
    ('a bigger size', 'um tamanho maior', '⏫'), ('a smaller size', 'um tamanho menor', '⏬'), ('size large', 'tamanho G', '👕'),
    ('another color', 'outra cor', '🎨'), ('leather', 'couro', '👜')]),
  W('Na loja', FREE, FREE, 'talk', 'shop', [
    ("I'm just looking.", 'Só estou olhando.', '👀'), ('Can I try it on?', 'Posso experimentar?', '👗'),
    ("It's too expensive.", 'Está muito caro.', '💸'), ("It's a good price.", 'É um bom preço.', '🏷️'),
    ("I'll take it.", 'Vou levar.', '🛍️'), ('Do you have a discount?', 'Tem desconto?', '🔖'),
    ('Can I pay in cash?', 'Posso pagar em dinheiro?', '💵'), ('Where is the fitting room?', 'Onde fica o provador?', '🚪'),
    ("It doesn't fit.", 'Não serviu.', '👖'), ('I want to return this.', 'Quero devolver isso.', '↩️')]),
  W('Eu trabalho...', 'I work {x}.', 'Eu trabalho {x}.', 'routine', 'office', [
    ('from home', 'de casa', '🏠'), ('in an office', 'em um escritório', '🏢'), ('at a hospital', 'em um hospital', '🏥'),
    ('in a school', 'numa escola', '🏫'), ('with computers', 'com computadores', '💻'), ('with people', 'com pessoas', '👥'),
    ('at night', 'à noite', '🌙'), ('on weekends', 'nos fins de semana', '📅'), ('for a big company', 'para uma empresa grande', '🏭'),
    ('in sales', 'com vendas', '📈')]),
  W('Tenho uma reunião...', 'I have a meeting {x}.', 'Eu tenho uma reunião {x}.', 'future', 'office', [
    ('at ten', 'às dez', '🕙'), ('in five minutes', 'em cinco minutos', '⏱️'), ('this afternoon', 'hoje à tarde', '🌇'),
    ('tomorrow morning', 'amanhã de manhã', '🌅'), ('on Monday', 'na segunda', '📅'), ('with my boss', 'com meu chefe', '👔'),
    ('with a client', 'com um cliente', '🤝'), ('online', 'online', '💻'), ('after lunch', 'depois do almoço', '🥪'),
    ('all day', 'o dia todo', '📆')]),
  W('Você poderia...?', 'Could you {x}?', 'Você poderia {x}?', 'ask', 'office', [
    ('send me the file', 'me mandar o arquivo', '📎'), ('check this', 'dar uma olhada nisso', '🔍'), ('call me back', 'me ligar de volta', '📞'),
    ('explain it again', 'explicar de novo', '🔁'), ('sign here', 'assinar aqui', '✍️'), ('send me an email', 'me mandar um email', '📧'),
    ('print this', 'imprimir isso', '🖨️'), ('give me a hand', 'me dar uma mão', '🤝'), ('share your screen', 'compartilhar sua tela', '🖥️'),
    ('turn on the projector', 'ligar o projetor', '📽️')]),
  W('Estou trabalhando em...', "I'm working on {x}.", 'Estou trabalhando {x}.', 'now', 'office', [
    ('a new project', 'num projeto novo', '🚀'), ('the report', 'no relatório', '📊'), ('the presentation', 'na apresentação', '🖼️'),
    ('the budget', 'no orçamento', '💰'), ('a website', 'num site', '🌐'), ('the schedule', 'no cronograma', '🗓️'),
    ('my English', 'no meu inglês', '📚'), ('the contract', 'no contrato', '📜'), ('an app', 'num aplicativo', '📱'),
    ('the spreadsheet', 'na planilha', '📈')]),
  W('No escritório', FREE, FREE, 'talk', 'office', [
    ("I'll be right back.", 'Já volto.', '🏃'), ("I'm in a meeting.", 'Estou em uma reunião.', '👥'), ('Let me check.', 'Deixa eu ver.', '🔍'),
    ('I agree.', 'Eu concordo.', '👍'), ("I don't agree.", 'Eu não concordo.', '👎'), ("That's a good idea.", 'É uma boa ideia.', '💡'),
    ("I'm almost done.", 'Estou quase terminando.', '⏳'), ("It's my day off.", 'É minha folga.', '🏖️'),
    ("I'm running late.", 'Estou [atrasada|atrasado].', '⏰'), ('Good job!', 'Bom trabalho!', '🏆')]),
  W('... está quebrado', 'The {x} is broken.', FREE, 'broken', 'office', [
    ('laptop', 'O notebook está quebrado.', '💻'), ('printer', 'A impressora está quebrada.', '🖨️'),
    ('coffee machine', 'A máquina de café está quebrada.', '☕'), ('chair', 'A cadeira está quebrada.', '🪑'),
    ('door', 'A porta está quebrada.', '🚪'), ('window', 'A janela está quebrada.', '🪟'), ('screen', 'A tela está quebrada.', '🖥️'),
    ('mouse', 'O mouse está quebrado.', '🖱️'), ('keyboard', 'O teclado está quebrado.', '⌨️'), ('car', 'O carro está quebrado.', '🚗')]),
  W('Quero... (dinheiro)', 'I want to {x}.', 'Eu quero {x}.', 'want', 'shop', [
    ('withdraw money', 'sacar dinheiro', '🏧'), ('open an account', 'abrir uma conta', '🏦'), ('change money', 'trocar dinheiro', '💱'),
    ('send money', 'mandar dinheiro', '💸'), ('save money', 'economizar dinheiro', '🐷'), ('buy a present', 'comprar um presente', '🎁'),
    ('cancel my order', 'cancelar meu pedido', '❌'), ('pay the bill', 'pagar a conta', '🧾'), ('split the bill', 'dividir a conta', '➗'),
    ('pay in cash', 'pagar em dinheiro', '💵')]),
 ]),
 dict(n=5, name='Passado e planos', tag='Contar o que fez e dizer o que vai fazer', waves=[
  W('Ontem eu...', 'Yesterday I {x}.', 'Ontem eu {x}.', 'past', 'home', [
    ('went to the beach', 'fui à praia', '🏖️'), ('worked a lot', 'trabalhei muito', '💼'), ('watched a movie', 'assisti um filme', '🎬'),
    ('cooked pasta', 'fiz macarrão', '🍝'), ('met my friends', 'encontrei meus amigos', '👫'), ('slept late', 'dormi tarde', '😴'),
    ('went shopping', 'fui às compras', '🛍️'), ('studied English', 'estudei inglês', '📚'), ('played football', 'joguei futebol', '⚽'),
    ('stayed at home', 'fiquei em casa', '🏠')]),
  W('No fim de semana passado...', 'Last weekend I {x}.', 'No fim de semana passado eu {x}.', 'past', 'park', [
    ('visited my parents', 'visitei meus pais', '👪'), ('went to a party', 'fui a uma festa', '🎉'), ('read a book', 'li um livro', '📖'),
    ('cleaned the house', 'limpei a casa', '🧹'), ('went to the gym', 'fui à academia', '🏋️'), ('had a barbecue', 'fiz um churrasco', '🍖'),
    ('saw a concert', 'vi um show', '🎸'), ('travelled to the coast', 'viajei para o litoral', '🌊'), ('rested', 'descansei', '🛋️'),
    ('went hiking', 'fiz uma trilha', '⛰️')]),
  W('Eu comprei...', 'I bought {x}.', 'Eu comprei {x}.', 'pastbuy', 'shop', [
    ('a new car', 'um carro novo', '🚗'), ('some clothes', 'umas roupas', '👕'), ('a plane ticket', 'uma passagem de avião', '✈️'),
    ('a present for you', 'um presente para você', '🎁'), ('fruit at the market', 'frutas na feira', '🍎'), ('a new laptop', 'um notebook novo', '💻'),
    ('flowers', 'flores', '💐'), ('a coffee machine', 'uma cafeteira', '☕'), ('a bike', 'uma bicicleta', '🚲'), ('a house', 'uma casa', '🏡')]),
  W('Amanhã eu vou...', "Tomorrow I'm going to {x}.", 'Amanhã eu vou {x}.', 'future', 'home', [
    ('wake up early', 'acordar cedo', '⏰'), ('visit my grandma', 'visitar minha avó', '👵'), ('go to the doctor', 'ir ao médico', '🩺'),
    ('start a new job', 'começar um emprego novo', '💼'), ('travel to London', 'viajar para Londres', '🎡'),
    ('cook for my family', 'cozinhar para minha família', '🍲'), ('go running', 'correr', '🏃'), ('buy a new phone', 'comprar um celular novo', '📱'),
    ('clean my room', 'arrumar meu quarto', '🧹'), ('rest all day', 'descansar o dia todo', '🛋️')]),
  W('Você já...?', 'Have you ever {x}?', 'Você já {x}?', 'ever', 'park', [
    ('been to London', 'foi a Londres', '🎡'), ('eaten sushi', 'comeu sushi', '🍣'), ('seen snow', 'viu neve', '❄️'),
    ('ridden a horse', 'andou a cavalo', '🐎'), ('flown in a helicopter', 'voou de helicóptero', '🚁'),
    ('lost your passport', 'perdeu seu passaporte', '🛂'), ('met a famous person', 'conheceu alguém famoso', '🌟'),
    ('cooked for ten people', 'cozinhou para dez pessoas', '🍲'), ('run a marathon', 'correu uma maratona', '🏃'),
    ('swum in the ocean', 'nadou no mar', '🌊')]),
  W('Eu já...', "I've already {x}.", 'Eu já {x}.', 'done', 'office', [
    ('eaten', 'comi', '🍽️'), ('done my homework', 'fiz meu dever de casa', '📝'), ('seen this movie', 'vi esse filme', '🎬'),
    ('paid', 'paguei', '💳'), ('sent the email', 'mandei o email', '📧'), ('called her', 'liguei para ela', '📞'),
    ('finished the report', 'terminei o relatório', '📊'), ('booked the hotel', 'reservei o hotel', '🏨'),
    ('packed my bag', 'arrumei minha mala', '🧳'), ('told him', 'contei para ele', '🗣️')]),
  W('Eu vou..., prometo', 'I will {x}, I promise.', 'Eu vou {x}, prometo.', 'promise', 'home', [
    ('call you tomorrow', 'te ligar amanhã', '📞'), ('be there at eight', 'estar lá às oito', '🕗'), ('help you', 'te ajudar', '🤝'),
    ('bring the cake', 'trazer o bolo', '🎂'), ('pay you back', 'te pagar de volta', '💵'), ('study harder', 'estudar mais', '📚'),
    ('be on time', 'chegar no horário', '⏰'), ('send it today', 'mandar hoje', '📤'), ('come back soon', 'voltar logo', '🔙'),
    ('never forget this', 'nunca esquecer isso', '🧠')]),
  W('Eu me sinto...', 'I feel {x}.', 'Eu me sinto {x}.', 'state', 'home', [
    ('much better', 'muito melhor', '💪'), ('a bit nervous', 'um pouco [nervosa|nervoso]', '😬'), ('excited', '[animada|animado]', '🤩'),
    ('relaxed', '[relaxada|relaxado]', '😌'), ('lonely', '[sozinha|sozinho]', '😶'), ('confident', 'confiante', '😎'),
    ('stressed', '[estressada|estressado]', '😫'), ('grateful', '[grata|grato]', '🙏'), ('sleepy', 'com sono', '😪'),
    ('at home here', 'em casa aqui', '🏡')]),
  W('Ano que vem eu quero...', 'Next year I want to {x}.', 'No ano que vem eu quero {x}.', 'dream', 'park', [
    ('speak English fluently', 'falar inglês fluente', '🗣️'), ('live abroad', 'morar fora', '🌍'), ('change jobs', 'mudar de emprego', '🔄'),
    ('learn to swim', 'aprender a nadar', '🏊'), ('buy a house', 'comprar uma casa', '🏡'), ('visit Japan', 'visitar o Japão', '🗾'),
    ('get married', 'casar', '💍'), ('start a business', 'abrir um negócio', '🏪'), ('read twenty books', 'ler vinte livros', '📚'),
    ('travel more', 'viajar mais', '✈️')]),
  W('Na conversa', FREE, FREE, 'talk', 'cafe', [
    ('What do you mean?', 'Como assim?', '🤔'), ('That makes sense.', 'Faz sentido.', '💡'), ('I see.', 'Entendi.', '👌'),
    ('Me too.', 'Eu também.', '🙌'), ('Really?', 'Sério?', '😮'), ('No way!', 'Não acredito!', '😱'),
    ('That sounds great!', 'Parece ótimo!', '🎉'), ("I'm not sure.", 'Não tenho certeza.', '🤷'), ('Let me think.', 'Deixa eu pensar.', '💭'),
    ('Never mind.', 'Deixa pra lá.', '🙅')]),
 ]),
]


from curriculo import PLAN, MONTHS
import glob, importlib, os
EXTRA = []
for _f in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dias_*.py'))):
    EXTRA += importlib.import_module(os.path.basename(_f)[:-3]).DAYS


def all_days():
    days = {d['n']: d for d in DAYS}
    for d in EXTRA:
        days[d['n']] = d
    info = {n: (t, g) for n, t, g in PLAN}
    out = []
    for n in sorted(days):
        d = dict(days[n]); d['name'], d['tag'] = info[n]
        out.append(d)
    return out


def build():
    out = []
    for d in all_days():
        waves = []
        for wi, w in enumerate(d['waves']):
            ph = []
            for k, (xe, xp, emo) in enumerate(w['items']):
                pid = f"d{d['n']}w{wi+1}p{k+1}"
                en = w['en'].replace('{x}', xe)
                pt = w['pt'].replace('{x}', xp)
                ph.append(dict(id=pid, en=en, pt=pt, x=xe, e=emo))
            waves.append(dict(title=w['title'], frame=w['en'].replace('{x}', '___'), framePt=w['pt'].replace('{x}', '___') if w['pt'] != FREE else '',
                              mod=w['mod'], bg=w['bg'], actor=w['actor'], phrases=ph))
        out.append(dict(n=d['n'], name=d['name'], tag=d['tag'], waves=waves))
    return out


def plan():
    return dict(months=MONTHS, days=[dict(n=n, name=t, tag=g) for n, t, g in PLAN])


if __name__ == '__main__':
    import re
    days = build()
    n = sum(len(w['phrases']) for d in days for w in d['waves'])
    print(len(days), 'dias', n, 'frases')
    seen = {}
    for d in days:
        assert len(d['waves']) == 10, d['n']
        for w in d['waves']:
            assert len(w['phrases']) == 10, (d['n'], w['title'])
            for p in w['phrases']:
                assert p['en'] and p['pt'] and p['e'], p
                assert '{x}' not in p['en'] + p['pt'], p
                assert p['pt'].count('[') == p['pt'].count(']'), p
                seen.setdefault(p['en'].lower(), []).append(p['id'])
    import re as _r
    html = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'site.html')).read()
    mods = set(_r.findall(r"case '([a-z]+)'", html)); bgs = set(_r.findall(r'\.bg-([a-z]+)', html))
    bad = [(d['n'], w['title'], w['mod'], w['bg']) for d in days for w in d['waves'] if w['mod'] not in mods or w['bg'] not in bgs]
    print('cenas inválidas:', bad[:20])
    dup = {k: v for k, v in seen.items() if len(v) > 1}
    print('repetidas:', len(dup)); [print(' ', k, v) for k, v in list(dup.items())[:40]]
