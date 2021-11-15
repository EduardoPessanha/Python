CREATE TABLE caixa(
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Data DATE,
        Tipo VARCHAR(10),
        Descricao VARCHAR(300),
        Valor INTEGER(30),
        Saldo INTEGER(30),
        Obs VARCHAR(500)
        );