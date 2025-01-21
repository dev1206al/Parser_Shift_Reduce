"""
El código implementa un parser Shift-Reduce, un algoritmo utilizado para analizar cadenas 
en base a una gramática definida. Este tipo de parser opera mediante dos acciones principales:
    Shift: Mueve el siguiente símbolo de la entrada a la pila.
    Reduce: Reemplaza un patrón en la pila con el lado izquierdo de una regla de producción de la gramática.
"""
class ShiftReduceParser:
    """
    Clase para implementar un parser Shift-Reduce que analiza cadenas
    basadas en una gramática definida en un archivo de texto.
    """

    def __init__(self, grammar_file):
        """
        Constructor de la clase ShiftReduceParser.
        Inicializamos el parser cargando la gramatica desde un archivo y preparamos una pila vacia para el analisis.
        @param grammar_file: Archivo que contiene la gramática.
        """
        # Leer la gramática desde el archivo
        self.grammar = self.load_grammar(grammar_file)
        self.stack = []  # Pila para tokens

    def load_grammar(self, file_path):
        """
        Carga la gramática desde un archivo .txt y la organiza en un diccionario.
        Lee cada línea del archivo de la grámatica
            - Divide la regla en:
                - Lado izq: No terminal, como S.
                - Lado der: Una lista de simbolos ['A', 'B']
            - Almacena las reglas en un diccionario:
                - Clave: Regla completa ("S -> A B")
                - Valor: Lista de simbolos del lado derecho (['A','B'])
        @param file_path: Ruta del archivo que contiene la gramática.
        @return: Un diccionario donde las claves son las reglas completas y los valores
                 son las partes derechas de las producciones.
        """
        grammar = {}
        with open(file_path, 'r') as file:
            for line in file:
                # Dividir la regla en lado izquierdo y derecho usando el separador '→'
                rule = line.strip().split('→')
                left = rule[0].strip()  # Lado izquierdo de la regla
                right = rule[1].strip().split()  # Lado derecho dividido en símbolos
                # Almacenar la regla en el diccionario
                grammar[f'{left} → {" ".join(right)}'] = right
        return grammar
    
    def display_grammar(self):
        print("\nGramática cargada:")
        for rule, right_side in self.grammar.items():
            print(f"{rule}")


    def display(self, input_tokens):
        """
        Muestra el estado actual de la pila y la entrada en cada paso del análisis.

        @param input_tokens: Lista de símbolos que quedan por analizar.
        """
        print(f"Pila: {self.stack} | Entrada: {' '.join(input_tokens)}")

    def parse(self, input_string):
        """
        Analiza una cadena de entrada utilizando el algoritmo Shift-Reduce.
        Convertimos la entrada en tokens y agrega el símbolo de fin de cadena.
        @param input_string: La cadena que se desea analizar.
        @return: True si la cadena es aceptada, False si no lo es.
        """
        # Convertir la entrada en tokens y agregar el símbolo de fin de cadena '$'
        input_tokens = input_string.split() + ['$']
        self.stack = []  # Vaciar la pila al iniciar el análisis
        
        print("\nIniciando análisis shift-reduce...\n")

        while len(input_tokens) > 0:
            # Mostrar el estado actual
            self.display(input_tokens)
        
            # Intentar reducir si es posible
            # Reduccion: Busca si la parte superior de la pila coincide con el patrón del lado derecho de una regla.
            # Si coincide, remplaza esa parte de la pila con el lado izquierdo de la regla.

            reduced = False
            for rule, pattern in self.grammar.items():
                # Comprobar si la parte superior de la pila coincide con el patrón de una regla
                if self.stack[-len(pattern):] == pattern:
                    # Realizar la reducción
                    self.stack = self.stack[:-len(pattern)]  # Quitar el patrón de la pila
                    left_side = rule.split('→')[0].strip()  # Obtener el lado izquierdo
                    self.stack.append(left_side)  # Reemplazar con el lado izquierdo
                    print(f"Reducido por regla: {rule}")
                    reduced = True
                    break

            # Si no se pudo reducir, realizar un shift
            # Mueve el siguiente token de la entrada a la pila.
            if not reduced:
                self.stack.append(input_tokens.pop(0))  # Mover el primer token de entrada a la pila
                print("Shift realizado.")

            # Verificar si la pila contiene solo el símbolo inicial y '$' está en la entrada
            #Si la pila contiene solo el simbolo inicial y la entrada $, la cadena es aceptada
            if self.stack == [list(self.grammar.keys())[0].split('→')[0].strip()] and input_tokens == ['$']:
                print("\nCadena aceptada.\n")
                return True

        # Si no se puede reducir, la cadena es rechazada.
        print("\nError de sintaxis. Cadena no aceptada.\n")
        return False


# -----------------------------------------------
# Lógica Principal
# -----------------------------------------------
if __name__ == "__main__":
    """
    Punto de entrada del programa. Carga una gramática desde un archivo,
    solicita cadenas al usuario y analiza cada cadena usando el parser.
    """
    # Solicitar el archivo con la gramática
    grammar_file = input("Ingresa el nombre del archivo con la gramática (ej. 'gramatica.txt'): ")
    
    # Crear el parser con la gramática cargada
    parser = ShiftReduceParser(grammar_file)

    #Mostrar la gramática cargada
    parser.display_grammar()

    while True:
        # Solicitar la cadena a analizar
        cadena = input("\nIngresa una cadena para analizar (o escribe 'salir' para terminar): ")
        
        if cadena.lower() == 'salir':
            break
        
        # Ejecutar el análisis
        parser.parse(cadena)

#Gram1 Formulas matematicas basicas.
#Gram2 Ingreso de id pares.
#Gram3 Formato correcto Nombres y Apellidos.
#Gram4 Formato de fecha en México
#Gram5 Formato de fecha basico
#Gram6 Ejemplo ( a ,0 ( a , a ))