import re
import time


def preprocess_text(text):
    text = text.lower()  # Convertir a minúsculas
    words = re.findall(r'\w+', text)  # Dividir en palabras
    return words  # Devolver la lista de palabras


def memoized_count_words(words):
    memo = {}  # Diccionario que sirve como cache
    for word in words:
        if word not in memo:
            # Función count, cuenta las ocurrencias de una palabra
            memo[word] = words.count(word)
    return memo


def memoized_count_words_without_stop_words(words, stop_words):
    memo = {}
    for word in words:
        # Excluir palabras de la lista de stop_words
        if word not in stop_words:
            if word not in memo:
                memo[word] = words.count(word)
    return memo


def count_words_in_documents(documents, stop_words, use_stop_words=True):
    # Combinar todos los documentos en un solo texto
    combined_text = ' '.join(documents)

    # Preprocesar el texto y contar las ocurrencias de las palabras
    words = preprocess_text(combined_text)
    if use_stop_words:
        word_count = memoized_count_words(words)
    else:
        word_count = memoized_count_words_without_stop_words(words, stop_words)

    # Ordenar y mostrar las palabras más repetidas
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    for word, count in sorted_words:
        if count > 2:  # Puedes ajustar este umbral según tus necesidades
            print(f"{word.ljust(15)} {count}")


def build_inverted_index(documents):
    inverted_index = {}
    for idx, document in enumerate(documents):
        words = document.lower().split()  # Dividir el documento en palabras
        for word in words:
            if word in inverted_index:
                inverted_index[word].append(idx)  # Agregar el índice del documento
            else:
                inverted_index[word] = [idx]  # Crear una nueva entrada en el índice
    return inverted_index


def search_word_in_inverted_index(word, inverted_index):
    word = word.lower()
    if word in inverted_index:
        return inverted_index[word]
    else:
        return []

def main():
    my_documents = ["La programación en Python es clave para el trabajo con datos",
                    "Los programadores en Java tienen un alto interés en pasar a Python",
                    "La optimización de algoritmos es fundamental en el desarrollo de software",
                    "Las bases de datos relacionales son esenciales para muchas aplicaciones",
                    "El paradigma de programación funcional gana popularidad",
                    "La seguridad informática es un tema crucial en el desarrollo de aplicaciones web",
                    "Los lenguajes de programación modernos ofrecen abstracciones poderosas",
                    "La inteligencia artificial está transformando diversas industrias",
                    "El aprendizaje automático es una rama clave de la ciencia de datos",
                    "Las interfaces de usuario intuitivas mejoran la experiencia del usuario",
                    "La calidad del código es esencial para mantener un proyecto exitoso",
                    "La agilidad en el desarrollo de software permite adaptarse a cambios rápidamente",
                    "Las pruebas automatizadas son cruciales para garantizar la estabilidad del software",
                    "La modularización del código facilita la colaboración en equipos de programadores",
                    "El control de versiones es necesario para rastrear cambios en el código",
                    "La documentación clara es fundamental para que otros entiendan el código",
                    "La programación orientada a objetos promueve la reutilización de código",
                    "La resolución de problemas es una habilidad esencial en la programación",
                    "La optimización prematura puede llevar a código complicado y difícil de mantener",
                    "El diseño de interfaces de usuario atractivas mejora la usabilidad de las aplicaciones",
                    "El código limpio es esencial para facilitar el mantenimiento",
                    "Los patrones de diseño son soluciones probadas para problemas comunes",
                    "Las pruebas unitarias garantizan el correcto funcionamiento de las partes del código",
                    "El desarrollo ágil prioriza la entrega continua de valor al cliente",
                    "Los comentarios en el código deben ser claros y útiles",
                    "La recursividad es una técnica poderosa en la programación",
                    "Las bibliotecas de código abierto aceleran el desarrollo de software",
                    "La virtualización permite una mejor utilización de los recursos de hardware",
                    "La seguridad en la programación web es fundamental para prevenir ataques",
                    "Los principios SOLID son fundamentales para el diseño de software robusto",
                    "La arquitectura de microservicios permite escalar componentes individualmente",
                    "La refactorización mejora la calidad del código sin cambiar su comportamiento",
                    "Los sistemas distribuidos presentan desafíos en la sincronización de datos",
                    "El enfoque DevOps une el desarrollo y las operaciones para una entrega eficiente",
                    "Las bases de datos NoSQL son útiles para manejar datos no estructurados",
                    "La agilidad en el desarrollo permite adaptarse a cambios del mercado",
                    "Las buenas prácticas en el control de versiones facilitan la colaboración",
                    "La programación concurrente mejora la eficiencia en sistemas multiusuario",
                    "Los marcos de trabajo MVC separan la lógica de la interfaz de usuario",
                    "La interacción entre aplicaciones se logra a través de APIs",
                    "El machine learning permite a las máquinas aprender de los datos",
                    "La analítica de datos ayuda a tomar decisiones basadas en información",
                    "El diseño responsivo garantiza una experiencia consistente en diferentes dispositivos",
                    "Las pruebas de carga verifican el rendimiento de las aplicaciones",
                    "El enfoque centrado en el usuario mejora la usabilidad de las aplicaciones",
                    "La programación reactiva es útil para manejar flujos de datos asincrónicos",
                    "Los contenedores facilitan la implementación y el despliegue de aplicaciones",
                    "La gestión de dependencias es esencial para administrar las bibliotecas externas",
                    "La integración continua automatiza la verificación de cambios en el código",
                    "El aprendizaje profundo es una rama avanzada del machine learning",
                    "La depuración es una habilidad crucial para encontrar y corregir errores",
                    "La criptografía protege la información sensible en aplicaciones",
                    "El desarrollo full-stack abarca tanto el frontend como el backend",
                    "Las pruebas de seguridad ayudan a identificar vulnerabilidades en el software",
                    "La agilidad cultural es clave para adoptar prácticas ágiles de manera efectiva",
                    "La infraestructura como código permite automatizar la gestión de servidores",
                    "Los patrones arquitectónicos guían la estructura general de una aplicación",
                    "El análisis predictivo utiliza datos históricos para predecir tendencias",
                    "Las interfaces API REST son ampliamente utilizadas para comunicarse con aplicaciones",
                    "El rendimiento de las aplicaciones es esencial para brindar una buena experiencia",
                    "La virtualización de servidores reduce costos y facilita la administración",
                    "La ingeniería de software implica la aplicación de métodos sistemáticos",
                    "El código autodocumentado es claro y fácil de entender para otros programadores",
                    "La integración de sistemas conecta diferentes aplicaciones para trabajar juntas",
                    "Las metodologías ágiles promueven la adaptación y la colaboración continua",
                    "El monitoreo de aplicaciones permite identificar y resolver problemas en tiempo real",
                    "El análisis de datos masivos (big data) abre oportunidades para obtener insights",
                    "El diseño de interfaces de usuario es crucial para la experiencia del usuario",
                    "La seguridad en el desarrollo es un proceso constante de mitigación de riesgos"]

    # Lista de palabras a excluir
    stop_words = ['de', 'el', 'la', 'en', 'un', 'una', 'para', 'con', 'es', 'y', 'los', 'las', 'por', 'se', 'al', 'del', 'a']

    inverted_index = build_inverted_index(my_documents)


    while True:
        print("Menú:")
        print("1. Contar palabras más repetidas con stop words")
        print("2. Contar palabras más repetidas sin stop words")
        print("3. Buscar palabra en documentos")
        print("4. Salir")
        choice = input("Seleccione una opción (1/2/3/4): ")

        if choice == "1":
            inicio = time.time()
            count_words_in_documents(my_documents, stop_words, use_stop_words=True)
            fin = time.time()
            duracion = fin - inicio
            print(f"Tiempo de ejecución: {duracion:.6f} segundos")

        elif choice == "2":
            inicio = time.time()
            count_words_in_documents(
                my_documents, stop_words, use_stop_words=False)
            fin = time.time()
            duracion = fin - inicio
            print(f"Tiempo de ejecución: {duracion:.6f} segundos")

        elif choice == "3":
            word_to_search = input("Seleccione palabra a buscar: ").lower()
            inicio = time.time()
            matching_indices = search_word_in_inverted_index(word_to_search, inverted_index)
            if matching_indices:
                print(f'"{word_to_search}": {matching_indices}')
            else:
                print(f'"{word_to_search}" no se encontró en ningún documento.')
            fin = time.time()
            duracion = fin - inicio
            print(f"Tiempo de ejecución: {duracion:.100f} segundos")

        elif choice == "4":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Seleccione una opción válida (1/2/3/4).")
if __name__ == "__main__":
    main()
