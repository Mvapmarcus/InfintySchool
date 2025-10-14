# ProvaPYA05
# Processador de Texto Simples com Funções Lambda

def processador_texto(texto, **kwargs):
    texto_original = texto

    if 'contar_palavras' in kwargs and kwargs['contar_palavras']:
        contar_palavras = lambda t: len(t.split())
        print(f"Número de palavras: {contar_palavras(texto)}")
    
    if 'contar_letras' in kwargs and kwargs['contar_letras']:
        contar_letras = lambda t: len(t.replace(" ", ""))
        print(f"Número de letras (sem espaços): {contar_letras(texto)}")
    
    if 'substituir_palavra' in kwargs and 'nova_palavra' in kwargs:
        palavra_antiga = kwargs['substituir_palavra']
        palavra_nova = kwargs['nova_palavra']
        substituir_palavra = lambda t, old, new: t.replace(old, new)
        texto = substituir_palavra(texto, palavra_antiga, palavra_nova)
        print(f"Texto após substituição: {texto}")
    
    texto_invertido = texto_original
    if 'inverter_texto' in kwargs and kwargs['inverter_texto']:
        inverter_texto = lambda t: t[::-1]
        texto_invertido = inverter_texto(texto_original)
        print(f"Texto original invertido: {texto_invertido}")
    
    return texto_original, texto, texto_invertido

# Exemplo de uso
texto_inicial = "Olá mundo! Este é um exemplo de processador de texto simples."
texto_original, texto_processado, texto_invertido = processador_texto(
    texto_inicial, 
    contar_palavras=True, 
    contar_letras=True, 
    substituir_palavra="texto", 
    nova_palavra="frases",
    inverter_texto=True
)

