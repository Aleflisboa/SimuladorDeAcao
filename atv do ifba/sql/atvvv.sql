create database atividade;
use atividade;

show tables;

CREATE TABLE Cliente (
    cnh VARCHAR(20) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    estado VARCHAR(2),
    endereco VARCHAR(255),
    telefone VARCHAR(20)
);

CREATE TABLE Escritorio (
    escNum INT PRIMARY KEY,
    local VARCHAR(255) NOT NULL
);

CREATE TABLE Veiculo (
    veiNum INT PRIMARY KEY,
    placa VARCHAR(20) NOT NULL,
    data_manut DATE,
    disponivel BOOLEAN DEFAULT TRUE
);

CREATE TABLE Contrato (
    contNum INT PRIMARY KEY,
    data DATE NOT NULL,
    duracao INT NOT NULL,
    cnh VARCHAR(20),
    escNum INT,
    veiNum INT,
    FOREIGN KEY (cnh) REFERENCES Cliente(cnh),
    FOREIGN KEY (escNum) REFERENCES Escritorio(escNum),
    FOREIGN KEY (veiNum) REFERENCES Veiculo(veiNum)
);

 -- atividade2

create database atividade2;
use atividade2;


show tables;


CREATE TABLE filial (
    codigo INT PRIMARY KEY,
    endereco VARCHAR(255),
    telefone VARCHAR(20),
    nome VARCHAR(100)
);

CREATE TABLE funcionario (
    codigo INT PRIMARY KEY,
    nome VARCHAR(100),
    endereco VARCHAR(255),
    telefone VARCHAR(20),
    filial_codigo INT,
    FOREIGN KEY (filial_codigo) REFERENCES filial(codigo)
);

CREATE TABLE dependente (
    codigo INT PRIMARY KEY,
    nome VARCHAR(100),
    nascimento DATE,
    funcionario_codigo INT,
    FOREIGN KEY (funcionario_codigo) REFERENCES funcionario(codigo)
);

CREATE TABLE cliente (
    codigo INT PRIMARY KEY,
    nome VARCHAR(100),
    endereco VARCHAR(255),
    telefone VARCHAR(20)
);

CREATE TABLE cidade (
    codigo INT PRIMARY KEY,
    nome VARCHAR(100),
    estado VARCHAR(50)
);  

CREATE TABLE tipo (
    codigo INT PRIMARY KEY,
    descricao VARCHAR(100),
    peso DECIMAL(10,2)
);

CREATE TABLE veiculo (
    codigo INT PRIMARY KEY,
    placa VARCHAR(20) UNIQUE,
    tipo_codigo INT,
    FOREIGN KEY (tipo_codigo) REFERENCES tipo(codigo)
);

CREATE TABLE frete (
    codigo INT PRIMARY KEY,
    valor DECIMAL(10,2),
    cliente_codigo INT,
    veiculo_codigo INT,
    FOREIGN KEY (cliente_codigo) REFERENCES cliente(codigo),
    FOREIGN KEY (veiculo_codigo) REFERENCES veiculo(codigo)
);

CREATE TABLE categoria (
    codigo INT PRIMARY KEY,
    descricao VARCHAR(100),
    percentual DECIMAL(5,2)
);

CREATE TABLE distancia (
    origem_cg INT,
    destino_cg INT,
    quilometros DECIMAL(10,2),
    PRIMARY KEY (origem_cg, destino_cg),
    FOREIGN KEY (origem_cg) REFERENCES cidade(cg),
    FOREIGN KEY (destino_cg) REFERENCES cidade(cg)
);


SELECT * FROM veiculo;
SELECT nome FROM veiculo;
INSERT INTO cliente (nome)
VALUES ('João Silva'),('Maria Souza');


SELECT * FROM veiculo;
SELECT nome FROM veiculo;
INSERT INTO veiculo (placa) 
VALUES ('ABC-1234'),('XYZ-5678');


SELECT * FROM veiculo;
SELECT nome FROM veiculo;
INSERT INTO frete (cliente_id, veiculo_id, valor) 
VALUES (1, 1, 1500.00),(2, 2, 800.00);
 

