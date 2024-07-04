-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jul 04, 2024 at 12:39 AM
-- Server version: 8.2.0
-- PHP Version: 8.2.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_quie_isso`
--

-- --------------------------------------------------------

--
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
CREATE TABLE IF NOT EXISTS `cliente` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `senha` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `cliente`
--

INSERT INTO `cliente` (`id`, `nome`, `email`, `senha`) VALUES
(1, 'adm-bruno', 'adm@outlook.com', '$2b$12$Z9eyvqTErTVoWJWBJ9o0AuAcqaWjtYBeGb0/fhIKcMs960poxSW.a'),
(2, 'Bruno', 'brunim@gmail.com', '$2b$12$8EfV7vJ03pMPkUBjYeG7bOxlthfvUtujSUj8jmtfwW.SliV6gmmv6'),
(3, 'Raul', 'rauzim@gmail.com', '$2b$12$nAS2kSQ0GvIWU/jZANyhqu5Oz5rF43M72QJGSMcsrVGhH7VrpsvXi'),
(4, 'testezera', 'testezera@gmail.com', '$2b$12$AnJ2NQsALYssW.ACQg4IUekSkE8/JWff82vSOwC2idCK41KGL1/GK'),
(6, 'te', 'testezera2@outlook.com', '$2b$12$R206xxgIHVfryKX5tqrBfuusG5Pw3HcPO44hOC5uEpXkEqoa6qYUe');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

DROP TABLE IF EXISTS `feedback`;
CREATE TABLE IF NOT EXISTS `feedback` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cliente_id` int NOT NULL,
  `opiniao` text COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cliente_id` (`cliente_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`id`, `cliente_id`, `opiniao`) VALUES
(1, 3, 'Faltou bootstrap filhão!'),
(3, 2, 'Quié isso heim filho do japonês?! XP');

-- --------------------------------------------------------

--
-- Table structure for table `livros`
--

DROP TABLE IF EXISTS `livros`;
CREATE TABLE IF NOT EXISTS `livros` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cliente_id` int NOT NULL,
  `ISBN` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `titulo` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `autor` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `editora` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `ano_publicacao` date NOT NULL,
  `categoria` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `quantidade` int NOT NULL,
  `preco` decimal(10,2) NOT NULL,
  `imagem` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `palavrinha` text COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cliente_id` (`cliente_id`)
) ENGINE=MyISAM AUTO_INCREMENT=52 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `livros`
--

INSERT INTO `livros` (`id`, `cliente_id`, `ISBN`, `titulo`, `autor`, `editora`, `ano_publicacao`, `categoria`, `quantidade`, `preco`, `imagem`, `palavrinha`) VALUES
(1, 1, '8576082675', 'Código Limpo: Habilidades Práticas do Agile Software', 'Robert C. Martin', 'Alta Books', '2009-09-08', 'programação', 10, 50.00, 'codigo-limpo.png', 'codigo limpo habilidades praticas agile software robert martin programador melhor praticar'),
(2, 1, '9788550800004', 'Programação para Adolescentes para Leigos', 'Camille McCue', 'Alta Books', '2016-06-01', 'programação', 10, 50.00, 'adol.png', 'conceitos basicos programacao desenho movimento animacao variaveis controle de teclado projeto passo a passo publico-alvo jovens aprender programar proprios jogos aplicativos computador'),
(3, 1, '8575227637', 'Aprendendo PHP: Introdução Amigável à Linguagem Mais Popular da Web', 'David Sklar', 'Novatec Editora', '2019-05-22', 'programação', 10, 50.00, 'aprend-php.png', 'aprendendo php introducao amigavel linguagem mais popular da web David Sklar sites dinamicos servidores navegadores banco de dados services desenvolvedor front end'),
(4, 1, '8536533080', 'JavaScript Descomplicado: Programação para a Web, IOT e Dispositivos Móveis', 'Cláudio Luís Vieira Oliveira e Humberto Augusto Piovesana Zanetti', 'Editora Érica - Sob Demanda', '2020-09-08', 'programação', 10, 50.00, 'js-descomp.png', 'javaScript descomplicado programacao web iot dispositivos moveis Claudio Luis Vieira Oliveira Humberto Augusto Piovesana Zanetti framework sistemas banco de dados'),
(5, 1, '8536508442', 'Programação Web com plataforma Java: Fundamentos e desenvolvimento de aplicações', 'João Alexandre Magri', 'Editora Érica - Sob Demanda', '2014-01-16', 'programação', 10, 50.00, 'prog-web.png', 'programacao web plataforma java fundamentos desenvolvimento aplicacoes Joao Alexandre Magri orientacao objeto linguagens html css JavaScript jsp servlets'),
(6, 1, '9788550803401', 'Use a Cabeça! Python ― 2ª Edição', 'Paul Barry', 'Alta Books', '2018-08-13', 'programação', 10, 50.00, 'python-att-1.png', 'use cabeca python 2 edicao Paul Barry linguagem manuais fundamentos estruturas dados funcoes predefinidas aplicativo web banco de dados excecoes administracao'),
(7, 1, '9788536509662', 'Algoritmos e Lógica de Programação em C – Uma Abordagem Didática', 'Silvio do Lago Pereira', 'Editora Érica - Sob Demanda', '2018-06-12', 'programação', 10, 50.00, 'prog-em-c.png', 'algoritmos logica programacao C uma abordagem didatica Silvio Lago Pereira fluxograma conceitos sequencia selecao repeticao algoritmo computacional estruturado'),
(8, 1, '9780064471046', 'As Crônicas de Nárnia', 'C. S. Lewis', 'WMF Martins Fontes', '2009-01-08', 'aventura', 5, 30.00, 'narnia.png', 'cronicas narnia leao feiticeira guarda roupa aslam Clive Staples Lewis'),
(9, 1, '8533613377', 'A Sociedade do Anel - Volume 1 da série O Senhor dos Anéis', 'J. R. R. Tolkien', 'Martins Fontes', '2000-03-03', 'aventura', 3, 30.00, 'senhor-aneis.png', 'sociedade anel volume 1 serie senhor aneis John Ronald Reuel Tolkien gandalf frodo hobbit aragorn boromir legolas gimli sauron saruman orc'),
(10, 1, '9722325337', 'Harry Potter e a Pedra Filosofal', 'J.K. Rowling', 'Editorial Presenca', '2000-12-14', 'aventura', 3, 30.00, 'pedra-filo.png', 'harry potter pedra filosofal J. K. Rowling bruxaria hogwarts trouxas escola magia quadribol'),
(11, 1, '8594541759', 'Alice no País das Maravilhas (Classic Edition)', 'Lewis Carroll', 'Darkside', '2019-10-04', 'aventura', 3, 30.00, 'alice-pais.png', 'Alice pais maravilhas Lewis Carroll menina toca coelho absurdo loucura'),
(12, 1, '8544001513', 'O Conde de Monte-Cristo', 'Alexandre Dumas', 'Martin Claret', '2017-10-20', 'aventura', 2, 40.00, 'conde-monte.png', 'conde Monte Cristo Alexandre Dumas edmond dantes traicao castelo prisao'),
(13, 1, '6586490553', 'Moby Dick', 'Herman Melville', 'Editora Antofágica', '2022-07-11', 'aventura', 3, 50.00, 'moby-dick.png', 'Moby Dick Herman Melville ishmael ahab pequod baleia'),
(14, 1, '8594318146', 'A volta ao mundo em 80 dias', 'Júlio Verne', 'Principis', '2019-03-25', 'aventura', 3, 30.00, 'volta-mundo.png', 'volta mundo 80 dias Julio Verne cavalheiro ingles phileas fogg passepartout fura-vidas faz-tudo detetive fix aouda'),
(15, 1, '8580573807', 'A Culpa é das Estrelas', 'John Green', 'Intrínseca', '2014-10-27', 'romance', 3, 30.00, 'culpa-estrelas.png', 'culpa estrelas John Green romance adolescente cancer Hazel Grace Lancaster Augustus Waters'),
(16, 1, '8599296159', 'Água para Elefantes', 'Sara Gruen', 'Editora Arqueiro', '2011-03-15', 'romance', 2, 15.00, 'agua-elefantes.png', 'agua elefantes Sara Gruen Jacob Jankowski casa de repouso circo esquadrao voador circo irmaos benzini'),
(17, 1, '9788581630625', 'P.S. Eu te Amo', 'Cecelia Ahern', 'HarperCollins Brasil', '2023-04-15', 'romance', 3, 20.00, 'ps-te-amo.png', 'p.s. eu te amo Cecelia Ahern Gerry Holly almas gemeas amor tumor cerebral cartas assinadas'),
(18, 1, '8594318235', 'O Morro dos Ventos Uivantes', 'Emily Brontë', 'Principis', '2019-06-17', 'romance', 2, 15.00, 'morro-ventos.png', 'morro ventos uivantes Emily Bronte ellis bell narrativa gotica inglaterra familia earnshaw linton'),
(19, 1, '6587817149', 'Orgulho e Preconceito', 'Jane Austen', 'Camelot Editora', '2021-09-16', 'romance', 2, 15.00, 'orgulho-preconceito.png', 'orgulho preconceito Jane Austen burguesia inglesa seculo xix amor dinheiro promiscuas mesquinhas'),
(20, 1, '8535906096', 'Olhai os Lírios do Campo', 'Erico Verissimo', 'Companhia das Letras', '2005-02-22', 'romance', 3, 30.00, 'olhai-lirios.png', 'olhai lirios campo Erico Verissimo sermao da montanha eugenio fontes medico paixao olivia'),
(21, 1, '8535929223', 'Anna Kariênina', 'Liev Tolstoi', 'Companhia das Letras', '2017-07-07', 'romance', 3, 30.00, 'anna-karenina.png', 'Anna Karienina Liev Tolstoi amor casamento familia infidelidade sociedade russa progresso tradicao'),
(22, 1, '9788520938393', 'O Auto da Compadecida', 'Ariano Suassuna', 'Nova Fronteira', '2018-05-31', 'comédia', 3, 35.00, 'auto-compadecida.png', 'auto compadecida Ariano Suassuna sertao nordestino chico joao grilo tradicao popular humor'),
(23, 1, '9788535922936', 'Cadê você Bernadette?', 'Maria Semple', 'Companhia das Letras', '2013-06-28', 'comédia', 3, 35.00, 'cade-voce-bebe.png', 'cade voce bernadete Maria Semple conceito identidade complexidades vida moderna bernadette fox'),
(24, 1, '6550471400', 'Epaminondas: O gato explicador', 'Clóvis de Barros Filho', 'Citadel', '2022-06-20', 'comédia', 3, 15.00, 'epaminondas-gato.png', 'epaminondas gato explicador Clovis Barros Filho epa felino necessidade atencao mesa cabeceira coisas quebram'),
(25, 1, '9788599296578', 'O guia do mochileiro das galáxias', 'Douglas Adams', 'Editora Arqueiro', '2010-11-09', 'comédia', 3, 35.00, 'guia-do-mochileiro.png', 'guia mochileiro galaxias Douglas Adams arthur dent terra destruida pelos vogons raca alienigena ford'),
(26, 1, '6555521171', 'As viagens de Gulliver', 'Jonathan Swift', 'Principis', '2020-09-28', 'comédia', 2, 15.00, 'gulliver-br.png', 'viagens Gulliver Jonathan Swift lemuel satira Lilliput pessoas minusculas gigante Brobdingnag'),
(27, 1, '8516091228', 'Sonho de uma noite de verão', 'William Shakespeare', 'Moderna Literatura', '2014-05-05', 'comédia', 3, 35.00, 'sonhos-noite-br.png', 'sonho noite verao William Shakespeare hermia Helena Lisandro Demetrio rei rainha fadas'),
(28, 1, '6584952037', 'As aventuras de Tom Sawyer: edição comentada e ilustrada', 'Mark Twain', 'Clássicos Zahar', '2023-03-23', 'comédia', 2, 45.00, 'tom-sawyer-br.png', 'Tom Sawyer Mark Twain peripecias confusoes criancas adultos sao petesburgo'),
(29, 1, '8525056006', 'Admirável mundo novo', 'Aldous Leonard Huxley', 'Biblioteca Azul', '2014-01-01', 'ficção', 3, 35.00, 'admiravel-br.png', 'admiravel mundo novo Aldous Huxley desafia convencoes sociais explora limites humanidade visao futurista distopica'),
(30, 1, '8535914846', '1984', 'George Orwell', 'Companhia das Letras', '2009-07-21', 'ficção', 2, 15.00, '1984-br.png', '1984 George Orwell literatura politica grande irmao atemporal mundo opressivo sombrio teletela ministerio da verdade'),
(31, 1, '6586064066', '2001: Uma Odisseia no Espaço', 'Arthur C. Clarke', 'Editora Aleph', '2015-09-16', 'ficção', 3, 45.00, '2001-br.png', '2001 uma odisseia espaço Arthur C. Clarke objeto inusitado evolução monolito lua equipe treinada HAL 9000'),
(32, 1, '8576574403', 'Blade Runner: Androides sonham com ovelhas elétricas?', 'Philip K. Dick', 'Editora Aleph', '2019-04-10', 'ficção', 3, 45.00, 'blade-runner-br.png', 'blade runner androides sonham com ovelhas elétricas Philip K. Dick deckard cacador recompensas androides fugitivos cyberpunk humanos robo humanoide'),
(33, 1, '857657313X', 'Duna: livro 1', 'Frank Herbert', 'Editora Aleph', '2017-04-28', 'ficção', 2, 55.00, 'duna-br.png', 'duna Frank Herbert imperio intergalatico feudal feudos planetarios controlados casas nobres casa corrino paul atreides'),
(34, 1, '6580448334', 'Frankenstein: Edição Luxo', 'Mary Shelley', 'Excelsior', '2019-11-26', 'ficção', 2, 25.00, 'frankenstein-br.png', 'Frankenstein Mary Shelley victor segredo criar vida monstro hediondo fonte miseria morte capitao walton'),
(35, 1, '8556510094', 'A guerra dos mundos', 'H.G. Wells', 'Suma', '2016-05-27', 'ficção', 3, 45.00, 'guerra-mundos-br.png', 'guerra mundos H.G. Wells invasao marciana alienigena terra'),
(36, 1, '8573266465', 'Crime e Castigo', 'Fiódor Dostoiévski', 'Editora 34', '2016-01-01', 'literatura estrangeira', 2, 60.00, 'crime-e-castigo-br.png', 'crime castigo Fiodor Dostoievski cometido ex estudante Rodion Ramanovich Raskolnikov consequencias'),
(37, 1, '8535907432', 'O processo', 'Franz Kafka', 'Companhia de Bolso', '2005-10-19', 'literatura estrangeira', 2, 25.00, 'o-processo-br.png', 'processo Franz Kafka Josef bancario preso processado crime que nao sabe labirinto burocratico legal'),
(38, 1, '8595200858', 'Dom Quixote', 'Miguel de Cervantes', 'Pé da Letra', '2018-04-09', 'literatura estrangeira', 2, 45.00, 'dom-quixote-br.png', 'Dom Quixote Miguel Cervantes aventuras desventuras homem meia idade cavaleiro andante sancho panca'),
(39, 1, '8563560565', 'Ilíada', 'Homero', 'Penguin-Companhia', '2013-02-06', 'literatura estrangeira', 2, 35.00, 'iliada-1-br.png', 'Iliada Homero poema epico cerco cidade Troia Aqueus resgatar Helena Menelau Paris Aquiles'),
(40, 1, '6586490707', 'Madame Bovary', 'Gustave Flaubert', 'Editora Antofágica', '2023-01-24', 'literatura estrangeira', 2, 35.00, 'madame-bovary-br.png', 'madame Bovary Gustave Flaubert narrativa realista critica sociedade burguesa Emma Charles realidade monotona'),
(41, 1, '8501115827', 'O nome da rosa (Edição especial)', 'Umberto Eco', 'Record', '2019-12-16', 'literatura estrangeira', 2, 65.00, 'nome-rosa-br.png', 'nome rosa Umberto Eco italia medieval mosteiro beneditino frei concilio clero investiga crimes heresia'),
(42, 1, '8595081514', 'O Pequeno Príncipe (Original): Tradução original com aquarelas do autor', 'Antoine de Saint-Exupéry', 'HarperCollins', '2018-08-27', 'literatura estrangeira', 2, 15.00, 'pequeno-principe-br.png', 'pequeno principe Antoine Saint Exupery menino amizade piloto de aviao asteroide 612 deserto Saara personagens solitarios'),
(43, 1, '8501061980', 'Amar se aprende amando', 'Carlos Drummond de Andrade', 'Record', '2001-01-01', 'poesia', 2, 45.00, 'amar-se-aprende-br.png', 'amar aprende amando Carlos Drummond Andrade sentimento amoroso amor sublime convivio ideal fusao amantes'),
(44, 1, '8535914080', 'Antologia Poética', 'Vinicius de Moraes', 'Companhia de Bolso', '2009-02-20', 'poesia', 3, 35.00, 'antologia-poetica-br.png', 'antologia poetica Vinicius Moraes espirito apaixonado irreverente vida obra poetinha'),
(45, 1, '858285093X', 'As flores do mal', 'Charles Baudelaire', 'Penguin-Companhia', '2019-10-04', 'poesia', 2, 45.00, 'flores-mal-br.png', 'flores mal Charles Baudelaire luxuria alienacao beleza literatura gotica confronta convencoes morais'),
(46, 1, '8520917941', 'Libertinagem E Estrela Da Manha', 'Manuel Bandeira', 'NOVA FRONTEIRA', '2008-01-01', 'poesia', 3, 25.00, 'libertinagem-e-estrela-br.png', 'libertinagem estrela manha Manuel Bandeira modernismo coloquialismo lirico rondo balada cantiga versos livres rimas refroes'),
(47, 1, '8525048860', 'Para Viver com Poesia', 'Mario Quintana', 'Biblioteca Azul', '2010-01-01', 'poesia', 2, 15.00, 'para-viver-poesia-br.png', 'para viver poesia Mario Quintana recortar eliminar destaque antologia forma critica temas dominantes'),
(48, 1, '8535922237', 'Toda poesia', 'Paulo Leminski', 'Companhia das Letras', '2013-02-27', 'poesia', 2, 45.00, 'toda-poesia-br.png', 'toda poesia Paulo Leminski haikais cancoes poemas concretos liricos autor curitibano'),
(49, 1, '6556660388', 'Vinte Poemas de Amor e uma Canção Desesperada: Edição Bilíngue', 'Pablo Neruda', 'L&PM', '2020-12-10', 'poesia', 2, 15.00, 'vinte-poemas-br.png', 'vinte poemas amor cancao desesperada Pablo Neruda essencia perda exaltacao amores vividos chile reverenciar feminino sensualidade'),
(50, 1, '1234567890', 'teste', 'Teste da Silva', 'SuperTeste', '2024-03-01', 'teste', 1, 10.00, 'livro.png', 'teste do teste com um livro cadastrado');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
