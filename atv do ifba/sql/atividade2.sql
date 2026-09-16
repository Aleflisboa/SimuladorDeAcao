INSERT INTO tipo (descricao, peso) VALUES
('Transporte leve', 500.5),
('Transporte médio', 1200.0),
('Transporte pesado', 3000.0),
('Transporte para carga perecível', 200.0),
('Transporte especial', 1500.0);


INSERT INTO cliente (nome, endereco) VALUES
('João Silva', 'Rua A, 123'),
('Maria Oliveira', 'Avenida B, 456'),
('Carlos Souza', 'Rua C, 789'),
('Ana Costa', 'Avenida D, 1011'),
('Paula Almeida', 'Rua E, 1213');

INSERT INTO filial (nome, telefone, endereco) VALUES
('Filial Centro', '+55 (75) 9999-9999', 'Rua Principal, 100'),
('Filial Norte', '+55 (75) 9888-8888', 'Avenida Norte, 200'),
('Filial Sul', '+55 (75) 9777-7777', 'Rua Sul, 300'),
('Filial Leste', '+55 (75) 9666-6666', 'Avenida Leste, 400'),
('Filial Oeste', '+55 (75) 9555-5555', 'Rua Oeste, 500');

INSERT INTO veiculo (placa, descricao, cod_tipo, cod_filial, marca) VALUES
('ABC-1234', 'Caminhão de carga', 1, 1, 'Fiat'),
('DEF-5678', 'Van de transporte', 2, 2, 'Volksvagem'),
('GHI-9101', 'Carro de passeio', 1, 3, 'Ford'),
('JKL-1122', 'Furgão', 3, 4, 'Fiat'),
('MNO-3344', 'Ônibus', 2, 5, 'Volksvagem');

INSERT INTO funcionario (nome, endereco, telefone, cod_filial) VALUES
('José Pereira', 'Rua F, 123', '+55 (75) 9999-5555', 1),
('Cláudia Souza', 'Rua G, 456', '+55 (75) 9999-6666', 2),
('Carlos Mendes', 'Avenida H, 789', '+55 (75) 9999-7777', 3),
('Fernanda Lima', 'Rua I, 101', '+55 (75) 9999-8888', 4),
('Ricardo Silva', 'Avenida J, 112', '+55 (75) 9999-9999', 5);

INSERT INTO dependente (nome, nascimento) VALUES
('Ana Pereira', '2010-05-10'),
('João Souza', '2012-08-15'),
('Carla Mendes', '2008-02-20'),
('Luiz Lima', '2014-11-30'),
('Pedro Silva', '2016-03-25');

INSERT INTO funcionario_dependente (cod_funcionario, cod_dependente) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);


INSERT INTO cidade (nome, estado) VALUES
('Salvador', 'BA'),
('Fortaleza', 'CE'),
('Recife', 'PE'),
('Maceió', 'AL'),
('Natal', 'RN');


INSERT INTO distancia (quilomentos, cod_cidade_origem, cod_cidade_destino) VALUES
(250, 1, 2),
(400, 2, 3),
(150, 3, 4),
(300, 4, 5),
(500, 1, 3);


INSERT INTO categoria (descricao, percentual) VALUES
('Categoria A', 5.00),
('Categoria B', 10.00),
('Categoria C', 15.00),
('Categoria D', 20.00),
('Categoria E', 25.00);


INSERT INTO frete (valor, cod_cliente) VALUES
(150.00, 1),
(200.00, 2),
(300.00, 3),
(400.00, 4),
(500.00, 5);

INSERT INTO frete_distancia (cod_distancia, cod_frete) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);


INSERT INTO frete_categoria (cod_categoria, cod_frete) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);


INSERT INTO frete_veiculo (cod_veiculo, cod_frete, data_frete) VALUES
(1, 1, '2025-03-26'),
(2, 2, '2025-03-26'),
(3, 3, '2025-03-26'),
(4, 4, '2025-03-26'),
(5, 5, '2025-03-26');




