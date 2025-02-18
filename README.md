My files of Python course and using git\github


# Curso Python - Curso em Vídeo

## Configuração para MacBook M3

### 1. Instalar Homebrew ✅
Abra o Terminal e execute:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 2. Instalar Python ✅

brew install python@3.12

### 3. Atualizar pip para última versão ✅

python3 -m pip install --upgrade pip

### 4. Verificar instalações ✅

python3 --version
pip3 --version

### 5. Configurar Ambiente Virtual
```bash
# Criar o ambiente virtual
python3 -m venv venv

# Ativar o ambiente virtual
source venv/bin/activate

# Para desativar quando necessário
deactivate
```

### 6. Instalar dependências no ambiente virtual ✅
# Com o ambiente virtual ativado, execute:
pip3 install -r requirements.txt

### Dicas importantes:
- Sempre use `python3` em vez de `python`
- Use `pip3` em vez de `pip`
- Para executar seus scripts: `python3 nome_do_arquivo.py`
- Sempre ative o ambiente virtual antes de trabalhar no projeto
- O diretório `venv` já está no `.gitignore`

### Gerenciando Dependências
```bash
# Para listar todas as bibliotecas instaladas
pip3 freeze

# Para salvar as dependências no requirements.txt
pip3 freeze > requirements.txt

# Para instalar dependências de um projeto
pip3 install -r requirements.txt
```

### Verificando Ambiente Virtual
```bash
# Ver se ambiente está ativo (deve mostrar (venv) no início do prompt)
(venv) usuario@computador %

# Ver qual Python está sendo usado
which python3

# Listar bibliotecas do ambiente atual
pip3 list

# Ativar ambiente virtual
source venv/bin/activate

# Desativar ambiente virtual
deactivate
```

### Ambiente Configurado! ✅
Seu ambiente está pronto para iniciar o curso de Python.