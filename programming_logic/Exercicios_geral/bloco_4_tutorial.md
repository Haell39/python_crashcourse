# 📚 BLOCO 4: Guia Detalhado com Pseudocódigo e Dicas

---

## 5️⃣ Verificador de Palíndromos

**O que é um palíndromo?**
Uma palavra/frase que se lê igual de trás pra frente.

**Exemplos:**
- "arara" → "arara" (é palíndromo)
- "racecar" → "racecar" (é palíndromo)
- "Arara" → convertir pra "arara" → "arara" (é palíndromo, ignorando maiúscula)
- "A man a plan a canal Panama" → "amanaplanacanalpanama" (é palíndromo, ignorando espaços)

---

## 📝 PSEUDOCÓDIGO - Verificador de Palíndromos

```
FUNÇÃO verificador_palindromo(texto):
    
    PASSO 1: Limpar o texto
    ├─ Converter tudo pra MINÚSCULA (usar .lower())
    ├─ Remover ESPAÇOS (usar .replace() ou similar)
    └─ Armazenar em uma variável "texto_limpo"
    
    PASSO 2: Inverter o texto
    ├─ Usar slicing [::-1] pra inverter
    ├─ Armazenar em uma variável "texto_invertido"
    └─ Dica: "abc"[::-1] vira "cba"
    
    PASSO 3: Comparar
    ├─ SE texto_limpo == texto_invertido
    │  └─ É palíndromo! Retornar True
    └─ SENÃO
       └─ Não é palíndromo! Retornar False
    
    PASSO 4: Usar a função
    ├─ Pedir entrada do usuário
    ├─ Chamar a função com a entrada
    └─ Printar o resultado
```

---

## 💡 DICAS - Palíndromo

**Dica 1: Remover espaços**
```python
texto = "A man a plan a canal Panama"
texto_sem_espacos = texto.replace(" ", "")
# "AmanaplanacanalPanama"
```

**Dica 2: Converter pra minúscula**
```python
texto = "ARARA"
texto_minusculo = texto.lower()
# "arara"
```

**Dica 3: Inverter com slicing**
```python
texto = "arara"
texto_invertido = texto[::-1]
# "arara"
```

**Dica 4: Combinar tudo**
```python
texto = "Arara"
# Passo 1: remover espaços
texto = texto.replace(" ", "")
# Passo 2: converter pra minúscula
texto = texto.lower()
# Passo 3: inverter
texto_invertido = texto[::-1]
# Passo 4: comparar
if texto == texto_invertido:
    print("É palíndromo!")
```

---

## ✅ Teste seu código com esses casos:

```python
# Deve retornar True
verificador_palindromo("arara")
verificador_palindromo("Arara")
verificador_palindromo("racecar")
verificador_palindromo("A man a plan a canal Panama")

# Deve retornar False
verificador_palindromo("python")
verificador_palindromo("hello")
```

---

---

## 6️⃣ Contador de Frequência

**O que é frequência?**
Quantas vezes cada elemento aparece em uma lista.

**Exemplo:**
```python
lista = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]

# Frequência:
# "maçã" aparece 3 vezes
# "banana" aparece 2 vezes
# "laranja" aparece 1 vez
```

---

## 📝 PSEUDOCÓDIGO - Contador de Frequência

```
FUNÇÃO contador_frequencia(lista):
    
    PASSO 1: Criar um dicionário vazio
    ├─ dicionario_frequencia = {}
    └─ Aqui vamos guardar: {elemento: quantas_vezes}
    
    PASSO 2: Iterar sobre a lista
    ├─ PARA CADA item NA lista:
    │  ├─ Verificar se o item JÁ está no dicionário
    │  │  ├─ SE sim: aumentar o contador (+1)
    │  │  └─ SE não: criar uma entrada com contador = 1
    │  └─ (Você pode usar .get() ou .count() ou verificar com 'in')
    └─ Continuar até terminar a lista
    
    PASSO 3: Exibir os resultados
    ├─ PARA CADA elemento E sua frequência NO dicionário:
    │  └─ Printar algo como: "maçã: 3 vezes"
    └─ Ou retornar o dicionário completo
```

---

## 💡 DICAS - Contador de Frequência

**Dica 1: Usar .count() (mais fácil)**
```python
lista = ["a", "b", "a", "c", "a"]
print(lista.count("a"))  # 3
print(lista.count("b"))  # 1
```

**Dica 2: Iterar e contar manualmente**
```python
lista = ["a", "b", "a"]
frequencia = {}

for item in lista:
    if item in frequencia:
        frequencia[item] = frequencia[item] + 1
    else:
        frequencia[item] = 1

print(frequencia)  # {"a": 2, "b": 1}
```

**Dica 3: Usar .get() (mais elegante)**
```python
frequencia = {}
for item in lista:
    frequencia[item] = frequencia.get(item, 0) + 1
    # .get() retorna 0 se a chave não existe

print(frequencia)  # {"a": 2, "b": 1}
```

**Dica 4: Evitar duplicatas ao contar**
```python
# Para evitar contar a mesma coisa 2x, 
# você pode usar um loop ou um set

# Opção 1: Usar set() pra pegar elementos únicos
elementos_unicos = set(lista)
# Depois contar cada um com .count()

# Opção 2: Usar um dicionário (como na dica 2 ou 3)
```

---

## ✅ Teste seu código com esses casos:

```python
# Teste 1: Números
lista1 = [1, 2, 1, 3, 1, 2, 2, 4]
# Esperado: 1 aparece 3x, 2 aparece 3x, 3 aparece 1x, 4 aparece 1x

# Teste 2: Nomes
lista2 = ["João", "Maria", "João", "Pedro", "Maria", "João"]
# Esperado: João 3x, Maria 2x, Pedro 1x

# Teste 3: Palavras
lista3 = ["python", "java", "python", "javascript", "python"]
# Esperado: python 3x, java 1x, javascript 1x
```

---

## 🎯 Resumo das Abordagens

### Palíndromo
1. **Entrada:** pedir texto do usuário
2. **Limpar:** remover espaços + minúsculas
3. **Inverter:** usar `[::-1]`
4. **Comparar:** `==`
5. **Retornar:** True ou False

### Frequência
1. **Entrada:** criar ou pedir uma lista
2. **Contar:** usar `.count()` OU um loop com dicionário
3. **Armazenar:** em um dicionário
4. **Exibir:** iterar e printar
5. **Retornar:** o dicionário ou printado

---

## 🚀 Próximos Passos

1. Tenta implementar usando o pseudocódigo
2. Testa com os casos de teste
3. Se travar, volta aqui e diz qual parte tá difícil
4. Não olha a resposta, pensa no que o pseudocódigo diz!

**Boa sorte!** 💪